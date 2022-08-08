from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer, VehicleSerializerPost
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from vehicles.filters import VehicleFilter

# Create your views here.
class VehicleListCreate(ListCreateAPIView):
    queryset = Vehicle.objects.all()
    filterset_class = VehicleFilter

    search_fields = ('unit_id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return VehicleSerializerPost

        return VehicleSerializer


class VehicleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
