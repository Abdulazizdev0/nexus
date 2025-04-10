from django.urls import path
from .views import *

urlpatterns = [
    path('list/', product_list, name='product-list'),
    path('detail/<int:pk>/', product_detail, name='product-detail'),
    path('product_add/',product_add,name='product_add'),
    path('dashboard/',dashboard,name='dashboard'),
    path('myads/',my_ads,name='myads'),
    path('messages/',messages,name='messages'),
    path('payment/',payment,name='payment'),
    path('favourite/',favourite,name='favourite'),
    path('setting/',user_setting,name='setting')

]