from django.db import models
from django.urls import reverse

class Photo(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos_web/static/media')
    image_name = models.CharField(max_length=200, blank=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        if self.image:
            self.image_name = self.image.name
        super(Photo, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
