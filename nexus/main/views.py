from django.shortcuts import render
from category.models import *
from product.models import *
from django.db.models import Prefetch



def main(request):
    categories = Category.objects.filter(is_main=True)
    regions = Region.objects.all()
    products = Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images')).all()


    ctx = {
        "categories": categories,
        "regions":regions,
        "products":products,

    }


    return render(request, 'index.html', ctx)

def category(request):
    categories = Category.objects.filter(is_main=True)
    regions = Region.objects.all()
    aaa = {
        "categories": categories,
        "regions": regions
    }
    return render(request,'category.html',aaa)





