# Generated by Django 4.0.2 on 2022-03-01 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='qrcode',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
