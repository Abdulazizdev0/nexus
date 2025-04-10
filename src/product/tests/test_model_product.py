import pytest
from product.models import Product,ProductView,ProductImage,Profile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from category.models import *

def test_create_product():
    user = User.objects.create(username="Ibrohim",password="password")
    image = SimpleUploadedFile( name='test_image.jpg',content=b'some_image_data_here',content_type='image/jpeg')
    profile = Profile.objects.create(user=user,firstname="Aziz",last_name="Yunusov",phone_number="+998909009090",image=image)
    region = Region.objects.create(name="Bali", sorting=7)
    category = Category.objects.create(name="Elektronikaa",is_main=True,slug="elektronika")
    brand = Brand.objects.create(name="HP")
    product = Product.objects.create(
        title="HP",
        description="ertyuikjhgfdcvbnpuytresxcvbnm",
        location=region,
        category=category,
        brand=brand,
        user=profile,
        price=999,
        )

    assert product.title == "HP"
    assert product.description == "ertyuikjhgfdcvbnpuytresxcvbnm"
    assert product.location == region
    assert product.category == category
    assert product.brand == brand
    assert product.user == profile
    assert product.price == 999
    assert product.created_at is not None
    assert product.updated_at is not None