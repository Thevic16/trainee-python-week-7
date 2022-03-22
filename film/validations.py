from datetime import date
from django.core.exceptions import ValidationError


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
