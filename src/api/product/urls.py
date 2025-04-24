from django.urls import path
from .views import ProductView,ProductDetailView

urlpatterns = [
    path('', ProductView.as_view(), name='product-list'),
    path('detail/<int:pk>/',ProductDetailView.as_view())
]

