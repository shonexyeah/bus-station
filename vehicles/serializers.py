from rest_framework import serializers
from vehicles.models import Vehicle


class VehicleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'
