from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django.utils.crypto import get_random_string

from film.models import Category


class Command(BaseCommand):
    help = 'DB random categories generator'

    def handle(self, *args, **kwargs):
        for i in range(10):
            name = get_random_string(15)
            description = get_random_string(15)

            try:
                Category.objects.create(name=name, description=description)

                self.stdout.write(f'name: {name}  description:({description}) '
                                  f'category created!')
            except IntegrityError:
                self.stdout.write('An error has occurred during the creation '
                                  'of the category')
