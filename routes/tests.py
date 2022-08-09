from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse

from destinations.models import Destination
from vehicles.models import Vehicle
from routes.models import Route

from routes.serializers import RouteSerializerPost
from vehicles.serializers import VehicleSerializerPost
from destinations.serializers import DestinationSerializerPost


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


class ReadRouteTest(APITestCase):

    def setUp(self):

        self.vehicle = Vehicle.objects.create(unique_number="33", licence_plate="BC009NX", seating_capacity="50")
        self.destination = Destination.objects.create(address_street="11.Novembra 68", address_city="Becej",
                                                      address_zip="21220", name="BC")

        self.route = Route.objects.create(start_point="SKP", finish_line_id=self.destination.id,
                                          seating_capacity="20", unique_number_id=self.vehicle.id)

    def test_route_read(self):
        response = self.client.get(reverse('route-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        print(response_data)

    def test_read_route_detail(self):
        response = self.client.get(reverse('route-detail', args=[self.route.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateRouteTest(APITestCase):
    def setUp(self):

        self.vehicle = Vehicle.objects.create(unique_number="33", licence_plate="BC009NX", seating_capacity="50")
        self.destination = Destination.objects.create(address_street="11.Novembra 68", address_city="Becej",
                                                      address_zip="21220", name="BC")

        self.route = Route.objects.create(start_point="SKP", finish_line_id=self.destination.id,
                                          seating_capacity="20", unique_number_id=self.vehicle.id)

        self.data = {"start_point": "SKP", "finish_line": self.destination.id,
                     "seating_capacity": "20", "unique_number": self.vehicle.id}

        self.data = RouteSerializerPost(self.route).data
        self.data.update({"seating_capacity": "50"})
        print(self.data)

    def test_update_route(self):
        response = self.client.put(reverse('route-detail', args=[self.route.id]), self.data)
        response_data = response.json()
        print(response_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)




class DeleteRouteTest(APITestCase):
    def setUp(self):

        self.vehicle = Vehicle.objects.create(unique_number="33", licence_plate="BC009NX", seating_capacity="50")
        self.destination = Destination.objects.create(address_street="11.Novembra68", address_city="Becej",
                                                      address_zip="21220", name="BC")

        self.route = Route.objects.create(start_point="SKP", finish_line_id=self.destination.id,
                                          seating_capacity="20", unique_number_id=self.vehicle.id)

    def test_delete_route(self):
        response = self.client.delete(reverse('route-detail', args=[self.route.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

# self.route = Route.objects.create(start_point="SKP", finish_line_id="", finished_at="",
        #                                   seating_capacity="5", unique_number_id="")