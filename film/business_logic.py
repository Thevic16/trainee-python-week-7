from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


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
