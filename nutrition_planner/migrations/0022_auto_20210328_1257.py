# Generated by Django 3.1.6 on 2021-03-28 11:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition_planner', '0021_auto_20210328_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nutrition',
            name='grams',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 12, 57, 30, 359614)),
        ),
    ]
