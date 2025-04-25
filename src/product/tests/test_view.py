import pytest
from product.models import Product,ProductImage,Profile
from django.urls import reverse
from category.models import *
from user.models import Profile
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile


def test_product_list(client):
    category1 = Category.objects.create(name='Tech', is_main=True, slug='Tech')
    region1 = Region.objects.create(name='Sclotland',sorting='99'),
    region2 = Region.objects.create(name='New Zelland',sorting='88'),
