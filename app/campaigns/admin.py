from django.contrib import admin

from campaigns.models import Campaign, Question, Response, QRCode


class QRCodeAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at", "deleted_at"]

class CampaignAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at", "deleted_at"]


class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at", "deleted_at"]


class ResponseAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at", "deleted_at"]


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Response, ResponseAdmin)
admin.site.register(QRCode, QRCodeAdmin)
