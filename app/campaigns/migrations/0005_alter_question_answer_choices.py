# Generated by Django 4.0.3 on 2022-03-13 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("campaigns", "0004_alter_question_answer_choices"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="answer_choices",
            field=models.CharField(
                blank=True,
                help_text="Example choice format for a radio or check answer template: Red, Blue, Green",
                max_length=1000,
            ),
        ),
    ]
