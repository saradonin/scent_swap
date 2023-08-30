import pytest

from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_get_index_page():
    client = Client()
    response = client.get(reverse("index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_brand_list():
    client = Client()
    response = client.get(reverse("brand-list"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_perfume_list():
    client = Client()
    response = client.get(reverse("perfume-list"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_user_list_not_logged():
    client = Client()
    response = client.get(reverse("user-list"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_user_list_logged(user_logged_in):
    response = user_logged_in.get(reverse("user-list"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_offer_list_not_logged():
    client = Client()
    response = client.get(reverse("offer-list"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_offer_list_logged(user_logged_in):
    response = user_logged_in.get(reverse("offer-list"))
    assert response.status_code == 200
