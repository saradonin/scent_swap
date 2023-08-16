from django.core.management.base import BaseCommand
from ._privatebrands import create_brands, delete_brands


class Command(BaseCommand):
    help = 'Add brands'

    def handle(self, *args, **options):
        create_brands()
        self.stdout.write(self.style.SUCCESS("Brands added"))