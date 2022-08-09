from routes.models import Route
from routes.serializers import RouteSerializer, RouteSerializerPost
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from routes.filters import RouteFilter

# Create your views here.
class RouteListCreate(ListCreateAPIView):
    queryset = Route.objects.all()
    filterset_class = RouteFilter

    search_fields = ('unit_id', 'finish_line')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RouteSerializerPost

        return RouteSerializer



class RouteDetail(RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return RouteSerializerPost

        return RouteSerializer
