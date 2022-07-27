from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
class BusList(ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class BusDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleSerializer

    def get_object(self):
        vehicle = Vehicle.objects.get(pk=self.kwargs['pk'])
        return vehicle




# znaci moram koristiti generic view
# queryset bi se trebao korisitit za "vracanje" objekata iz ovog view