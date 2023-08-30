from random import sample

from django.contrib.auth.models import User
from faker import Faker

from common.utils import get_random_brand, get_random_concentration, get_random_year, get_random_category
from scent_app.models import Category, Brand, Perfumer, Note, Perfume, CONCENTRATIONS

faker = Faker(["en_EN", "it_IT", "fr_FR"])


def create_test_user():
    test_user = User.objects.create_user(
        username=faker.first_name(),
        email=faker.ascii_free_email(),
        password="haslo123"
    )
    return test_user


def create_categories():
    category_list = ['Citrus', 'Floral', 'Fresh', 'Fruity', 'Spicy']
    for category in category_list:
        Category.objects.create(name=category)


def create_fake_brand():
    Brand.objects.create(name=faker.name(), description=faker.address())


def create_fake_perfumer():
    Perfumer.objects.create(first_name=faker.first_name(), last_name=faker.last_name())


def random_notes():
    notes = list(Note.objects.all())
    return sample(notes, 3)


def create_random_perfume():
    perfume = Perfume.objects.create(
        brand=get_random_brand(),
        name=faker.texts(nb_texts=2, max_nb_chars=20),
        concentration=get_random_concentration(),
        year=get_random_year()
    )
    perfume.save()

    perfume.perfumer.add(create_fake_perfumer())
    perfume.category.add(get_random_category())
    perfume.top_notes.add(random_notes())
    perfume.middle_notes.add(random_notes())
    perfume.base_notes.add(random_notes())
