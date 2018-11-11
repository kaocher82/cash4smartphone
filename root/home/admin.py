from django.contrib import admin
from .models import Brands, Products, Phones
# Register your models here.

admin.site.register(Brands)
admin.site.register(Products)
admin.site.register(Phones)
