from django.urls import path,include
from .views import get_list_user



urlpatterns = [
    path('',get_list_user)
]
