# Generated by Django 3.1.6 on 2021-03-28 12:38

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition_planner', '0037_auto_20210328_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='categories',
            field=models.TextField(blank=True, help_text='Separate categories with ;', null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(blank=True, help_text='Separate ingredients with ;', null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='content',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
