import random
import string

from scent_app.models import Brand, Note, Perfumer, Category, CONCENTRATIONS, Perfume


def generate_random_name(brand):
    random_name = "Perfume " + brand.name[0:2].upper() + "-" + (str(random.randint(1, 999))) + random.choice(
        string.ascii_letters)
    return random_name


def generate_random_perfume():
    brand = Brand.objects.order_by('?')[0]
    name = generate_random_name(brand)
    concentration = random.choice(CONCENTRATIONS)[0]
    perfumer = Perfumer.objects.order_by('?')[0]
    year = random.randint(1920, 2023)

    perfume = Perfume.objects.create(name=name, brand=brand, concentration=concentration, year=year)
    perfume.save()

    perfume.perfumer.add(perfumer)

    for i in range(random.randint(1, 3)):
        category = Category.objects.order_by('?')[0]
        perfume.category.add(category)

    for i in range(random.randint(1, 7)):
        note = Note.objects.order_by('?')[0]
        perfume.top_notes.add(note)

    for i in range(random.randint(1, 7)):
        note = Note.objects.order_by('?')[0]
        perfume.middle_notes.add(note)

    for i in range(random.randint(1, 7)):
        note = Note.objects.order_by('?')[0]
        perfume.base_notes.add(note)


def delete_perfumes():
    Perfume.objects.all().delete()
