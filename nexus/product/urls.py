from django.urls import path
from .views import product_list, product_detail,product_add

urlpatterns = [
    path('list/', product_list, name='product-list'),
    path('detail/<int:pk>/', product_detail, name='product-detail'),
    path('product_add/',product_add,name='product_add')
]