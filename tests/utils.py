import random

from django.contrib.auth.models import User
from faker import Faker

from scent_app.models import Category, Brand, Perfumer, Note, Perfume, CONCENTRATIONS, Message

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


def create_notes():
    note_list = ['Amber', 'Cedar', 'Iris', 'Lime', 'Pepper']
    for note in note_list:
        Note.objects.create(name=note)


def create_random_perfume():
    brand = Brand.objects.order_by('?')[0]
    name = faker.city()
    concentration = random.choice(CONCENTRATIONS)[0]
    year = random.randint(1960, 2023)
    perfumer = create_fake_perfumer()
    category = Category.objects.order_by('?')[0]

    perfume = Perfume.objects.create(brand=brand, name=name, concentration=concentration, year=year)

    perfume.perfumer.add(perfumer)
    perfume.category.add(category)
    perfume.save()
    return perfume


def create_test_messages():
    users = User.objects.all()

    for user in users:
        other_user = None
        while other_user is None or other_user == user:
            other_user = User.objects.order_by('?').first()
        Message.objects.create(sender=user, receiver=other_user, content=f"test content from {user.id} to {other_user.id}")