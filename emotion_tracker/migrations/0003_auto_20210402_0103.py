# Generated by Django 3.1.6 on 2021-04-02 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emotion_tracker', '0002_auto_20210402_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='diary',
            name='emotion',
            field=models.CharField(choices=[('happy', 'Happy'), ('exited', 'Exited'), ('angry', 'Angry'), ('sad', 'Sad')], max_length=300),
        ),
    ]
