from rest_framework import serializers
from routes.models import Route


class RouteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Route
        fields = '__all__'


class RouteSerializerPost(serializers.ModelSerializer):

    class Meta:
        model = Route
        fields = '__all__'