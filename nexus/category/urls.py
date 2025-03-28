from django.urls import path
from .models import Region
from .views import region

urlpatterns = [

    path("",region,name='region')

]