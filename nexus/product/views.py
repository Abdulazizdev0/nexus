from django.shortcuts import render
from django.db.models import Prefetch
from .models import *
from hitcount.views import HitCountDetailView, HitCountMixin
from hitcount.utils import get_hitcount_model
# from django.core.paginator import Paginator
from user.views import logout_view



def product_list(request,):
    categories = Category.objects.filter(is_main=True)
    regions = Region.objects.all()
    products = Product.objects.prefetch_related(Prefetch('images',
            queryset=ProductImage.objects.filter(is_main=True),to_attr='main_images'))
    # p = Paginator(products,4)
    # page = request.GET.get('page')
    # _product = p.get_page(page)
    # nums = "s"*product_list.paginator.num_pages
    ctx = {
        "categories":categories,
        "regions":regions,
        "products":products,
        # "_product":_product,
        # "nums":nums

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

def product_add(request):
    categories = Category.objects.filter(is_main=True)
    regions = Region.objects.all()

    ctx={
        "categories":categories,
        "regions":regions,

    }
    return render(request,'product_add.html',ctx)




