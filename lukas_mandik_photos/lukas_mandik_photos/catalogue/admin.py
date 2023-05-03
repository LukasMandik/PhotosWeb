from django.contrib import admin
from oscar.apps.catalogue.admin import ProductAdmin as CoreProductAdmin
from oscar.apps.catalogue.admin import *  # noqa



admin.site.unregister(Product)
admin.site.register(Product, ProductAdmin)






