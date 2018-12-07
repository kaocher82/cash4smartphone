from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.http import Http404


# Create your views here.
from .models import Brand
from .models import Product
from .models import Catagory


def button(request):
    button = {
        "button_list": Catagory.objects.all()
    }
    return render(request, "base.html", context=button)
    
    
def index(request):
    context = {
        "brand_list": Brand.objects.all()
#        "Phone_list": Phone.objects.all()
    }

    return render(request, "index.html", context)
'''
def BrandPhone(request, Brands_id):
    try:
        Brand_phone = Phones.object.get(pk=Brands_id)
    except Brands.DoseNotExist:
        raise Http404(" Brands Dose Not Exist ")
    context = {
        "Phone_list": phones
    }
    return render(request, "brand.html", context)
'''
