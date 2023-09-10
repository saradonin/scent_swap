import pytest
from django.shortcuts import resolve_url

from django.test import Client
from django.urls import reverse

from scent_app.models import Perfume, Brand, UserPerfume


@pytest.mark.django_db
def test_get_index_page():
    client = Client()
    response = client.get(reverse("index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_brand_list_not_logged():
    client = Client()
    response = client.get(reverse("brand-list"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_brand_details_not_logged(set_up):
    client = Client()
    brand = Brand.objects.first()
    # response = client.get(reverse("brand-perfumes", args=(brand.id,)))
    response = client.get(resolve_url("brand-perfumes", brand.id))
    assert response.status_code == 200


@pytest.mark.django_db
def test_brand_add_logged(user_logged_in, set_up):
    new_brand = {
        "name": "Test Brand Name",
        "description": "Test description"
    }
    response = user_logged_in.client.post(reverse("brand-add"), new_brand)
    assert response.status_code == 403


@pytest.mark.django_db
def test_brand_add_logged_superuser(superuser_logged_in, set_up):
    brand_count = Brand.objects.count()
    new_brand = {
        "name": "Test Brand Name",
        "description": "Test description"
    }
    response = superuser_logged_in.client.post(reverse("brand-add"), new_brand)
    assert response.status_code == 302
    assert Brand.objects.count() == brand_count + 1
    assert Brand.objects.filter(name=new_brand["name"]).exists()


@pytest.mark.django_db
def test_brand_update_logged_superuser(superuser_logged_in, set_up):
    brand = Brand.objects.first()

    # get update page
    response = superuser_logged_in.client.get(reverse("brand-update", args=(brand.id,)))
    assert response.status_code == 200

    # update brand data
    updated_brand_data = {
        "name": "New Brand Name",
        "description": "New updated description"
    }
    response = superuser_logged_in.client.post(reverse("brand-update", args=(brand.id,)), updated_brand_data)
    assert response.status_code == 302

    # check if updated
    updated_brand = Brand.objects.get(id=brand.id)
    assert updated_brand.name == updated_brand_data["name"]


@pytest.mark.django_db
def test_get_perfume_list():
    client = Client()
    response = client.get(reverse("perfume-list"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_collection_list(user_logged_in):
    user = user_logged_in
    response = user.client.get(resolve_url("userperfume-list", user.id))
    assert response.status_code == 200


@pytest.mark.django_db
def test_collection_add_logged(user_logged_in, set_up):
    collection_count = UserPerfume.objects.count()
    perfume = Perfume.objects.first()

    new_userperfume = {
        "user": user_logged_in,
        "perfume": perfume,
        "volume": 50,
        "status": "full",
        "to_exchange": False
    }
    response = user_logged_in.client.post(reverse("userperfume-add", args=(perfume.id,)), new_userperfume)

    assert response.status_code == 302
    assert UserPerfume.objects.count() == collection_count + 1

    assert UserPerfume.objects.filter(perfume=new_userperfume["perfume"]).exists()


@pytest.mark.django_db
def test_get_user_list_not_logged():
    client = Client()
    response = client.get(reverse("user-list"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_user_list_logged(user_logged_in):
    response = user_logged_in.client.get(reverse("user-list"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_offer_list_not_logged():
    client = Client()
    response = client.get(reverse("offer-list"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_get_offer_list_logged(user_logged_in):
    response = user_logged_in.client.get(reverse("offer-list"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_offer_list_logged_superuser(superuser_logged_in):
    response = superuser_logged_in.client.get(reverse("offer-list"))
    assert response.status_code == 200
