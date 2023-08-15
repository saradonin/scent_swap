from django.core.management.base import BaseCommand

from scent_app.management.commands._privateperfumes import generate_random_perfume


class Command(BaseCommand):
    help = 'Add perfumes'

    def handle(self, *args, **options):
        for _ in range(200):
            generate_random_perfume()
        self.stdout.write(self.style.SUCCESS("Random fake perfumes added"))
