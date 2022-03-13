# Generated by Django 4.0.3 on 2022-03-11 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("campaigns", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="answer_choices",
            field=models.CharField(
                blank=True,
                help_text="Example choice format for a radio or check answer template ['Red','Blue','Green']",
                max_length=1000,
            ),
        ),
        migrations.AlterField(
            model_name="response",
            name="location",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]