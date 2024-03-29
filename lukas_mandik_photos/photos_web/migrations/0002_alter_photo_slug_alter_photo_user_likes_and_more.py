# Generated by Django 4.1.5 on 2023-04-05 16:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos_web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='user_likes',
            field=models.ManyToManyField(blank=True, related_name='liked_photos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
