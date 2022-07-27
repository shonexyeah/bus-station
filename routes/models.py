from django.db import models
from core.models import DateModelMixin


# Create your models here.
class Route(DateModelMixin):
    # city info
    start_point = models.CharField(max_length=64, default='SKP')
    finish_line = models.ForeignKey('destinations.Destination', on_delete=models.PROTECT) #treba povezati sa destinations/destination

    # time info
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(auto_now=True)

    # vehicle info
    seating_capacity = models.IntegerField()
    unique_number = models.ForeignKey('vehicles.Vehicle', on_delete=models.PROTECT) #povezati sa vehicles/models unique number?


    class Meta():
        ordering = ('-created_at', )
