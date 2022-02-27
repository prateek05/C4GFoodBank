import uuid

from django.db import models


# User model
class CampaignUser(models.Model):
    class Meta:
        db_table = "campaign_users"

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField("email address", unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField()


# Agency Site Info
class AgencySite(models.Model):
    class Meta:
        db_table = "agency_sites"

    site_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    latitude = models.DecimalField(max_digits=10, decimal_places=4)
    longitude = models.DecimalField(max_digits=10, decimal_places=4)
    address = models.CharField(max_length=200, null=False)
    point_of_contact = models.ForeignKey(
        CampaignUser, on_delete=models.SET_NULL, blank=True, null=True, related_name="+"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField()
