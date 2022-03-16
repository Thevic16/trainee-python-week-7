from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils.encoding import smart_text
from film.models import Film
from person.models import Client
from django.db.models.signals import pre_save
from film.business_logic import (validator_no_negative,
                                 validator_date_limit_future)
from rent.business_logic import RentBusinessLogic

STATE_CHOICES = {
    ('open', 'Open'),
    ('close', 'Close'),
}


class Rent(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.Model)
    amount = models.IntegerField(validators=[validator_no_negative])
    start_date = models.DateField(validators=[validator_date_limit_future])
    return_date = models.DateField(validators=[validator_date_limit_future])
    actual_return_date = models.DateField(
        validators=[validator_date_limit_future], blank=True, null=True)
    state = models.CharField(max_length=120, choices=STATE_CHOICES)

    def __str__(self):
        return smart_text(f"{self.film.title} - {self.client.person.name}"
                          f"  {self.client.person.lastname} -"
                          f" {self.return_date} ")

    @property
    def cost(self):
        return RentBusinessLogic.get_rent_cost(self.amount, self.start_date,
                                               self.return_date,
                                               self.actual_return_date,
                                               self.film.price_by_day)


def rent_model_pre_save_receiver(sender, instance, *args, **kwargs):
    # Validations that should always happen
    RentBusinessLogic.validate_state_close(instance.state,
                                           instance.actual_return_date)

    RentBusinessLogic.validate_date1_eq_or_low_date2(
        instance.return_date, instance.start_date, 'return_date'
    )

    RentBusinessLogic.validate_date_gt_max_limit(
        instance.return_date, instance.start_date, 'return_date'
    )

    RentBusinessLogic.validate_date1_gr_or_eq_date2(
        instance.actual_return_date, instance.start_date, 'actual_return_date'
    )

    try:
        # update
        pre_save_rent = Rent.objects.get(id=instance.id)
        RentBusinessLogic.validate_update_permission(pre_save_rent.state)

        RentBusinessLogic.state_close_return_films(instance.state,
                                                   pre_save_rent.state,
                                                   instance.amount,
                                                   instance.film)

        RentBusinessLogic.validate_amount_update(instance.amount,
                                                 instance.film,
                                                 pre_save_rent)
    except ObjectDoesNotExist:
        # create first time
        RentBusinessLogic.validate_amount_availability(instance.amount,
                                                       instance.film)

        RentBusinessLogic.state_close_return_films(instance.state,
                                                   "open",
                                                   instance.amount,
                                                   instance.film)


pre_save.connect(rent_model_pre_save_receiver, sender=Rent)
