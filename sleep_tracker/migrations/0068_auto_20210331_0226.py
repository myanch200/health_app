# Generated by Django 3.1.6 on 2021-03-31 01:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sleep_tracker', '0067_auto_20210331_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sleep',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 31, 2, 26, 25, 141792)),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 31, 2, 26, 25, 141755)),
        ),
    ]
