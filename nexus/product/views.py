from django.shortcuts import render,redirect
from django.db.models import Prefetch
from django.http import HttpResponse
from .models import *
from hitcount.views import HitCountDetailView, HitCountMixin
from hitcount.utils import get_hitcount_model
# from django.core.paginator import Paginator
from user.views import logout_view
from user.models import Profile
from .forms import ProductForm, ProductImageFormSet



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
    profiles = Profile.objects.all()
    if request.method == "POST":
        form = ProductForm(request.POST)
        formset = ProductImageFormSet(request.POST, request.FILES)  # Rasmlarni qabul qilish

        if form.is_valid() and formset.is_valid():
            product = form.save(commit=False)
            product.user = request.user.profile  # Foydalanuvchi bilan bog‘lash
            product.save()

            images = formset.save(commit=False)
            for image in images:
                image.product = product  # Har bir rasmni mahsulot bilan bog‘lash
                image.save()

            return HttpResponse("Product added successfully")
    else:
        form = ProductForm()
        formset = ProductImageFormSet()



    ctx={
       "profiles":profiles,
        "form":form,
        "formset":formset

    }
    return render(request,'product_add.html',ctx)




