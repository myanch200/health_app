# Generated by Django 3.1.6 on 2021-03-28 10:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition_planner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='text',
            field=ckeditor.fields.RichTextField(default='Default'),
            preserve_default=False,
        ),
    ]
