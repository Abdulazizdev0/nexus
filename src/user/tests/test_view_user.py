import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client


@pytest.mark.django_db
def test_user_login():
    user = User.objects.create_user(username='testuser',password='password')
    client = Client()
    response = client.post(reverse('login'),{'username':'testuser','password':'password'})

    assert  response.status_code == 302
    assert  response.url == reverse('main')




