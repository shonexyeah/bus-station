from django.db import models
from core.models import DateModelMixin

from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator


# Create your models here.
class Vehicle(DateModelMixin):
    # basic info
    unique_number = models.CharField(max_length=2, unique=True)
    licence_plate = models.CharField(max_length=7, validators=[MinLengthValidator(7)] , unique=True)
    seating_capacity = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(200)])

    class Meta:
        ordering = ('-created_at', )


class VehicleStat(DateModelMixin):
    vehicle = models.ForeignKey('vehicles.Vehicle', on_delete=models.CASCADE)
    data = models.JSONField(default=dict)

    def __str__(self):
        return self.vehicle.unique_number

    class Meta:
        ordering = ('-created_at', )