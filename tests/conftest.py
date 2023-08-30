import pytest
from django.contrib.auth.models import User
from django.test import Client

from tests.utils import create_test_user, create_categories, create_fake_brand, create_fake_perfumer, \
    create_random_perfume


@pytest.fixture
def create_test_superuser():
    test_superuser = User.objects.create_superuser(
        username="test_superuser",
        email="super_email@django.com",
        password="haslo123",
        is_superuser=True)
    return test_superuser


@pytest.fixture
def user_logged_in():
    User.objects.create_user(username='testuser', password='testpassword')
    client = Client()
    client.login(username='testuser', password='testpassword')
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
