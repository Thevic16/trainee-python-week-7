from django.db import models
from django.db.models.signals import pre_save
from django.utils.encoding import smart_text
from film.business_logic import (validator_date_limit_today,
                                 validator_no_negative, FilmBusinessLogic)

FILM_TYPE_CHOICES = {
    ('movie', 'Movie'),
    ('serie', 'Serie'),
}


class Category(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return smart_text(self.name)


class Film(models.Model):
    title = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    release_date = models.DateField(validators=[validator_date_limit_today])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price_by_day = models.DecimalField(max_digits=15, decimal_places=2,
                                       validators=[validator_no_negative])
    stock = models.IntegerField(validators=[validator_no_negative])
    availability = models.IntegerField(validators=[validator_no_negative])
    film_type = models.CharField(max_length=120, choices=FILM_TYPE_CHOICES)

    film_prequel = models.OneToOneField('self', on_delete=models.CASCADE,
                                        null=True, blank=True)

    def __str__(self):
        return smart_text(self.title)


def film_model_pre_save_receiver(sender, instance, *args, **kwargs):
    FilmBusinessLogic.validate_stock_greater_availability(instance.stock,
                                                          instance.availability
                                                          )
    if instance.film_prequel is not None:
        FilmBusinessLogic.validate_film_type_equal_prequel_film_type(
                instance.film_type, instance.film_prequel.film_type)


pre_save.connect(film_model_pre_save_receiver, sender=Film)


class Season(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE,
                             limit_choices_to={'film_type': 'serie'})
    title = models.CharField(max_length=120)
    season_prequel = models.OneToOneField('self', on_delete=models.CASCADE,
                                          null=True, blank=True)

    def __str__(self):
        return smart_text(f"{self.film.title} - {self.title} ")


class Chapter(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    chapter_prequel = models.OneToOneField('self', on_delete=models.CASCADE,
                                           null=True, blank=True)

    def __str__(self):
        return smart_text(f"{self.season.film.title} - {self.season.title}"
                          f" - {self.title} ")
