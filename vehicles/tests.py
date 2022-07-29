from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from vehicles.models import Vehicle

# Create your tests here.

class VehicleTest(APITestCase):
    def test_create_vehicle(self):

        url = reverse('vehicle-list')
        data = {'id': '01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vehicle.objects.count(), 1)
        self.assertEqual(Vehicle.objects.get().name, '01')