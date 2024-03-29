# Generated by Django 3.1.6 on 2021-03-28 11:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition_planner', '0007_auto_20210328_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('kcal', 'kcal'), ('fat', 'fat'), ('saturates', 'saturates'), ('carbs', 'carbs'), ('sugars', 'sugars'), ('fibre', 'fibre'), ('protein', 'protein'), ('salt', 'salt')], max_length=120)),
            ],
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='text',
        ),
        migrations.AddField(
            model_name='recipe',
            name='cook_time',
            field=models.CharField(default='10 minutes', max_length=100),
        ),
        migrations.AddField(
            model_name='recipe',
            name='prep_time',
            field=models.CharField(default='10 minutes', max_length=100),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 12, 23, 3, 259514)),
        ),
    ]
