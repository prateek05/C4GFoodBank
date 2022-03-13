from os import path, remove

import qrcode
from azure.storage.blob import BlobServiceClient
from django.conf import settings
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from campaigns.models import Campaign, QRCode
from users.models import AgencySite


@receiver(m2m_changed, sender=Campaign.sites.through)
def init_new_qr_code(instance, action, reverse, model, **kwargs):
    if action == "post_add" and not reverse:
        for site in instance.sites.all():
            qr_code_path = (
                f"{settings.QR_CODE_STORAGE_LOCATION}/{instance.name}_{site.name}.png"
            )
            if not path.isfile(qr_code_path):
                slug = f"{instance.campaign_id}/{site.site_id}"
                url = f"{settings.BASE_WEB_URL}/survey/{slug}"
                img = qrcode.make(f"{url}")
                img.save(qr_code_path)
                if settings.ACCOUNT_URL:
                    service = BlobServiceClient(
                        account_url=settings.ACCOUNT_URL,
                        credential=settings.ACCOUNT_ACCESS_KEY,
                    )
                    blob_client = service.get_blob_client(
                        container=settings.QR_CODE_CONTAINER,
                        blob=f"{instance.name}_{site.name}.png",
                    )
                    image_content_setting = ContentSettings(content_type="image/jpeg")
                    print(f"uploading file")
                    with open(qr_code_path, "rb") as data:
                        blob_client.upload_blob(
                            data, overwrite=True, content_settings=image_content_setting
                        )
                    remove(qr_code_path)
                    qr_code_path = blob_client.make_blob_url(
                        container=settings.QR_CODE_CONTAINER,
                        blob=f"{instance.name}_{site.name}.png",
                        protocol="https",
                    )
                QRCode.objects.create(
                    slug=slug, qr_code_path=qr_code_path, site=site, campaign=instance
                )
