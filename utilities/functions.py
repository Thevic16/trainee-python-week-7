from datetime import datetime, timedelta
from random import randint, uniform


def gen_dates():
    start = datetime.now()
    random_amount_days = randint(1, 15)
    end = start
    end += timedelta(days=random_amount_days)

    return {'start': start.today(), 'end': end.today()}


def gen_random_int():
    return randint(0, 100)


def gen_random_float():
    return uniform(0, 1) * 100


def gen_random_film_type():
    random_number = randint(0, 100)

    if random_number < 50:
        return 'movie'
    else:
        return 'serie'
