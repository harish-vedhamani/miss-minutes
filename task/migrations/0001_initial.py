# Generated by Django 3.2.6 on 2024-06-19 16:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=255, null=True)),
                ('task_title', models.CharField(max_length=255, null=True)),
                ('task_discription', models.CharField(max_length=255, null=True)),
                ('original_estimate', models.IntegerField(max_length=25, null=True)),
                ('duration', models.CharField(max_length=255, null=True)),
                ('task_status', models.CharField(max_length=255, null=True)),
                ('assigned_user', models.CharField(max_length=255, null=True)),
                ('project_name', models.CharField(max_length=255, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
