from django.contrib import admin
from .models import Brands, Products, ProductDetails
# Register your models here.

admin.site.register(Brands)
admin.site.register(Products)
admin.site.register(ProductDetails)
