from django.core.management.base import BaseCommand
from django.db import IntegrityError
import random
from film.models import Film
from person.models import Person, Role, FilmPersonRole


class Command(BaseCommand):
    help = 'DB random films-persons-roles generator'

    def handle(self, *args, **kwargs):
        for i in range(10):
            # Django get a random film object
            items_film = list(Film.objects.all())
            film = random.choice(items_film)

            # Django get a random person object
            items_person = list(Person.objects.all())
            person = random.choice(items_person)

            # Django get a random person object
            items_role = list(Role.objects.all())
            role = random.choice(items_role)

            try:
                FilmPersonRole.objects.create(
                    film=film, person=person,
                    role=role)

                self.stdout.write(f'film: {film} , person:{person}'
                                  f' role:{role},'
                                  f' film-person-role created!')
            except IntegrityError:
                self.stdout.write('An error has occurred during the creation '
                                  'of the films-persons-roles')
