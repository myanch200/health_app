# Generated by Django 3.1.6 on 2021-03-26 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sleep_tracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sleep',
            name='end',
        ),
        migrations.RemoveField(
            model_name='sleep',
            name='start',
        ),
    ]