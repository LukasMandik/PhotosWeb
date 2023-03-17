from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

class Photo(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos_web/static/media')
    image_name = models.CharField(max_length=200, blank=True, null=True,)
    description = models.TextField()

    def save(self, *args, **kwargs):
        if self.image and not self.image_name:
            self.image_name = self.image.name
        super(Photo, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class MetaPhoto(models.Model):
    photo = models.OneToOneField(Photo, on_delete=models.CASCADE, related_name='meta')
    make = models.CharField(max_length=200, null=True, blank=True)
    model = models.CharField(max_length=200, null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.photo.name} - {self.make} {self.model}"


