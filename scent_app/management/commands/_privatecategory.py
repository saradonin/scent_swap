from scent_app.models import Category

CATEGORY_LIST = ['Citrus', 'Floral', 'Fresh', 'Fruity', 'Green', 'Oriental', 'Smoky', 'Spicy', 'Sweet', 'Woody']


def create_categories():
    for category in CATEGORY_LIST:
        if not Category.objects.filter(name=category).exists():
            Category.objects.create(name=category)
