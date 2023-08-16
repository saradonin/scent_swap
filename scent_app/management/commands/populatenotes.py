from django.core.management.base import BaseCommand
from ._privatenotes import create_notes, delete_notes


class Command(BaseCommand):
    help = 'Add notes'

    def handle(self, *args, **options):
        # delete_notes()
        create_notes()
        self.stdout.write(self.style.SUCCESS("Notes added"))
