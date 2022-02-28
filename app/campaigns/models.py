import uuid

from django.db import models


# Campaign Questions Info Model
class Question(models.Model):
    class Meta:
        db_table = "questions"

    TEMPLATE_TYPES = [("text", "Text"), ("radio", "Radio"), ("check", "CheckBox")]
    LANGUAGE_TYPES = [("EN", "English")]
    questionn_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    question = models.CharField(max_length=1000, null=False, blank=False)
    answer_choices = models.CharField(max_length=1000, null=False, blank=False)
    answer_template = models.CharField(max_length=25, null=True, choices=TEMPLATE_TYPES)
    language = models.CharField(max_length=2, default="EN", choices=LANGUAGE_TYPES)
    active = models.BooleanField()
    additional_info = models.CharField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField()
    create_by = models.ForeignKey(
        "users.CampaignUser",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="questions_created",
    )


# Response Info Model
class Response(models.Model):
    class Meta:
        db_table = "responses"

    response_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(
        Question,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="responses",
    )
    site_id = models.ForeignKey(
        "users.AgencySite",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="responses",
    )
    value = models.CharField(max_length=1000, null=False)
    location = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField()


# Campaign Model
class Campaign(models.Model):
    class Meta:
        db_table = "campaigns"

    ACTOR_TYPE_CHOICES = [
        ("client", "Client"),
        ("agent", "Agent"),
        ("staff", "Staff"),
        ("volunteer", "Volunteer"),
    ]
    campaign_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False)
    slug = models.SlugField(null=False)
    questions = models.ManyToManyField(Question)
    sites = models.ManyToManyField("users.AgencySite")
    create_by = models.ForeignKey(
        "users.CampaignUser",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="campaigns_created",
    )
    actor_type = models.CharField(max_length=25, null=True, choices=ACTOR_TYPE_CHOICES)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField()

#Site QRCode Model
class QRCode(models.Model):
    class Meta:
        db_table = "qr_codes"

    slug = models.SlugField(null=False)
    qr_code_path = models.URLField()
    site = models.ForeignKey(
        "users.AgencySite", on_delete=models.SET_NULL, blank=True, null=True, related_name="qr_codes"
    )
    campaign = models.ForeignKey(
        Campaign, on_delete=models.SET_NULL, blank=True, null=True, related_name="qr_codes"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField()