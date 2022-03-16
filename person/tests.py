from datetime import date
from django.test import TestCase
from unittest.mock import patch

from person.business_logic import PersonBusinessLogic


def fake_today():
    return date(year=2022, month=3, day=13)


# Create your tests here.
class PersonAppTestCase(TestCase):

    @patch("person.business_logic.date")
    def test_get_age_by_birthday(self, mock_today):
        # Set mock
        mock_today.today.return_value = fake_today()

        age = 22
        self.assertEqual(age, PersonBusinessLogic.get_age_by_birthday(
            date(year=1999, month=3, day=16)))
