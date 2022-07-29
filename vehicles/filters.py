from django_filters import rest_framework as filters
from vehicles.models import Vehicle



class VehicleFilter(filters.FilterSet):


    class Meta:
        model = Vehicle
        fields = {
            "id",
        }

