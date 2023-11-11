from django.core.management.base import BaseCommand

from scent_app.models import Category, Note, Perfumer, Brand, Perfume
from ._privatenotes import create_notes
from ._privateperfumes import generate_random_perfume, create_perfumer, create_brand, create_categories


class Command(BaseCommand):
    help = 'Add perfumes'

    def handle(self, *args, **options):
        if not Category.objects.exists():
            create_categories()
            self.stdout.write(self.style.SUCCESS("Categories created"))
            
        if not Note.objects.exists():
            create_notes()
            self.stdout.write(self.style.SUCCESS("Notes added"))
            
        if not Perfumer.objects.exists():
            for _ in range(50):
                create_perfumer()
            self.stdout.write(self.style.SUCCESS("Fake perfumers added"))

        if not Brand.objects.exists():
            for _ in range(50):
                create_brand()
            self.stdout.write(self.style.SUCCESS("Fake brands added"))

        if not Perfume.objects.exists():
            for _ in range(100):
                generate_random_perfume()
            self.stdout.write(self.style.SUCCESS("Random fake perfumes added"))
