from destinations.models import Destination
from destinations.serializers import DestinationSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.
class DestinationList(ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DestinationDetail(RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    #def get_object(self):
        #destination = Destination.objects.get(pk=self.kwargs['pk'])
        #return destination


    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


from django.shortcuts import render

# Create your views here.
