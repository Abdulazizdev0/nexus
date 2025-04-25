from django.urls import path,include
from .views import *



urlpatterns = [
    path('',ProfileGenericApiView.as_view()),
    path('profile/<int:pk>/',ProfileGenericApiMixinsdetail.as_view()),
    path('profilenomixin/<int:pk>/',ProfileGenericApidetail.as_view())
]
