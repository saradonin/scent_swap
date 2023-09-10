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
def test_brand_add_logged_superuser(superuser_logged_in, set_up):
    brand_count = Brand.objects.count()
    new_brand = {
        "name": "Test Brand Name",
        "description": "Test description"
    }
    response = superuser_logged_in.post(reverse("brand-add"), new_brand)
    assert response.status_code == 302
    assert Brand.objects.count() == brand_count + 1
    assert Brand.objects.filter(name=new_brand["name"]).exists()


@pytest.mark.django_db
def test_brand_update_logged_superuser(superuser_logged_in, set_up):
    brand = Brand.objects.first()

    # get update page
    response = superuser_logged_in.get(reverse("brand-update", args=(brand.id,)))
    assert response.status_code == 200

    # update brand name
    updated_brand_data = {
        "name": "New Brand Name",
        "description": "New updated description"
    }
    response = superuser_logged_in.post(reverse("brand-update", args=(brand.id,)), updated_brand_data)
    assert response.status_code == 302

    # check if updated
    updated_brand = Brand.objects.get(id=brand.id)
    assert updated_brand.name == updated_brand_data["name"]


