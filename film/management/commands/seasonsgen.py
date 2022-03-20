from random import choice

from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django.utils.crypto import get_random_string
from film.models import Film, Season


class Command(BaseCommand):
    help = 'DB random seasons generator'

    def handle(self, *args, **kwargs):
        for i in range(10):
            # Django get a random category object
            items_film = list(Film.objects.all())
            film = choice(items_film)
            title = get_random_string(15)

            try:
                Season.objects.create(film=film,
                                      title=title)

                self.stdout.write(f'film: {film} , title:{title}'
                                  f' season created!')
            except IntegrityError:
                self.stdout.write('An error has occurred during the creation '
                                  'of the season')
