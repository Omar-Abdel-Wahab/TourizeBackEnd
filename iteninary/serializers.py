from rest_framework import serializers
from .models import Iteninary, Path, Transport, Activity, Housing

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

class PathsSerializer(serializers.ModelSerializer):
    transportation = TransportationSerializer(read_only=True,many=True)
    housing = HousingSerializer(read_only=True,many=True)
    activities = ActivitiesSerializer(read_only=True,many=True) 
    class Meta:
        model = Path
        fields = [
            'origin',
            'destination',
            'start_date',
            'end_date',
            'open',
            'transportation',
            'housing',
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

    