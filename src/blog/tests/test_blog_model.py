import pytest
from django.contrib.auth.models import User
from user.models import Profile
from django.core.files.uploadedfile import SimpleUploadedFile
from blog.models import Blog,BlogCategory,BlogView,Comment


def test_create_ctg():
    category = BlogCategory.objects.create(
        name="Kiyim",
        is_main=True,
        slug="Kiyim"
    )
    assert category.name == "Kiyim"
    assert category.is_main is True
    assert category.slug == "Kiyim"
    assert category.parent is None



def test_create_blog():
    user = User.objects.create(username="Karamatillo", password="password")
    image = SimpleUploadedFile(name='test_image.jpg', content=b'some_image_data_here', content_type='image/jpeg')
    profile = Profile.objects.create(user=user,firstname="Karamatillo",last_name="Mahmudjanov",phone_number="+998909009090",image=image)
    category = BlogCategory.objects.create(name="Elektronikaa",is_main=True,slug="elektronika")

    blog = Blog.objects.create(
        author=profile,
        title="asdfghjkl",
        description="qwertyuiopasdfghjkzxcvbnmmnbvcxzsdfgh",
        category=category,
        image=image
        )

    assert blog.author == profile
    assert blog.title == "asdfghjkl"
    assert blog.description == "qwertyuiopasdfghjkzxcvbnmmnbvcxzsdfgh"
    assert blog.category == category
    assert blog.image.name.startswith('blog_images/test_image')
    assert blog.image.name.endswith('.jpg')
    assert blog.image.size == len(b'some_image_data_here')
    assert blog.image.field.name == 'image'
    assert blog.created_at is not None



def test_comment_model():
    user = User.objects.create(username="Karamatillo", password="password")
    image = SimpleUploadedFile(name='test_image.jpg', content=b'some_image_data_here', content_type='image/jpeg')
    profile = Profile.objects.create(user=user,firstname="Karamatillo",last_name="Mahmudjanov",phone_number="+998909009090",image=image)
    category = BlogCategory.objects.create(name="Elektronikaa",is_main=True,slug="elektronika")
    blog = Blog.objects.create(author=profile,title="asdfghjkl",description="qwertyuiopasdfghjkzxcvbnmmnbvcxzsdfgh",category=category,image=image)
    comment = Comment.objects.create(
        blog=blog,
        user=user,
        text="qwertyuioplkjhgfdsazxcvbnm",
    )

    assert comment.blog == blog
    assert comment.user == user
    assert comment.text == "qwertyuioplkjhgfdsazxcvbnm"
    assert comment.created_date is not None



