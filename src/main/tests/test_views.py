from django.urls import reverse
from category.models import Category, Region, Brand
from product.models import Product
from blog.models import Blog, BlogCategory
from hitcount.models import HitCount
import pytest
from user.models import Profile
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.mark.django_db
def test_main_view(client):
    Blog.objects.all().delete()
    User.objects.all().delete()
    Profile.objects.all().delete()
    Product.objects.all().delete()
    Region.objects.all().delete()
    Category.objects.all().delete()

    category1 = Category.objects.create(name='Tech', is_main=True, slug='tech')
    region1 = Region.objects.create(name='usa', sorting='44')
    region2 = Region.objects.create(name='usa2', sorting='55')

    user1 = User.objects.create(username="djalil", password="password")
    image = SimpleUploadedFile(name='test_image.jpg', content=b'some_image_data_here', content_type='image/jpeg')
    profile1 = Profile.objects.create(user=user1, firstname="Shorasul", last_name="Lazizov",
                                      phone_number="+998909009090", image=image)


    region = Region.objects.create(name="Bali", sorting=7)
    product_category = Category.objects.create(name="Elektronikaaa", is_main=True, slug="elektronika")
    brand = Brand.objects.create(name="HP")
    product = Product.objects.create(
        title="MAC",
        description="Some description for MAC.",
        location=region,
        category=product_category,
        brand=brand,
        user=profile1,
        price=999,
    )


    blog_category = BlogCategory.objects.create(name="Kiyim", is_main=True, slug="kiyim")


    user_blog1 = User.objects.create(username="Bosit", password="bosit")
    user_blog2 = User.objects.create(username="Karamatillo", password="password")

    profile_blog1 = Profile.objects.create(user=user_blog1, firstname="Madaminov", last_name="Madamin",
                                           phone_number="+998909009090", image=image)
    profile_blog2 = Profile.objects.create(user=user_blog2, firstname="Karamatillo", last_name="Mahmudjanov",
                                           phone_number="+998909009090", image=image)


    blog1 = Blog.objects.create(
        author=profile_blog1,
        title="asdfghjkl",
        description="Some random text for blog 1",
        category=blog_category,
        image=image
    )

    blog2 = Blog.objects.create(
        author=profile_blog2,
        title="asdfghjkk",
        description="Some random text for blog 2",
        category=blog_category,
        image=image
    )


    url = reverse('main')
    response = client.get(url)


    assert response.status_code == 200
    assert "blogs" in response.context
    assert len(response.context["blogs"]) == 2
    content = response.content.decode()
    assert "asdfghjkl" in content
    assert "asdfghjkk" in content

    assert "regions" in response.context
    assert len(response.context["regions"]) == 3
    content = response.content.decode()
    assert "usa" in content
    assert "usa2" in content

    assert product.title == "MAC"
    assert product.description == "Some description for MAC."
    assert product.location == region
    assert product.category == product_category
    assert product.brand == brand
    assert product.user == profile1  
    assert product.price == 999
    assert product.created_at is not None
    assert product.updated_at is not None
