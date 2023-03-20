# Generated by Django 4.1.5 on 2023-03-19 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos_web', '0014_remove_photo_meta_data2'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='bands',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='brightness',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='image_mode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='image_size',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='mean',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='median',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='std_dev',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='MetaPhoto',
        ),
    ]