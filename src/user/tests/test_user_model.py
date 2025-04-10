import pytest
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from user.models import Profile

def test_create_profile():
    user = User.objects.create(username="Rahmatillo", password="password")
    image = SimpleUploadedFile(name='test_image.jpg', content=b'some_image_data_here', content_type='image/jpeg')

    profile = Profile.objects.create(
        user=user,
        firstname="Rahmatillo",
        last_name="Yunusov",
        phone_number="+998888008080",
        image=image
    )

    assert profile.user == user
    assert profile.firstname == 'Rahmatillo'
    assert profile.last_name == 'Yunusov'
    assert profile.phone_number == '+998888008080'
    assert profile.image.name.startswith('test_image')
    assert profile.image.name.endswith('.jpg')
    assert profile.image.size == len(b'some_image_data_here')
    assert profile.image.field.name == 'image'