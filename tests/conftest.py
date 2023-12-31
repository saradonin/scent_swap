import pytest
from django.contrib.auth.models import User
from django.test import Client

from scent_app.models import Perfume, Brand, Perfumer, Note, Category, UserPerfume, SwapOffer
from tests.utils import create_test_user, create_categories, create_fake_brand, create_fake_perfumer, \
    create_random_perfume, create_test_superuser, create_notes, create_test_messages


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
def set_up(user_logged_in):
    create_test_superuser()
    for _ in range(3):
        create_test_user()

    create_test_messages()
    create_notes()
    create_categories()

    for _ in range(5):
        create_fake_brand()
        create_fake_perfumer()
    for _ in range(10):
        create_random_perfume()


@pytest.fixture
def new_perfume_data():
    return {
        "name": "Perfume Name",
        "brand": Brand.objects.first().id,
        "concentration": 'Eau de Toilette',
        "year": 1999,
        "perfumer": Perfumer.objects.first().id,
        "top_notes": Note.objects.order_by('?').first().id,
        "middle_notes": Note.objects.order_by('?').first().id,
        "base_notes": Note.objects.order_by('?').first().id,
        "category": Category.objects.first().id
    }


@pytest.fixture
def new_userperfume_data(user_logged_in):
    perfume = Perfume.objects.order_by('?').first()

    return {
        "user": user_logged_in,
        "perfume": perfume,
        "volume": 50,
        "status": "full",
        "to_exchange": False
    }


@pytest.fixture
def new_offer(user_logged_in, new_userperfume_data):
    user = user_logged_in
    UserPerfume.objects.create(**new_userperfume_data)
    userperfume = UserPerfume.objects.filter(user=user).first()
    # create offer - objects when creating directly
    offer_data = {
        "offering_perfume": userperfume,
        "requested_perfume": Perfume.objects.order_by('?').first(),
    }
    offer = SwapOffer.objects.create(**offer_data)
    return offer
