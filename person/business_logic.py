from datetime import date


class PersonBusinessLogic:
    """
    The class contains all the business logic of the person app
    """
    @staticmethod
    def get_age_by_birthday(birthday: date) -> date or str:
        """
        Validate that the stock is greater than availability

        Args:
            birthday (date): the birthday of the person

        Return:
            age (int): the current age of the person
            message (str): N.A, abbreviation for not applicable or not
            available
        """
        if birthday:
            return int((date.today() - birthday).days / 365.25)
        else:
            return "N.A"
