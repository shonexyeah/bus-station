from rest_framework.views import Response, APIView


class HomePage(APIView):

    def get(self, request):

        arguments = {
        'vehicles': 'http://127.0.0.1:8100/vehicles/',
        'destinations': 'http://127.0.0.1:8100/destinations/',
        'routes': 'http://127.0.0.1:8100/routes/',
    }

        return Response(arguments)

