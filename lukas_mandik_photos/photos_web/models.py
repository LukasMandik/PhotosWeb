from django.db import models
from PIL import Image, ExifTags, ImageStat
from datetime import datetime
import os
from django.utils.timezone import make_aware
from django.contrib.auth.models import User
from django.forms import IntegerField
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('photos_web:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Photo(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(blank=True, null=True,)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    # webp_image = models.ImageField(upload_to='photos_web/static/photos', blank=True, null=True)
    png_image = models.ImageField(blank=True, null=True)
    image_name = models.CharField(max_length=200, blank=True, null=True,)
    file_name = models.CharField(max_length=200, blank=True, null=True,)
    description = models.TextField()
    timestamp = models.DateTimeField(blank=True, null=True)
    device = models.CharField(max_length=200, blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    gps_coordinates = models.CharField(max_length=100, blank=True, null=True)
    meta_data = models.TextField(blank=True, null=True)

    image_mode = models.CharField(max_length=10, blank=True, null=True)
    image_size = models.CharField(max_length=100, blank=True, null=True)
    bands = models.CharField(max_length=100, blank=True, null=True)
    mean = models.CharField(max_length=100, blank=True, null=True)
    median = models.CharField(max_length=100, blank=True, null=True)
    std_dev = models.CharField(max_length=100, blank=True, null=True)
    brightness = models.CharField(max_length=100, blank=True, null=True)

    likes = models.PositiveIntegerField(default=0)
    user_likes = models.ManyToManyField(User, related_name='liked_photos', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):

        if self.image and not self.image_name:
            self.image_name = self.image.name

        if self.image and not self.file_name:
              # self.file_name = os.path.basename(self.image.name)
            # Extract the file name without the extension
            base_name, _ = os.path.splitext(self.image.name)
            self.file_name = os.path.basename(base_name)

        super(Photo, self).save(*args, **kwargs)

        img = Image.open(self.image)
        exif_data_raw = img._getexif()
        exif_data = {}

        if exif_data_raw:
            for tag, value in exif_data_raw.items():
                if tag in ExifTags.TAGS:
                    exif_data[ExifTags.TAGS[tag]] = value

                    # Save timestamp
                    if "DateTimeOriginal" in exif_data:
                        date_time_str = exif_data["DateTimeOriginal"]
                        date_time_obj = datetime.strptime(date_time_str, "%Y:%m:%d %H:%M:%S")
                        aware_datetime = make_aware(
                            date_time_obj)  # Konverzia na dátum a čas s informáciami o časovej zóne
                        self.timestamp = aware_datetime

                    # Save device
                    if "Model" in exif_data and "Make" in exif_data:
                        self.device = f"{exif_data['Model']} {exif_data['Make']}"

                    # Save width and height
                    self.width, self.height = img.size

                    # Save GPS coordinates
                    if "GPSInfo" in exif_data:
                        gps_info = exif_data["GPSInfo"]
                        gps_latitude = gps_info.get(2, None)
                        gps_latitude_ref = gps_info.get(1, None)
                        gps_longitude = gps_info.get(4, None)
                        gps_longitude_ref = gps_info.get(3, None)

                        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
                            latitude = self.convert_to_decimal(gps_latitude, gps_latitude_ref)
                            longitude = self.convert_to_decimal(gps_longitude, gps_longitude_ref)
                            self.gps_coordinates = f"{latitude}, {longitude}"

                    # Save EXIF data to meta_data
                    self.meta_data = exif_data

        # # Convert the image to WebP format
        # width, height = img.size
        # new_size = (width // 7, height // 7)
        # img.thumbnail(new_size)
        #
        # webp_image_path = os.path.splitext(self.image.path)[0] + '.webp'
        # img.save(webp_image_path, 'WEBP', quality=100, lossless=True)
        # self.webp_image.name = os.path.join('photos_web', 'static', 'photos', os.path.basename(webp_image_path))

        # Convert the image to PNG format
        img = Image.open(self.image.path)

        width, height = img.size
        new_size = (width // 7, height // 7)
        img.thumbnail(new_size)

        png_image_path = os.path.splitext(self.image.path)[0] + '.png'
        img.save(png_image_path, 'PNG', compress_level=9)
        self.png_image.name = os.path.join(os.path.basename(png_image_path))

        img = Image.open(self.image.path)
        stats = ImageStat.Stat(img)

        self.image_mode = img.mode
        self.image_size = str(img.size)
        self.bands = ', '.join(img.getbands())
        self.mean = ', '.join(map(str, stats.mean))
        self.median = ', '.join(map(str, stats.median))
        self.std_dev = ', '.join(map(str, stats.stddev))
        self.brightness = ', '.join(map(str, stats.rms))

        super(Photo, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('photos_web:view_photo', args=[self.slug])

    def __str__(self):
        return f"{self.name} {self.image}"


    @staticmethod
    def convert_to_decimal(value, ref):
        degrees, minutes, seconds = value
        result = degrees + (minutes / 60.0) + (seconds / 3600.0)
        if ref in ['S', 'W']:
            result = -result
        return result


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.CharField(max_length=200, default='admin')
    description = models.TextField(blank=True)
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('photos_web:product_detail', args=[self.slug])

    def __str__(self):
        return self.name


