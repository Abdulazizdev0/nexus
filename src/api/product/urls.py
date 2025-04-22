from django.urls import path
from .views import get_list_pr

urlpatterns = [
    path('', get_list_pr, name='product-list'),
    # path('detail/<int:pk>/',detail_ctg)
]

