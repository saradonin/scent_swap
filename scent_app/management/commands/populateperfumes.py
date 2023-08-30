from django.core.management.base import BaseCommand
from ._privatecategory import create_categories
from ._privatenotes import create_notes, delete_notes
from ._privateperfumers import create_perfumers
from ._privatebrands import create_brands, delete_brands
from ._privateperfumes import generate_random_perfume, delete_perfumes


class Command(BaseCommand):
    help = 'Add perfumes'

    def handle(self, *args, **options):
        create_categories()
        self.stdout.write(self.style.SUCCESS("Categories created"))
        create_notes()
        self.stdout.write(self.style.SUCCESS("Notes added"))
        create_perfumers()
        self.stdout.write(self.style.SUCCESS("Popular perfumers added"))
        create_brands()
        self.stdout.write(self.style.SUCCESS("Popular brands added"))

        for _ in range(500):
            generate_random_perfume()
        self.stdout.write(self.style.SUCCESS("Random fake perfumes added"))
