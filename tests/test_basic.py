import pytest

from django.test import Client
from django.urls import reverse

from scent_app.models import Perfume, Brand


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


@pytest.mark.django_db
def test_get_offer_list_logged_superuser(superuser_logged_in):
    response = superuser_logged_in.get(reverse("offer-list"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_brand_add_logged_superuser(superuser_logged_in):
    brand_count = Brand.objects.count()
    new_brand = {
        "name": "Test Brand Name",
        "description": "Test description"
    }
    response = superuser_logged_in.post(reverse("brand-add"), new_brand)
    assert response.status_code == 302
    assert Brand.objects.count() == brand_count + 1
    assert Brand.objects.filter(name=new_brand["name"]).exists()


