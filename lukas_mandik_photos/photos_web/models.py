import json
from datetime import datetime

from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image, ExifTags


class Photo(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/photos/')
    image_name = models.CharField(max_length=200, blank=True, null=True,)
    description = models.TextField()
    orientation = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    device = models.CharField(max_length=200, blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    gps_coordinates = models.CharField(max_length=100, blank=True, null=True)
    meta_data = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        img = Image.open(self.image)
        exif_data_raw = img._getexif()
        exif_data = {}

        if exif_data_raw:
            for tag, value in exif_data_raw.items():
                if tag in ExifTags.TAGS:
                    exif_data[ExifTags.TAGS[tag]] = value

                    # Save orientation
                    if "Orientation" in exif_data:
                        self.orientation = exif_data["Orientation"]

                    # Save timestamp
                    if "DateTimeOriginal" in exif_data:
                        date_time_str = exif_data["DateTimeOriginal"]
                        date_time_obj = datetime.strptime(date_time_str, "%Y:%m:%d %H:%M:%S")
                        self.timestamp = date_time_obj

                    # Save device
                    if "Model" in exif_data:
                        self.device = f"{exif_data['Model']}"

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

        if self.image and not self.image_name:
            self.image_name = self.image.name
        super(Photo, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.device} {self.timestamp}"


    @staticmethod
    def convert_to_decimal(value, ref):
        degrees, minutes, seconds = value
        result = degrees + (minutes / 60.0) + (seconds / 3600.0)
        if ref in ['S', 'W']:
            result = -result
        return result







