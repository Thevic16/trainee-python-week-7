from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validator_date_limit_today(input_date: date) -> date:
    """
    Validate that the input date is not in the future

    Args:
        input_date (date): Input date

    Raises:
        ValidationError: The inserted date has not happened yet

    Return:
        input_date (date): Input date
    """
    if input_date > date.today():
        raise ValidationError("The inserted date has not happened yet")

    return input_date


def validator_date_limit_future(input_date: date) -> date:
    """
    Validate that the input date is  in the future

    Args:
        input_date (date): Input date

    Raises:
        ValidationError: The inserted date has not happened yet

    Return:
        input_date (date): Input date
    """
    if input_date < date.today():
        raise ValidationError("The inserted date shouldn't be in the past")

    return input_date


def validator_no_negative(num: int) -> int:
    """
    Validate that the number is not negative

    Args:
        num (int): Input number

    Raises:
        ValidationError: The inserted number has to be '0' or positive

    Return:
        num (int): Input number
    """
    if num < 0:
        raise ValidationError("The inserted number has to be '0' or positive")

    return num


class FilmBusinessLogic:
    """
    The class contains all the business logic of the film app
    """
    @staticmethod
    def validate_stock_greater_availability(stock: int, availability: int):
        """
        Validate that the stock is greater than availability

        Args:
            stock (int): stock of the film
            availability (int): availability of the film

        Raises:
            ValidationError: The availability shouldn't be higher than stock
        """
        if availability > stock:
            raise ValidationError({'availability': _(
                "The availability shouldn't be higher than stock")})

    @staticmethod
    def validate_film_type_equal_prequel_film_type(film_type: str,
                                                   prequel_film_type: str):
        """
        Validate that type of the film and film prequel are equal

        Args:
            film_type (str): stock of the film
            prequel_film_type (str): availability of the film

        Raises:
            ValidationError: The film prequel should be the same type as the
             current film type
        """
        if prequel_film_type is not None:
            if film_type != prequel_film_type:
                raise ValidationError(
                    {'film_prequel': _('The film prequel should '
                                       'be the same type as '
                                       'the current film type. '
                                       '(Example both movie '
                                       'type)')})
