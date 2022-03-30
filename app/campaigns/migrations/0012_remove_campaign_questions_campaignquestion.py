# Generated by Django 4.0.3 on 2022-03-30 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0011_alter_question_answer_choices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='questions',
        ),
        migrations.CreateModel(
            name='CampaignQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, help_text='Value needs to be > 0')),
                ('campaign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='campaigns.campaign')),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='campaigns.question')),
            ],
            options={
                'db_table': 'campaign_questions',
            },
        ),
    ]
