from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("", views.button, name="button"),
#    path("<str:Brands_manufacturer>", views.BrandPhone, name="phones")
]
