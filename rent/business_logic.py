from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from film.models import Film
from utilities.logger import Logger

amount_day_max_limit = 15


class RentBusinessLogic:
    """
    The class contains all the business logic of the rent app
    """

    # Methods about validate date
    @classmethod
    def validate_date_gt_max_limit(cls, date1: date, date2: date, field: str):
        """
        Validate that the difference between both dates is not greater than max
         limit.

        Args:
            date1 (date): Input date1
            date2 (date): Input date2
            field (str): Indicate the field to report the ValidationError
        Raises:
            ValidationError: This return date has to be before the max limit
        """
        if cls.get_date_diff_in_days(date1, date2) > amount_day_max_limit:
            raise ValidationError(
                {field: _(f'This return date has to be before'
                          f' {amount_day_max_limit} days from the start date')
                 })

    @staticmethod
    def validate_date1_gr_or_eq_date2(date1: date, date2: date, field: str):
        """
        Validate that date2 is not greater or equal than date2

        Args:
            date1 (date): Input date1
            date2 (date): Input date2
            field (str): Indicate the field to report the ValidationError
        Raises:
            ValidationError: date2 has to be after the date1
        """
        if date1 is not None:
            if date2 >= date1:
                raise ValidationError(
                    {field: _('This date has to be'
                              ' after the start date')
                     })

    @staticmethod
    def validate_date1_eq_or_low_date2(date1: date, date2: date, field: str):
        """
        Validate that date1 is not lower or equal than date2

        Args:
            date1 (date): Input date1
            date2 (date): Input date2
            field (str): Indicate the field to report the ValidationError

        Raises:
            ValidationError: date1 has to be after the date2
        """
        if date1 <= date2:
            raise ValidationError(
                {field: _('This date has to be'
                          ' after the start date')
                 })

    @staticmethod
    def validate_amount_availability(amount: int, film: Film):
        """
        Validate that amount that the client is requesting is available

        Args:
            amount (date): Input date1
            film (date): Input date2

        Raises:
            ValidationError: The amount of film(s) that you are adding exceed
             the availability
        """
        film.availability -= amount

        if film.availability < 0:
            raise ValidationError(
                {'amount': _("The amount of film(s) that you are adding"
                             " exceed the availability"
                             f" ({film.availability})")})
        else:
            film.save()

    @classmethod
    def validate_amount_update(cls, current_amount: int, film: Film,
                               pre_save_rent):
        """
        Validate that the amount update process is it being executed correctly

        Args:
            current_amount (int): Amount of film to rent
            film (Film): Film to rent
            pre_save_rent (Rent): Pre save rent

        Raises:
            ValidationError: The film can't be change
        """

        # Film hasn't been change
        if pre_save_rent.film.id == film.id:
            cls.validate_amount_availability(
                (current_amount - pre_save_rent.amount), film)

        # The film have change
        else:
            raise ValidationError({'film': _("Once the film is saved"
                                             " it cannot be modified."
                                             " For this you have to create"
                                             " a new order.")})

    # Methods about obtain cost
    # I need to test this method, because is not working as expected
    @classmethod
    def get_rent_cost(cls, amount_film: int, star_date: date,
                      return_date: date, actual_return_date: date,
                      film_price_by_day: float):
        """
        Get the cost of renting the film

        Args:
            amount_film (int): Amount of film to rent
            star_date (date): Star date of the rent
            return_date (date): Return date of the rent
            actual_return_date (date): Actual return date of the rent
            film_price_by_day (float): The price by day of renting the film
        Return:
            cost (float): the cost of renting the film
            message (str): N.A, abbreviation for not applicable or not
            available
        """
        if actual_return_date is None:
            amount_days = cls.get_date_diff_in_days(return_date, star_date)
            cost = cls.get_theoretical_cost(amount_film, amount_days,
                                            film_price_by_day)

        else:
            cost = cls.get_actual_cost(amount_film, star_date, return_date,
                                       actual_return_date, film_price_by_day)

        if cost > 0:
            return cost

        Logger.debug(f"amount_film: {amount_film}")
        Logger.debug(f"star_date: {star_date}")
        Logger.debug(f"return_date: {return_date}")
        Logger.debug(f"actual_return_date: {actual_return_date}")
        Logger.debug(f"film_price_by_day: {film_price_by_day}")
        return 'N.A'

    @staticmethod
    def get_date_diff_in_days(date1: date, date2: date) -> int:
        """
        Get the difference in days between both dates

        Args:
            date1 (date): Input date1
            date2 (date): Input date1

        Return:
            days (int): amount of days of difference between the dates
        """
        date_difference = date1 - date2
        return date_difference.days

    @staticmethod
    def get_theoretical_cost(amount_film: int, amount_days: int,
                             film_price_by_day: float) -> float:
        """
        Get the theoretical cost without considering extra penalty costs

        Args:
            amount_film (int): Amount of films to rent
            amount_days (int): Theoretical amount of days to rent
            film_price_by_day (float): The price by day of renting the film

        Return:
            cost (float): the theoretical cost of renting the film
        """
        Logger.debug(f"amount_film: {amount_film}")
        Logger.debug(f"amount_days: {amount_days}")
        Logger.debug(f"film_price_by_day: {film_price_by_day}")
        cost = amount_film * amount_days * film_price_by_day
        Logger.debug(f"get_theoretical_cost: {cost}")
        return cost

    @staticmethod
    def get_extra_cost(amount_film: int, extra_days: int,
                       film_price_by_day: float) -> float:
        """
        Get the extra cost that means penalty costs for extra days

        Args:
            amount_film (int): Amount of films to rent
            extra_days (int):  Amount of extra days to rent
            film_price_by_day (float): The price by day of renting the film

        Return:
            cost (float): the extra cost of renting the film
        """
        Logger.debug(f"amount_film: {amount_film}")
        Logger.debug(f"film_price_by_day: {film_price_by_day}")
        Logger.debug(f"extra_days: {extra_days}")
        cost = extra_days * (amount_film * film_price_by_day + extra_days + 1)
        Logger.debug(f"get_extra_cost: {cost}")
        return cost

    @classmethod
    def get_actual_cost(cls, amount_film: int, star_date: date,
                        return_date: date, actual_return_date: date,
                        film_price_by_day: int) -> float:
        amount_days_normal_cost = cls.get_date_diff_in_days(return_date,
                                                            star_date)
        """
        Get the actual cost considering extra penalty costs

        Args:
            amount_film (int): Amount of film to rent
            star_date (date): Star date of the rent
            return_date (date): Return date of the rent
            actual_return_date (date): Actual return date of the rent
            film_price_by_day (float): The price by day of renting the film

        Return:
            cost (float): the actual cost of renting the film
        """

        Logger.debug(f"amount_days_normal_cost: {amount_days_normal_cost}")

        amount_days_actual_cost = cls.get_date_diff_in_days(actual_return_date,
                                                            star_date)

        Logger.debug(f"amount_days_actual_cost: {amount_days_actual_cost}")

        # Deliver before or on return_date
        if actual_return_date <= return_date:
            return cls.get_theoretical_cost(amount_film,
                                            amount_days_actual_cost,
                                            film_price_by_day)

        extra_days = amount_days_actual_cost - amount_days_normal_cost
        theorical_cost = cls.get_theoretical_cost(amount_film,
                                                  amount_days_normal_cost,
                                                  film_price_by_day)

        extra_cost = cls.get_extra_cost(amount_film, extra_days,
                                        film_price_by_day)

        actual_cost = theorical_cost + extra_cost

        Logger.debug(f"get_actual_cost: {actual_cost}")
        return actual_cost

    # Method about validate state
    @staticmethod
    def validate_state_close(state: str, actual_return_date: date):
        """
        Validate if is possible to close the rent base on state and actual
        return date

        Args:
            state (str): State of the rent
            actual_return_date (date):  Actual return date

        Raises:
            ValidationError: To change the state to close actual return date
            has to be different of None
        """
        if state == 'close' and actual_return_date is None:
            raise ValidationError({'state': _('To change the state to close'
                                              ' you have to first enter an'
                                              ' actual return date.')})

    @staticmethod
    def state_close_return_films(state: str, state_presave: str,
                                 amount: int, film: Film):
        """
        If a rent is close put films available to rent again

        Args:
            state (str): State of the rent
            state_presave (str): State of the rent before save
            amount (int):  Amount of film to rent
            film (Film): film to rent
        """
        if state == 'close' and state_presave == 'open':
            film.availability += amount
            Logger.debug(f"film.availability:{film.availability}")
            Logger.debug(f"film.stock:{film.stock}")
            film.save()

    # Methods for permission
    @staticmethod
    def validate_update_permission(state_presave: str):
        """
        If a rent is close put films available to rent again

        Args:
            state_presave (str): State of the rent before save

        Raises:
            ValidationError: You don't have permission to modify an already
             close rent
        """
        if state_presave == 'close':
            raise ValidationError("You don't have permission to modify"
                                  " an already close rent")
