from os import path

import qrcode
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
                url = f"{settings.BASE_URL}/api/survey/{slug}"
                img = qrcode.make(f"{url}")
                img.save(qr_code_path)
                QRCode.objects.create(
                    slug=slug, qr_code_path=qr_code_path, site=site, campaign=instance
                )
