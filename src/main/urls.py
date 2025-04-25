from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('category/',category, name='category.urls'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
]