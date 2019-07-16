from rest_framework import serializers
from .models import Iteninary, Path, Restaurant, Transport, Activity, Housing

class HousingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Housing
        fields = [
            'location',
            'type',
            'price',
        ] 

class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = [
            'location',
            'type',
            'start_date',
            'end_date',
        ] 

class TransportationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = [
            'type',
            'price',
            'provider',
            'start_date',
            'end_date',
        ] 

class RestaurantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'price',
            'name',
        ] 


class PathsSerializer(serializers.ModelSerializer):
    transportation = TransportationSerializer(read_only=True,many=True)
    housing = HousingSerializer(read_only=True,many=True)
    restaurants = RestaurantsSerializer(read_only=True,many=True)
    activities = ActivitiesSerializer(read_only=True,many=True) 
    class Meta:
        model = Path
        fields = [
            'origin',
            'destination',
            'start_date',
            'end_date',
            'transportation',
            'housing',
            'restaurants',
            'activities',
        ] 


class IteninarySerializer(serializers.ModelSerializer):
    paths = PathsSerializer(read_only=True,many=True)
    class Meta:
        model = Iteninary
        fields = [
            'title',
            'start_date',
            'end_date',
            'paths',
        ] 

    