# Generated by Django 4.1.5 on 2023-03-18 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos_web', '0005_remove_photo_datetime_remove_photo_make_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metaphoto',
            name='model',
        ),
        migrations.AddField(
            model_name='metaphoto',
            name='gps',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
