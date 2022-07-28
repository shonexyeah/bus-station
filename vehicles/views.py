from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
class BusList(ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BusDetail(RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#class BusDelete(RetrieveUpdateDestroyAPIView):
    #queryset = Vehicle.objects.all()
    #serializer_class = VehicleSerializer

    #def delete(self, request, *args, **kwargs):
        #return self.destroy(request, *args, **kwargs)





# znaci moram koristiti generic view
# queryset bi se trebao korisitit za "vracanje" objekata iz ovog view