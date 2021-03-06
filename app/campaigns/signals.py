from os import path

import qrcode
from cloudstorage import get_driver_by_name
from django.conf import settings
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from campaigns.models import Campaign, QRCode

options = {
    'acl': 'public-read',
    'content_type': 'image/png'
}

# TODO: Change driver cls attributes based on CLOUD PARTNER
# TODO: Auto Detect CLOUD PARTNER ENVIRONMENT AND LOOK FOR KEYS FROM KV
driver_cls = get_driver_by_name(settings.CLOUD_PARTNER)
storage = driver_cls(account_name=settings.OBJECT_CONTAINER_NAME, key=settings.ACCESS_KEY)


@receiver(m2m_changed, sender=Campaign.sites.through)
def init_new_qr_code(instance, action, reverse, model, **kwargs):
    if action == "post_add" and not reverse:
        for site in instance.sites.all():
            filename = (
                f"{instance.name.replace(' ', '-').replace('/','-')}_{site.name.replace(' ', '-').replace('/','-')}.png"
            )
            qr_code_path = f"{settings.QR_CODE_STORAGE_LOCATION}/{filename}"
            if not path.isfile(qr_code_path):
                slug = f"{instance.campaign_id}/{site.site_id}"
                url = f"{settings.BASE_WEB_URL}/survey/{slug}"
                img = qrcode.make(f"{url}")
                img.save(qr_code_path)
                if settings.OBJECT_CONTAINER_NAME:
                    try:
                        container = storage.get_container(settings.OBJECT_CONTAINER_NAME)
                        picture_blob = container.upload_blob(qr_code_path, **options)
                        qr_code_path = picture_blob.cdn_url
                    except:
                         print("image removal failed")
                QRCode.objects.create(
                    slug=slug, qr_code_path=qr_code_path, site=site, campaign=instance
                )
