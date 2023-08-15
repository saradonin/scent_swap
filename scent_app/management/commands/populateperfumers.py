from django.core.management.base import BaseCommand

from scent_app.management.commands._privateperfumers import create_perfumers


class Command(BaseCommand):
    help = 'Add perfumers'

    def handle(self, *args, **options):
        create_perfumers()
        self.stdout.write(self.style.SUCCESS("Some of the most popular perfumers added"))