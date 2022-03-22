from datetime import date

from django.core.exceptions import ValidationError
from django.test import TestCase
from unittest.mock import patch

from film.business_logic import FilmBusinessLogic

from film.validations import (validator_date_limit_today,
                              validator_date_limit_future,
                              validator_no_negative)


def fake_today():
    return date(year=2020, month=1, day=1)


# Create your tests here.
class FilmAppTestCase(TestCase):

    def setUp(self):
        self.previous_date = date(year=2019, month=12, day=1)
        self.later_date = date(year=2020, month=1, day=2)
        self.positive_number = 5
        self.negative_number = -5

    @patch("film.validations.date")
    def test_validator_date_limit_today(self, mock_today):
        # Set mock
        mock_today.today.return_value = fake_today()

        self.assertEqual(self.previous_date, validator_date_limit_today(
            self.previous_date))

        with self.assertRaises(ValidationError):
            validator_date_limit_today(self.later_date)

    @patch("film.validations.date")
    def test_validator_date_limit_future(self, mock_today):
        # Set mock
        mock_today.today.return_value = fake_today()

        self.assertEqual(self.later_date, validator_date_limit_future(
            self.later_date))

        with self.assertRaises(ValidationError):
            validator_date_limit_future(self.previous_date)

    def test_validator_no_negative(self):
        self.assertEqual(self.positive_number,
                         validator_no_negative(self.positive_number))

        with self.assertRaises(ValidationError):
            validator_no_negative(self.negative_number)

    def test_validate_stock_greater_availability(self):
        with self.assertRaises(ValidationError):
            stock = 5
            availability = 10
            FilmBusinessLogic.validate_stock_greater_availability(
                stock, availability)

    def test_validate_film_type_equal_prequel_film_type(self):
        with self.assertRaises(ValidationError):
            film_type = 'movie'
            prequel_film_type = 'serie'
            FilmBusinessLogic.validate_film_type_equal_prequel_film_type(
                film_type, prequel_film_type)
