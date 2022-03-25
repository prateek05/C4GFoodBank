from django.contrib import admin

from campaigns.models import Campaign, QRCode, Question, Response


class QRCodeAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at", "deleted_at"]


class CampaignAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at", "deleted_at"]

    def save_model(self, request, obj, form, change):
        if not change:
           obj.create_by = request.user 
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at", "deleted_at"]


class ResponseAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at", "deleted_at"]


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Response, ResponseAdmin)
admin.site.register(QRCode, QRCodeAdmin)
