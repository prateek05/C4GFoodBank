# Generated by Django 4.0.3 on 2022-03-17 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0005_alter_question_answer_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='qr_code_path',
            field=models.URLField(),
        ),
    ]