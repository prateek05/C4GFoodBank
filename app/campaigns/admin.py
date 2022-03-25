from django.contrib import admin

from campaigns.models import Campaign, QRCode, Question, Response, AnswerChoice


class QRCodeAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at", "deleted_at"]
    list_filter = ('site', 'campaign')
    ordering=("-created_at", "-updated_at")


class CampaignAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at", "deleted_at", 'create_by', 'updated_by', "campaign_id"]
    list_filter = ('sites', 'campaign_owner', 'create_by', 'updated_by', 'actor_type', 'active')
    filter_horizontal = ('questions','sites') 
    ordering=("-created_at", "-updated_at")

    def save_model(self, request, obj, form, change):
        if not change:
           obj.create_by = request.user 
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at", "deleted_at"]
    list_filter = ('answer_template', 'language', 'active')
    filter_horizontal = ['answer_choices'] 
    ordering=("-created_at", "-updated_at")

class ResponseAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at", "deleted_at"]
    list_filter = ('site', 'language', 'location', "created_at", "updated_at")
    ordering=("-created_at", "-updated_at")

class AnswerChoiceAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at", "deleted_at"]
    ordering=("-created_at", "-updated_at")

admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Response, ResponseAdmin)
admin.site.register(QRCode, QRCodeAdmin)
admin.site.register(AnswerChoice, AnswerChoiceAdmin)
