import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# User model
class CampaignUser(AbstractUser):
    class Meta:
        db_table = "campaign_users"

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)


# Agency Site Info
class AgencySite(models.Model):
    class Meta:
        db_table = "agency_sites"

    site_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=200, null=False)
    latitude = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    address = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return f"Site {self.name}"
