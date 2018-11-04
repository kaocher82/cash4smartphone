from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Brands
def index(request):
    context = {
        "brand_list": Brands.objects.all()
    }
    return render(request, "index.html", context)
