# Generated by Django 3.1.6 on 2021-04-03 13:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sleep_tracker', '0076_auto_20210402_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sleep',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 3, 14, 49, 36, 443814)),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 3, 14, 49, 36, 443785)),
        ),
    ]
