import pytest
from django.contrib.auth.models import User
from django.test import Client

from tests.utils import create_test_user, create_categories, create_fake_brand, create_fake_perfumer, \
    create_random_perfume, create_test_superuser


@pytest.fixture
def superuser_logged_in():
    test_superuser = User.objects.create_superuser(
        username="test_superuser",
        email="super_email@django.com",
        password="admin_password",
        is_superuser=True)
    client = Client()
    client.login(username='test_superuser', password='admin_password')
    return client


@pytest.fixture
def user_logged_in():
    User.objects.create_user(username='test_user', password='test_password')
    client = Client()
    client.login(username='test_user', password='test_password')
    return client


@pytest.fixture
def set_up():
    create_test_superuser()
    for _ in range(3):
        create_test_user()

    create_categories()
    for _ in range(5):
        create_fake_brand()
        create_fake_perfumer()
    for _ in range(10):
        create_random_perfume()
