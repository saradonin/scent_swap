import pytest
from django.contrib.auth.models import User
from django.test import Client

from scent_app.models import Perfume, UserPerfume
from tests.utils import create_test_user, create_categories, create_fake_brand, create_fake_perfumer, \
    create_random_perfume, create_test_superuser, create_notes


@pytest.fixture
def superuser_logged_in():
    test_superuser = User.objects.create_superuser(
        username="test_superuser",
        email="super_email@django.com",
        password="test_password",
        is_superuser=True)
    client = Client()
    client.login(username='test_superuser', password='test_password')
    test_superuser.client = client
    return test_superuser


@pytest.fixture
def user_logged_in():
    user = User.objects.create_user(username='test_user', password='test_password')
    client = Client()
    client.login(username='test_user', password='test_password')
    user.client = client  # Attach the client to the user object
    return user


@pytest.fixture
def set_up():
    create_test_superuser()
    for _ in range(3):
        create_test_user()

    create_notes()
    create_categories()
    for _ in range(5):
        create_fake_brand()
        create_fake_perfumer()
    for _ in range(10):
        create_random_perfume()


@pytest.fixture
def create_userperfume(user_logged_in):
    user = user_logged_in
    perfume = Perfume.objects.first()
    userperfume_data = {
        "user": user,
        "perfume": perfume,
        "volume": 50,
        "status": "full",
        "to_exchange": False
    }
    userperfume = UserPerfume.objects.create(**userperfume_data)
    return userperfume
