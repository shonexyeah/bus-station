from rest_framework.test import APITestCase
from rest_framework import status
from routes.models import Route
from django.urls import reverse
from destinations.models import Destination
from vehicles.models import Vehicle


# Create your tests here.
class CreationRouteTest(APITestCase):

    def setUp(self) -> None:

        self.vehicle = Vehicle.objects.create(unique_number="33", licence_plate="BC009NX", seating_capacity="200")
        self.destination = Destination.objects.create(address_street="11.Novembra 68", address_city="Becej",
                                                      address_zip="21220", name="BC")

        self.route = Route.objects.create(
            start_point="SKP", finish_line_id=self.destination.id,
            seating_capacity="5", unique_number_id=self.vehicle.id)

        self.data = {"start_point": "SKP", "finish_line": self.destination.id,
                     "seating_capacity": "5", "unique_number": self.vehicle.id}

    def test_create(self):
        response = self.client.post(reverse('route-list-create'), self.data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response_data = response.json()
        self.assertEqual(response_data['start_point'], "SKP")
        print(response_data)






# self.route = Route.objects.create(start_point="SKP", finish_line_id="", finished_at="",
        #                                   seating_capacity="5", unique_number_id="")