# Generated by Django 3.1.6 on 2021-03-28 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition_planner', '0046_remove_recipe_cook_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cook_time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]