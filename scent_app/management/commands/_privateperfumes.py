import random
import string
from faker import Faker

from scent_app.models import Brand, Note, Perfumer, Category, CONCENTRATIONS, Perfume, User

faker = Faker(["en_GB", "it_IT", "fr_FR"])

CATEGORY_LIST = ['Citrus', 'Floral', 'Fresh', 'Fruity',
                 'Green', 'Oriental', 'Smoky', 'Spicy', 'Sweet', 'Woody']


def create_categories():
    for category in CATEGORY_LIST:
        if not Category.objects.filter(name=category).exists():
            Category.objects.create(name=category)


def create_perfumer():
    Perfumer.objects.create(first_name=faker.first_name(),
                            last_name=faker.last_name())


def create_brand():
    Brand.objects.create(name=faker.name(), description=faker.address())


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

    perfume = Perfume.objects.create(
        name=name, brand=brand, concentration=concentration, year=year)
    perfume.save()

    perfume.perfumer.add(perfumer)

    for _ in range(random.randint(1, 3)):
        category = Category.objects.order_by('?')[0]
        perfume.category.add(category)

    for _ in range(random.randint(1, 7)):
        note = Note.objects.order_by('?')[0]
        perfume.top_notes.add(note)

    for _ in range(random.randint(1, 7)):
        note = Note.objects.order_by('?')[0]
        perfume.middle_notes.add(note)

    for _ in range(random.randint(1, 7)):
        note = Note.objects.order_by('?')[0]
        perfume.base_notes.add(note)
        
def create_users():
    User.objects.create_superuser(username='admin', email='admin@scentswap.com', password='admin')
    for i in range(2):
        username = f"user{i+1}"
        email = f"user{i+1}@scentswap.com"
        User.objects.create_user(username=username, email=email, password='password123')
    
