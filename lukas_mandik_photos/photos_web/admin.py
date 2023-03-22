from django.contrib import admin

from . import models
from .models import Photo, Category





# Register your models here.
# admin.site.register(models.Photo)
admin.site.register(models.Category)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_name', 'category', 'timestamp','png_image']
    list_filter = []
    list_editable = ['category']
    # prepopulated_fields = {'slug': ('name',)}
