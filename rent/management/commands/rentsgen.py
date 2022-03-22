from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
from django.db import IntegrityError
import random
from film.models import Film
from person.models import Client
from rent.models import Rent
from utilities.functions import gen_number, gen_dates


class Command(BaseCommand):
    help = 'DB random films-persons-roles generator'

    def handle(self, *args, **kwargs):
        for i in range(10):
            # Django get a random film object
            items_film = list(Film.objects.all())
            film = random.choice(items_film)

            # Django get a random client object
            items_client = list(Client.objects.all())
            client = random.choice(items_client)

            amount = gen_number(1, 9)
            start_date = gen_dates()['start']
            return_date = gen_dates()['end']
            state = 'open'

            try:
                Rent.objects.create(
                    film=film, client=client, amount=amount,
                    start_date=start_date, return_date=return_date,
                    state=state)

                self.stdout.write(f'film: {film} , client:{client}'
                                  f' amount:{amount}, start_date:{start_date},'
                                  f' return_date:{return_date}, state:{state},'
                                  f' Rent created!')
            except IntegrityError:
                self.stdout.write('An error has occurred during the creation '
                                  'of the Rent')
            except ValidationError:
                self.stdout.write('An error has occurred during the creation '
                                  'of the Rent')
