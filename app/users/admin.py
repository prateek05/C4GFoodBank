import csv
from io import StringIO

from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import path

from campaigns.admin import CsvImportForm, ExportCsvMixin
from users.models import AgencySite, CampaignUser


class CampaignUserAdmin(admin.ModelAdmin, ExportCsvMixin):
    change_list_template = "entities/change_list.html"

    readonly_fields = ["created_at", "updated_at", "deleted_at"]
    ordering = ("-created_at", "-updated_at")
    actions = ["export_as_csv"]

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("import-csv/", self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            uploaded_file = request.FILES["csv_file"].read().decode("utf-8")
            reader = csv.DictReader(
                StringIO(uploaded_file),
                delimiter="|",
                quotechar="`",
                quoting=csv.QUOTE_NONE,
            )
            for row in reader:
                CampaignUser.objects.update_or_create(
                    user_id=row["user_id"],
                    defaults={k: v for k, v in row.items() if v and k != "user_id"},
                )
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(request, "csv_form.html", payload)


class SurverySiteAdmin(admin.ModelAdmin, ExportCsvMixin):
    change_list_template = "entities/change_list.html"
    readonly_fields = ["created_at", "updated_at", "deleted_at"]
    ordering = ("-created_at", "-updated_at")
    actions = ["export_as_csv"]

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("import-csv/", self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            uploaded_file = request.FILES["csv_file"].read().decode("utf-8")
            reader = csv.DictReader(
                StringIO(uploaded_file),
                delimiter="|",
                quotechar="`",
                quoting=csv.QUOTE_NONE,
            )
            for row in reader:
                AgencySite.objects.update_or_create(
                    site_id=row["site_id"],
                    defaults={k: v for k, v in row.items() if v and k != "site_id"},
                )
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(request, "csv_form.html", payload)


admin.site.register(CampaignUser, CampaignUserAdmin)
admin.site.register(AgencySite, SurverySiteAdmin)
