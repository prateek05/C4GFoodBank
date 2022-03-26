from django.contrib import admin
from django import forms
import csv
from django.urls import path
from django.http import HttpResponse
from campaigns.models import Campaign, QRCode, Question, Response, AnswerChoice
from django.shortcuts import render, redirect
from io import StringIO
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        fields = [field for field in meta.get_fields()]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response, delimiter='|', quotechar= '`', quoting=csv.QUOTE_NONE)
        field_names = []
        for field in fields:
            if field.many_to_one:
                field_names.append(f"{field.name}_id")
            else:
                field_names.append(field.name)
        writer.writerow( field_names )
        for obj in queryset:
            data = []
            for field in fields:
                try:
                    if field.many_to_many == True or field.one_to_many == True:
                        data.append([str(value) for value in getattr(obj, field.name).all().values_list('pk',flat=True)])
                        # data.append("")
                    elif field.many_to_one == True: 
                        data.append(getattr(obj, field.name).pk)
                    else:
                        data.append(getattr(obj, field.name))
                except Exception as e:
                    print(e)
                    
            row = writer.writerow(data)

        return response

    export_as_csv.short_description = "Export Selected"

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

class QRCodeAdmin(admin.ModelAdmin, ExportCsvMixin):
    readonly_fields = ["created_at", "updated_at", "deleted_at"]
    list_filter = ('site', 'campaign')
    ordering=("-created_at", "-updated_at")
    actions = ["export_as_csv"]


class CampaignAdmin(admin.ModelAdmin, ExportCsvMixin):
    change_list_template = "entities/change_list.html"

    readonly_fields = ["created_at", "updated_at", "deleted_at", 'create_by', 'updated_by', "campaign_id"]
    list_filter = ('sites', 'campaign_owner', 'create_by', 'updated_by', 'actor_type', 'active')
    filter_horizontal = ('questions','sites') 
    ordering=("-created_at", "-updated_at")
    actions = ["export_as_csv"]

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls
    
    def import_csv(self, request):
        if request.method == "POST":
            uploaded_file = request.FILES["csv_file"].read().decode('utf-8')
            reader = csv.DictReader(StringIO(uploaded_file),delimiter='|', quotechar= '`', quoting=csv.QUOTE_NONE)
            for row in reader:
                Campaign.objects.update_or_create(campaign_id=row["campaign_id"], defaults={k: v for k, v in row.items() if v and k != "campaign_id" })
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "csv_form.html", payload
        )

    def save_model(self, request, obj, form, change):
        if not change:
           obj.create_by = request.user 
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


class QuestionAdmin(admin.ModelAdmin, ExportCsvMixin):
    change_list_template = "entities/change_list.html"
    readonly_fields = ["created_at", "updated_at", "deleted_at",  "question_id"]
    list_filter = ('answer_template', 'language', 'active')
    filter_horizontal = ['answer_choices'] 
    ordering=("-created_at", "-updated_at")
    actions = ["export_as_csv"]

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls
    
    def import_csv(self, request):
        if request.method == "POST":
            uploaded_file = request.FILES["csv_file"].read().decode('utf-8')
            reader = csv.DictReader(StringIO(uploaded_file),delimiter='|', quotechar= '`', quoting=csv.QUOTE_NONE)
            for row in reader:
                Question.objects.update_or_create(question_id=row["question_id"], defaults={k: v for k, v in row.items() if v and k != "question_id" })
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "csv_form.html", payload
        )
class ResponseAdmin(admin.ModelAdmin, ExportCsvMixin):
    readonly_fields = ["created_at", "updated_at", "deleted_at",  "response_id"]
    list_filter = ('site', 'language', 'location', "created_at", "updated_at")
    ordering=("-created_at", "-updated_at")
    actions = ["export_as_csv"]

class AnswerChoiceAdmin(admin.ModelAdmin, ExportCsvMixin):
    change_list_template = "entities/change_list.html"
    readonly_fields = ["created_at", "updated_at", "deleted_at",  "answer_id"]
    ordering=("-created_at", "-updated_at")
    actions = ["export_as_csv"]

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls
    
    def import_csv(self, request):
        if request.method == "POST":
            uploaded_file = request.FILES["csv_file"].read().decode('utf-8')
            reader = csv.DictReader(StringIO(uploaded_file),delimiter='|',quotechar= '`', quoting=csv.QUOTE_NONE)
            for row in reader:
                AnswerChoice.objects.update_or_create(answer_id=row["answer_id"], defaults={k: v for k, v in row.items() if v and k != "answer_id" })
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "csv_form.html", payload
        )

admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Response, ResponseAdmin)
admin.site.register(QRCode, QRCodeAdmin)
admin.site.register(AnswerChoice, AnswerChoiceAdmin)
