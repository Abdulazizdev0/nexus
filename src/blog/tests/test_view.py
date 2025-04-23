import pytest
from django.urls import reverse
from blog.models import Blog,BlogCategory
from user.models import Profile
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

@pytest.mark.django_db
def test_blog_page_view(client):
    Blog.objects.all().delete()
    user = User.objects.create(username="Rahmatillo", password="password")
    image = SimpleUploadedFile(name='test_image.jpg', content=b'some_image_data_here', content_type='image/jpeg')
    profile = Profile.objects.create(
        user=user,
        firstname="Rahmatillo",
        last_name="Yunusov",
        phone_number="+998888008080",
        image=image
    )
    category = BlogCategory.objects.create(name='Tech',is_main=True,slug='Tech')

    Blog.objects.create(
        author=profile,
        title="Test Blog 1",
        description="Description 1",
        category=category,
        image=image
    )

    Blog.objects.create(
        author=profile,
        title="Test Blog 2",
        description="Description 2",
        category=category,
        image=image
    )

    url = reverse('blog')
    response = client.get(url)

    assert response.status_code == 200
    assert "blogs" in response.context
    assert len(response.context["blogs"]) == 2


    content = response.content.decode()
    assert "Test Blog 1" in content
    assert "Test Blog 2" in content


