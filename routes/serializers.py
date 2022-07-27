from rest_framework import serializers
from routes.models import Route


class VehicleSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Route
        fields = '__all__'
