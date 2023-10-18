from datetime import date
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Trackable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Person(Trackable):
    class Genders(models.TextChoices):
        MALE = "M", "MALE"
        FEMALE = "F", "FEMALE"

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(null=True, blank=True, unique=True)
    gender =  models.CharField(max_length=3, choices=Genders.choices, blank=True, null=True)
    date_of_birth = models.DateField()
    industry = models.CharField(max_length=150, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))], blank=True, null=True)
    years_of_experience = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"