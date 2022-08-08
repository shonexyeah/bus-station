from rest_framework.test import APITestCase
from rest_framework import status
from vehicles.models import Vehicle
from django.urls import reverse


class CreationVehicleTest(APITestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle.objects.create()
        self.data = {"unique_number": "22", "licence_plate": "BC007NX", "seating_capacity": "12"}

    def test_create(self):
        response = self.client.post(reverse('vehicle-list-create'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response_data = response.json()
        self.assertEqual(response_data['unique_number'], "22")
        print(response_data)


class ReadVehicleTest(APITestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(unique_number="33", licence_plate="BC009NX", seating_capacity="200")
        self.vehicle = Vehicle.objects.create(unique_number="22", licence_plate="BC007NX", seating_capacity="12")
        self.vehicle = Vehicle.objects.create(unique_number="12", licence_plate="NS007NX", seating_capacity="50")
        self.vehicle = Vehicle.objects.create(unique_number="51", licence_plate="PA921LK", seating_capacity="50")


    def test_vehicle_read(self):
        response = self.client.get(reverse('vehicle-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        print(response_data)


    def test_read_vehicle_detail(self):
        response = self.client.get(reverse('vehicle-detail', args=[self.vehicle.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)






# class FilterTest(APITestCase):
#     def setUp(self):
#             self.vehicle = Vehicle.objects.create(unique_number="33", licence_plate="BC009NX", seating_capacity="200")
#             self.vehicle = Vehicle.objects.create(unique_number="22", licence_plate="BC007NX", seating_capacity="12")
#             self.vehicle = Vehicle.objects.create(unique_number="12", licence_plate="NS007NX", seating_capacity="50")
#             self.vehicle = Vehicle.objects.create(unique_number="51", licence_plate="PA921LK", seating_capacity="50")
#
#     def test_filter(self):
#         response = self.client.get(reverse('bus-detail', args=[self.vehicle.seating_capacity]))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#         response_data = response.json()
#         self.assertEqual(response_data['seating_capacity'], "50")
#         print(response_data)




    # def test_creation(self):
    #     data = {"unique_number": "22", "licence_plate": "BC070NX", "seating_capacity": "12"}
    #     response = self.client.post("/vehicles/", data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     print(response.json())
    #
    #
    #
    #     # response_data = response.json()
    #     # self.assertEqual(response_data['unique_number'], "22")
    #
    # def test_bus_list(self):
    #     url = reverse('bus-list')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    #
    #
    # def test_filter_bus_list(self):
    #     pass
