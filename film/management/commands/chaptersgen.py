from random import choice
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django.utils.crypto import get_random_string
from film.models import Chapter, Season


class Command(BaseCommand):
    help = 'DB random chapters generator'

    def handle(self, *args, **kwargs):
        for i in range(10):
            # Django get a random category object
            items_season = list(Season.objects.all())
            season = choice(items_season)
            title = get_random_string(15)

            try:
                Chapter.objects.create(season=season,
                                       title=title)

                self.stdout.write(f'season: {season} , title:{title}'
                                  f' chapter created!')
            except IntegrityError:
                self.stdout.write('An error has occurred during the creation '
                                  'of the chapter')
