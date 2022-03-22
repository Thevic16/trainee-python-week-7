from random import choice

from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django.utils.crypto import get_random_string


from person.models import Person, Client
from utilities.functions import gen_phone


class Command(BaseCommand):
    help = 'DB random persons generator'

    def handle(self, *args, **kwargs):
        for i in range(10):
            # Django get a random person object
            items_person = list(Person.objects.all())
            person = choice(items_person)
            direction = get_random_string(15)
            phone = gen_phone()
            email = get_random_string(15)

            try:
                Client.objects.create(
                    person=person, direction=direction, phone=phone,
                    email=f'{email}@filmrentalsystem.com')

                self.stdout.write(f'person: {person} , direction:{direction}'
                                  f' phone:{phone}, email:{email} '
                                  f' client created!')
            except IntegrityError:
                self.stdout.write('An error has occurred during the creation '
                                  'of the client')
