from django.contrib import admin

from users.models import AgencySite, CampaignUser


class CampaignUserAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at", "deleted_at"]
    ordering=("-created_at", "-updated_at")


class SurverySiteAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at", "deleted_at"]
    ordering=("-created_at", "-updated_at")


admin.site.register(CampaignUser, CampaignUserAdmin)
admin.site.register(AgencySite, SurverySiteAdmin)
