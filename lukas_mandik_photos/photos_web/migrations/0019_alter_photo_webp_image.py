# Generated by Django 4.1.5 on 2023-03-20 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos_web', '0018_alter_photo_webp_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='webp_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/photos/'),
        ),
    ]