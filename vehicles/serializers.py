from rest_framework import serializers
from vehicles.models import Vehicle # ZASTO ? sta nisam uradio dobro


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'
