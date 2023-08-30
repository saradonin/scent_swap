import pytest

from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_get_brand_list():
    client = Client()
    response = client.get(reverse("perfume-list"))
    assert response.status_code == 200

