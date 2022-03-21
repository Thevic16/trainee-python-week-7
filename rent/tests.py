from django.core.exceptions import ValidationError
from datetime import date
from django.test import TestCase

from film.models import Film, Category
from person.models import Person, Client
from rent.business_logic import RentBusinessLogic
from rent.validations import RentValidation
from rent.models import Rent


class RentAppTestCase(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='comedy')
        self.price_by_day = 10
        self.stock = 10
        self.availability = 8
        self.film1 = Film.objects.create(title='film1',
                                         release_date=date(year=2013, month=9,
                                                           day=12),
                                         category=self.category,
                                         price_by_day=self.price_by_day,
                                         stock=self.stock,
                                         availability=self.availability,
                                         film_type='movie')

        self.film2 = Film.objects.create(title='film2',
                                         release_date=date(year=2013, month=9,
                                                           day=12),
                                         category=self.category,
                                         price_by_day=self.price_by_day,
                                         stock=self.stock,
                                         availability=self.availability,
                                         film_type='movie')

        self.person = Person.objects.create(name='victor', lastname='gomez',
                                            gender='male',
                                            date_of_birth=date(year=2013,
                                                               month=9,
                                                               day=10),
                                            person_type='client')

        self.client = Client.objects.create(person=self.person, direction='RD',
                                            phone='812-5669-0742',
                                            email='test@gmail.com')
        self.amount = 2
        self.start_date = date(year=2050, month=1, day=1)
        self.return_date = date(year=2050, month=1, day=2)
        self.actual_return_date = date(year=2050, month=1, day=5)
        self.state = 'open'

        self.rent1 = Rent.objects.create(film=self.film1, client=self.client,
                                         amount=self.amount,
                                         start_date=self.start_date,
                                         return_date=self.return_date,
                                         state=self.state)

    def test_validate_date_gt_max_limit(self):
        with self.assertRaises(ValidationError):
            date1 = date(year=2022, month=1, day=17)
            date2 = date(year=2022, month=1, day=1)
            RentValidation.validate_date_gt_max_limit(date1, date2, "test")

    def test_validate_date1_gr_or_eq_date2(self):
        with self.assertRaises(ValidationError):
            date1 = date(year=2022, month=1, day=1)
            date2 = date(year=2022, month=1, day=1)
            RentValidation.validate_date1_gr_or_eq_date2(date1, date2,
                                                         "test")

        with self.assertRaises(ValidationError):
            date1 = date(year=2022, month=1, day=1)
            date2 = date(year=2022, month=1, day=2)
            RentValidation.validate_date1_gr_or_eq_date2(date1, date2,
                                                         "test")

    def test_validate_date1_eq_or_low_date2(self):
        with self.assertRaises(ValidationError):
            date1 = date(year=2022, month=1, day=1)
            date2 = date(year=2022, month=1, day=1)
            RentValidation.validate_date1_eq_or_low_date2(date1, date2,
                                                          "test")

            date1 = date(year=2022, month=1, day=1)
            date2 = date(year=2022, month=1, day=2)
            RentValidation.validate_date1_eq_or_low_date2(date1, date2,
                                                          "test")

    def test_validate_amount_update(self):
        with self.assertRaises(ValidationError):
            RentValidation.validate_amount_update(self.amount, self.film2,
                                                  self.rent1)

    def test_get_rent_cost(self):
        cost = 20
        self.assertEqual(cost,
                         RentBusinessLogic.get_rent_cost(self.amount,
                                                         self.start_date,
                                                         self.return_date,
                                                         None,
                                                         self.price_by_day))

    def test_get_actual_cost(self):
        cost = 92
        self.assertEqual(cost,
                         RentBusinessLogic.get_actual_cost
                         (self.amount,
                          self.start_date,
                          self.return_date,
                          self.actual_return_date,
                          self.price_by_day))

    def test_validate_state_close(self):
        with self.assertRaises(ValidationError):
            RentValidation.validate_state_close('close', None)

    def test_state_close_return_films(self):
        amount = 2
        availability = 10
        RentBusinessLogic.state_close_return_films('close', 'open',
                                                   amount, self.film2)
        self.assertEqual(availability, self.film2.availability)

    def test_validate_update_permission(self):
        with self.assertRaises(ValidationError):
            RentValidation.validate_update_permission('close')
