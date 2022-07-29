from django_filters import rest_framework as filters
from routes.models import Route



class RouteFilter(filters.FilterSet):


    class Meta:
        model = Route
        fields = {
            "id",
            "finish_line",
        }