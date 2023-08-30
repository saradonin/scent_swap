import pytest
from django.contrib.auth.models import User


@pytest.fixture
def create_test_user():
    test_user = User.objects.create_user(username="test_user1", email="test_email1@django.com", password="haslo123")
    return test_user
