from django.core.management.base import BaseCommand

from scent_app.management.commands._privatecategory import create_categories


class Command(BaseCommand):
    help = 'Add categories'

    def handle(self, *args, **options):
        create_categories()
        self.stdout.write(self.style.SUCCESS("Categories added"))
