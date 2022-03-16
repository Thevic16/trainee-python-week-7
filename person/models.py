from django.db import models
from django.utils.encoding import smart_text
from film.models import Film
from django.core.validators import RegexValidator

# Create your models here.
from film.business_logic import validator_date_limit_today
from person.business_logic import PersonBusinessLogic

GENDER_CHOICES = {
    ('male', 'Male'),
    ('feminine', 'Feminine'),
    ('other', 'Other'),
}

PERSON_TYPE_CHOICES = {
    ('film related', 'Film related'),
    ('client', 'Client'),
}


class Person(models.Model):
    name = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    gender = models.CharField(max_length=120, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(validators=[validator_date_limit_today])
    person_type = models.CharField(max_length=120, choices=PERSON_TYPE_CHOICES)

    def __str__(self):
        return smart_text(f"{self.name} {self.lastname}")

    @property
    def age(self):
        return PersonBusinessLogic.get_age_by_birthday(self.date_of_birth)


class Role(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return smart_text(self.name)


class FilmPersonRole(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE,
                               limit_choices_to={'person_type': 'film related'}
                               )
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return smart_text(f"{self.role.name} - {self.film.title} - "
                          f"{self.person.name} {self.person.lastname}")


class Client(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE,
                                  limit_choices_to={'person_type': 'client'})
    direction = models.TextField()
    phone = models.CharField(max_length=120, validators=[
        RegexValidator(r'^\d{3}-\d{4}-\d{4}$')])
    email = models.EmailField()

    def __str__(self):
        return smart_text(f"{self.person.name} {self.person.lastname}")
