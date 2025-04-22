from django.shortcuts import render
from category.models import *
from product.models import *
from blog.models import Blog
from django.db.models import Prefetch
from hitcount.views import HitCountDetailView, HitCountMixin
from hitcount.utils import get_hitcount_model



def main(request):
    categories = Category.objects.filter(is_main=True)
    regions = Region.objects.all()
    products = Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images'))


    hits = {}
    for product in products:
        hit_count = get_hitcount_model().objects.get_for_object(product)
        hits[product.id] = hit_count.hits

        hit_count_response = HitCountMixin.hit_count(request, hit_count)
        if hit_count_response.hit_counted:
            hits[product.id] += 1
    blogs = Blog.objects.all()
    ctx = {
        "categories": categories,
        "regions":regions,
        "products":products,
        "hits":hits,
        "blogs":blogs

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





