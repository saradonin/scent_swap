import random

from scent_app.models import Brand, Note, Perfumer, Category, CONCENTRATIONS


def get_random_brand():
    random_brand = Brand.objects.order_by('?')[0]
    return random_brand


def get_random_concentration():
    random_concentration = random.choice(CONCENTRATIONS)
    return random_concentration[0]


def get_random_note():
    random_note = Note.objects.order_by('?')[0]
    return random_note


def get_random_perfumer():
    random_perfumer = Perfumer.objects.order_by('?')[0]
    return random_perfumer


def get_random_category():
    random_category = Category.objects.order_by('?')[0]
    return random_category


def get_random_year():
    random_year = random.randint(1960, 2023)
    return random_year
