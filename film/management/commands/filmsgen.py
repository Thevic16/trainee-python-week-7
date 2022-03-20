from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django.utils.crypto import get_random_string
import random

from film.models import Category, Film
from utilities.functions import gen_random_float, gen_random_int, \
    gen_random_film_type, gen_date


class Command(BaseCommand):
    help = 'DB random films generator'

    def handle(self, *args, **kwargs):
        for i in range(10):
            title = get_random_string(15)
            description = get_random_string(15)
            release_date = gen_date()
            # Django get a random category object
            items_category = list(Category.objects.all())
            category = random.choice(items_category)

            price_by_day = gen_random_float()
            stock = gen_random_int()
            availability = stock
            film_type = gen_random_film_type()

            try:
                Film.objects.create(
                    title=title, description=description,
                    release_date=release_date, category=category,
                    price_by_day=price_by_day, stock=stock,
                    availability=availability, film_type=film_type)

                self.stdout.write(f'title: {title} , description:{description}'
                                  f' release_date:{release_date},'
                                  f'category:{category}, '
                                  f'price_by_day:{price_by_day},'
                                  f'stock:{stock},'
                                  f'availability:{availability},'
                                  f'film_type:{film_type},'
                                  f' film created!')
            except IntegrityError:
                self.stdout.write('An error has occurred during the creation '
                                  'of the film')
