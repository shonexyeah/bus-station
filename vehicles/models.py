from django.db import models
from core.models import DateModelMixin

from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator


# Create your models here.
class Vehicle(DateModelMixin):
    # basic info
    unique_number = models.CharField(max_length=2, unique=True) # da li je ovo nepohodno obzirom da se pravi ID svakako
    licence_plate = models.CharField(max_length=7, validators=[MinLengthValidator(7)] , unique=True)
    seating_capacity = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(200)])

    class Meta:
        ordering = ('-created_at', )


