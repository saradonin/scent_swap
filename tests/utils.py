from random import sample

from django.contrib.auth.models import User
from faker import Faker

from common.utils import get_random_brand, get_random_concentration, get_random_year, get_random_category
from scent_app.models import Category, Brand, Perfumer, Note, Perfume, CONCENTRATIONS

faker = Faker(["en_GB", "it_IT", "fr_FR"])


def create_test_user():
    test_user = User.objects.create_user(
        username=faker.first_name(),
        email=faker.ascii_free_email(),
        password="test_password"
    )
    return test_user


def create_test_superuser():
    test_superuser = User.objects.create_superuser(
        username=faker.first_name(),
        email=faker.ascii_free_email(),
        password="test_password",
        is_superuser=True
    )
    return test_superuser


def create_categories():
    category_list = ['Citrus', 'Floral', 'Fresh', 'Fruity', 'Spicy']
    for category in category_list:
        Category.objects.create(name=category)


def create_fake_brand():
    Brand.objects.create(name=faker.name(), description=faker.address())


def create_fake_perfumer():
    perfumer = Perfumer.objects.create(first_name=faker.first_name(), last_name=faker.last_name())
    return perfumer


def random_notes():

    notes = list(Note.objects.all())
    return sample(notes, 3)


def create_random_perfume():
    brand = get_random_brand()
    name = faker.city()
    concentration = get_random_concentration()
    year = get_random_year()
    perfumer = create_fake_perfumer()
    category = get_random_category()

    perfume = Perfume.objects.create(brand=brand, name=name, concentration=concentration, year=year)

    perfume.perfumer.add(perfumer)
    perfume.category.add(category)
    perfume.save()
    return perfume
