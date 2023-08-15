import random
import string

from scent_app.models import Brand, Note, Perfumer, Category, CONCENTRATIONS, Perfume


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


def generate_random_name():
    random_name = "Perfume " + random.choice(string.ascii_letters) + (str(random.randint(1, 999999)))
    return random_name


def generate_random_perfume():
    name = generate_random_name()
    brand = get_random_brand()
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