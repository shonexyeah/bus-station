from rest_framework.views import Response, APIView


class HomePage(APIView):

    def get(self, request):

        arguments = {
        'VEHICLES': 'http://127.0.0.1:8100/vehicles/',
        'DESTINATIONS': 'http://127.0.0.1:8100/destinations/',
        'ROUTES': 'http://127.0.0.1:8100/routes/',
    }

        return Response(arguments)

