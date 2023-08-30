import random
import string

from common.utils import get_random_brand, get_random_concentration, get_random_perfumer, get_random_year, \
    get_random_category, get_random_note
from scent_app.models import Brand, Note, Perfumer, Category, CONCENTRATIONS, Perfume


def generate_random_name(brand):
    random_name = "Perfume " + brand.name[0:2].upper() + "-" + (str(random.randint(1, 999))) + random.choice(
        string.ascii_letters)
    return random_name


def generate_random_perfume():
    brand = get_random_brand()
    name = generate_random_name(brand)
    concentration = get_random_concentration()
    perfumer = get_random_perfumer()
    year = get_random_year()

    perfume = Perfume.objects.create(name=name, brand=brand, concentration=concentration, year=year)
    perfume.save()

    perfume.perfumer.add(perfumer)

    for i in range(random.randint(1, 3)):
        category = get_random_category()
        perfume.category.add(category)

    for i in range(random.randint(1, 7)):
        note = get_random_note()
        perfume.top_notes.add(note)

    for i in range(random.randint(1, 7)):
        note = get_random_note()
        perfume.middle_notes.add(note)

    for i in range(random.randint(1, 7)):
        note = get_random_note()
        perfume.base_notes.add(note)


def delete_perfumes():
    Perfume.objects.all().delete()
