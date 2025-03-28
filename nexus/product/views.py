from django.shortcuts import render
from django.db.models import Prefetch
from .models import *
from hitcount.views import HitCountDetailView, HitCountMixin
from hitcount.utils import get_hitcount_model



def product_list(request,):
    categories = Category.objects.filter(is_main=True)
    regions = Region.objects.all()
    products = Product.objects.prefetch_related(Prefetch('images',
            queryset=ProductImage.objects.filter(is_main=True),to_attr='main_images'))
    ctx = {
        "categories":categories,
        "regions":regions,
        "products":products


    }
    return render(request,'products.html',ctx)

def product_detail(request,pk):
    product = Product.objects.get(pk=pk)
    images = product.images.all()
    hit_count = get_hitcount_model().objects.get_for_object(product)
    hits = hit_count.hits
    hit_count_response = HitCountMixin.hit_count(request,hit_count)
    if hit_count_response.hit_counted:
        hits += 1
    ctx = {
        "product":product,
        "images":images,
        "hits":hits

    }
    return render(request,'detail.html',ctx)
