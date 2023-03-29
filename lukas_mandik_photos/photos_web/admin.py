from django.contrib import admin

from . import models
from .models import Photo, Category, Product


# Register your models here.
# admin.site.register(models.UserProfile)
# admin.site.register(models.Category)
@admin.register(Category)
class CateroryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'category', 'timestamp',]
    list_filter = []
    list_editable = ['category']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'category', 'slug', 'photo',
                    'price', 'is_active', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
