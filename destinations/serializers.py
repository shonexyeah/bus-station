from rest_framework import serializers
from destinations.models import Destination


class DestinationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Destination
        fields = '__all__'
