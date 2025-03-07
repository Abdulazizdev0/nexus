from django.db import models
from category.models import Region, Category, Brand
from user.models import Profile


class Product(models.Model):
    condition_types = [
        (1,'New'),
        
    ]
