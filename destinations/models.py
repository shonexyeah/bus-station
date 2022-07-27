from django.db import models
from core.models import DateModelMixin


# Create your models here.
class Destination(DateModelMixin):
    # adress info
    address_street = models.CharField(max_length=128)
    address_city = models.CharField(max_length=64)
    address_zip = models.CharField(max_length=5)

    # basic info
    name = models.CharField(max_length=64)

    class Meta:
        ordering = ('-created_at', )
