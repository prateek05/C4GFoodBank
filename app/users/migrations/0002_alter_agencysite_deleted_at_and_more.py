# Generated by Django 4.0.2 on 2022-03-01 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="agencysite",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="campaignuser",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
    ]