from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Brands
from .models import Phones

def index(request):
    context = {
        "brand_list": Brands.objects.all()
    }
    return render(request, "index.html", context)

def indexPhone(request):
    context = {
        "Phone_list": Phones.objects.all()
    }
    return render(request, "index.html", context)
