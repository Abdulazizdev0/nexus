from django.shortcuts import render
from .models import *

def product_list(request):
    categories = Category.objects.filter(is_main=True)
    regions = Region.objects.all()

    ctx = {
        "categories":categories,
        "regions":regions


    }
    return render(request,'products.html',ctx)

def product_detail(request,pk):
    products = Product.objects.get(pk=pk)
    ctx = {
        "products":products

    }
    return render(request,'detail.html',ctx)
