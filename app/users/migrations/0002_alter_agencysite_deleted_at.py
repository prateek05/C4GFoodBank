# Generated by Django 4.0.3 on 2022-03-08 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencysite',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]