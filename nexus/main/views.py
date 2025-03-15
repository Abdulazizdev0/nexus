from django.shortcuts import render
from category.models import *

def main(request):
    categories = Category.objects.filter(is_main=True)
    regions = Region.objects.all()
    ctx = {
        "categories": categories,
        "regions":regions
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





