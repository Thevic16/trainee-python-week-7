from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django.utils.crypto import get_random_string

from account.models import MyUser


class Command(BaseCommand):
    help = 'DB random account generator'

    def add_arguments(self, parser):
        parser.add_argument('-a', '--admin', action='store_true',
                            help='Define an admin account')
        parser.add_argument('-e', '--employee', action='store_true',
                            help='Define an employee account')

    def handle(self, *args, **kwargs):
        admin = kwargs['admin']
        employee = kwargs['employee']

        for i in range(10):
            email = get_random_string(15)
            password = get_random_string(15)

            try:
                if admin:
                    MyUser.objects.create_superuser(
                        email=f'{email}@filmrentalsystem.com',
                        password=password)
                elif employee:
                    MyUser.objects.create_user_employee(
                        email=f'{email}@filmrentalsystem.com',
                        password=password)
                else:
                    MyUser.objects.create_user(
                        email=f'{email}@filmrentalsystem.com',
                        password=password)

                self.stdout.write(f'Email: {email}  password:({password}) '
                                  f'account created!')
            except IntegrityError:
                self.stdout.write('An error has occurred during the creation '
                                  'of the account')
