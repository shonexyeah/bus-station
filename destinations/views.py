from destinations.models import Destination
from destinations.serializers import DestinationSerializer, DestinationSerializerPost
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from destinations.filters import DestinationFilter


# Create your views here.
class DestinationListCreate(ListCreateAPIView):
    queryset = Destination.objects.all()
    filterset_class = DestinationFilter

    search_fields = ('unit_id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DestinationSerializerPost

        return DestinationSerializer




class DestinationDetail(RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return DestinationSerializerPost

        return DestinationSerializer



