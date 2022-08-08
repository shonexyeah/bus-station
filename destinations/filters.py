from django_filters import rest_framework as filters
from destinations.models import Destination



class DestinationFilter(filters.FilterSet):


    class Meta:
        model = Destination
        fields = {
            "id",
        }

