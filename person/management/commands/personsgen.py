from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django.utils.crypto import get_random_string


from person.models import Person
from utilities.functions import gen_date, gen_person_gender, gen_person_type


class Command(BaseCommand):
    help = 'DB random persons generator'

    def handle(self, *args, **kwargs):
        for i in range(10):
            name = get_random_string(15)
            lastname = get_random_string(15)
            gender = gen_person_gender()
            date_of_birth = gen_date()
            person_type = gen_person_type()

            try:
                Person.objects.create(
                    name=name, lastname=lastname,
                    gender=gender, date_of_birth=date_of_birth,
                    person_type=person_type)

                self.stdout.write(f'name: {name} , lastname:{lastname}'
                                  f' gender:{gender},'
                                  f'gender:{gender}, '
                                  f'date_of_birth:{date_of_birth},'
                                  f'person_type:{person_type},'
                                  f' person created!')
            except IntegrityError:
                self.stdout.write('An error has occurred during the creation '
                                  'of the person')
