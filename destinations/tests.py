from rest_framework.test import APITestCase
from rest_framework import status
from destinations.models import Destination
from django.urls import reverse

# Create your tests here.
class CreationTest(APITestCase):

    def test_creation(self):
        data = {"address_street": "Pere Perica 13", "address_city": "Begec",
                "address_zip": "96352", "name": "SKP-TRS"}
        response = self.client.post("/destinations/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



class CreationDestinationTest(APITestCase):

    def setUp(self) -> None:
        self.destination = Destination.objects.create()
        self.data = {"address_street": "11.Novembra 68", "address_city": "Becej", "address_zip": "21220", "name": "BC"}

    def test_create(self):
        response = self.client.post(reverse('destination-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response_data = response.json()
        self.assertEqual(response_data['name'], "BC")
        print(response_data)


class ReadDestinationTest(APITestCase):
    def setUp(self):
        self.destination = Destination.objects.create(address_street="11.Novembra 68", address_city="Becej",
                                                      address_zip="21220", name="BC")
        self.destination = Destination.objects.create(address_street="11.Novembra 69", address_city="Stari Becej",
                                                      address_zip="21221", name="NS")
        self.destination = Destination.objects.create(address_street="11.Novembra 70", address_city="Novi Becej",
                                                      address_zip="21222", name="ZR")
        self.destination = Destination.objects.create(address_street="11.Novembra 71", address_city="Izmisljeni Becej",
                                                      address_zip="21223", name="LK")


    def test_destination_read(self):
        response = self.client.get(reverse('destination-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        print(response_data)


    def test_read_destination_detail(self):
        response = self.client.get(reverse('destination-detail', args=[self.destination.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)