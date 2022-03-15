from os import path, remove

import boto3
import qrcode
from azure.storage.blob import BlobServiceClient
from django.conf import settings
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from campaigns.models import Campaign, QRCode
from users.models import AgencySite

session = boto3.Session(
    aws_access_key_id=settings.ACCESS_KEY,
    aws_secret_access_key=settings.SECRET_ACCESS_KEY,
)
client = session.client("s3", region_name="us-east-1")
s3_resource = session.resource("s3")


@receiver(m2m_changed, sender=Campaign.sites.through)
def init_new_qr_code(instance, action, reverse, model, **kwargs):
    if action == "post_add" and not reverse:
        for site in instance.sites.all():
            filename = (
                f"{instance.name.replace(' ','-')}_{site.name.replace(' ' ,'-')}.png"
            )
            qr_code_path = f"{settings.QR_CODE_STORAGE_LOCATION}/{filename}"
            if not path.isfile(qr_code_path):
                slug = f"{instance.campaign_id}/{site.site_id}"
                url = f"{settings.BASE_WEB_URL}/survey/{slug}"
                img = qrcode.make(f"{url}")
                img.save(qr_code_path)
                if settings.S3_BUCKET:
                    # service = BlobServiceClient(
                    #     account_url=settings.ACCOUNT_URL,
                    #     credential=settings.ACCOUNT_ACCESS_KEY,
                    # )
                    # blob_client = service.get_blob_client(
                    #     container=settings.QR_CODE_CONTAINER,
                    #     blob=f"{instance.name}_{site.name}.png",
                    # )
                    # image_content_setting = ContentSettings(content_type="image/jpeg")
                    # print(f"uploading file")
                    # with open(qr_code_path, "rb") as data:
                    #     blob_client.upload_blob(
                    #         data, overwrite=True, content_settings=image_content_setting
                    #     )
                    try:
                        client.upload_file(
                            qr_code_path, settings.S3_BUCKET, f"{filename}"
                        )
                        object_acl = s3_resource.ObjectAcl(
                            settings.S3_BUCKET, f"{filename}"
                        )
                        response = object_acl.put(ACL="public-read")
                        remove(qr_code_path)
                    except:
                        print("image removal failed")
                    qr_code_path = (
                        f"https://{settings.S3_BUCKET}.s3.amazonaws.com/{filename}"
                    )
                    # qr_code_path = blob_client.make_blob_url(
                    #     container=settings.QR_CODE_CONTAINER,
                    #     blob=f"{instance.name}_{site.name}.png",
                    #     protocol="https",
                    # )
                QRCode.objects.create(
                    slug=slug, qr_code_path=qr_code_path, site=site, campaign=instance
                )
