from django.core.management.base import BaseCommand
from ._privatenotes import create_notes
from ._privateperfumes import generate_random_perfume, create_perfumer, create_brand, create_categories


class Command(BaseCommand):
    help = 'Add perfumes'

    def handle(self, *args, **options):
        create_categories()
        self.stdout.write(self.style.SUCCESS("Categories created"))
        create_notes()
        self.stdout.write(self.style.SUCCESS("Notes added"))

        for _ in range(125):
            create_perfumer()
        self.stdout.write(self.style.SUCCESS("Fake perfumers added"))

        for _ in range(200):
            create_brand()
        self.stdout.write(self.style.SUCCESS("Fake brands added"))

        for _ in range(1000):
            generate_random_perfume()
        self.stdout.write(self.style.SUCCESS("Random fake perfumes added"))
