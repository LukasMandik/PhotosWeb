from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractProduct, AbstractAttributeOption, AbstractAttributeOptionGroup

class AttributeOptionGroup(AbstractAttributeOptionGroup):
    pass

class AttributeOption(AbstractAttributeOption):
    group = models.ForeignKey(AttributeOptionGroup, on_delete=models.CASCADE, related_name='options')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


class Product(AbstractProduct):
    attribute_options = models.ManyToManyField(AttributeOption, blank=True, related_name='products')
    video_url = models.URLField()

    def get_price(self):
        selected_options = self.attribute_options.all()
        if selected_options.exists():
            price = sum(option.price for option in selected_options)
            return price
        return super().get_price()


from oscar.apps.catalogue.models import *  # noqa isort:skip
