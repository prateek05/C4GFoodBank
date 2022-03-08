# Generated by Django 4.0.3 on 2022-03-08 04:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('campaign_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('actor_type', models.CharField(choices=[('client', 'Client'), ('agent', 'Agent'), ('staff', 'Staff'), ('volunteer', 'Volunteer')], max_length=25, null=True)),
                ('active', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'campaigns',
            },
        ),
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=200)),
                ('qr_code_path', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'qr_codes',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=1000)),
                ('answer_choices', models.CharField(blank=True, max_length=1000)),
                ('answer_template', models.CharField(choices=[('text', 'Text'), ('radio', 'Radio'), ('check', 'CheckBox')], max_length=25, null=True)),
                ('language', models.CharField(choices=[('EN', 'English')], default='EN', max_length=2)),
                ('active', models.BooleanField()),
                ('additional_info', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'questions',
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('response_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('language', models.CharField(choices=[('EN', 'English')], default='EN', max_length=2)),
                ('value', models.CharField(max_length=1000)),
                ('location', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responses', to='campaigns.question')),
            ],
            options={
                'db_table': 'responses',
            },
        ),
    ]
