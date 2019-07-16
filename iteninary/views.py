from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Iteninary, Path, Transport, Activity, Housing
from .serializers import (
    HousingSerializer,
    ActivitiesSerializer,
    TransportationSerializer,
    PathsSerializer,
    IteninarySerializer,)
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> Home </h1>')

def housingsave(request):
    path = Path.objects.last()
    housings = request.data["housing"]
    for housing in housings:
        serializer = HousingSerializer(data=housing)
        if serializer.is_valid():
            serializer.save()
            path.housing.add(Housing.objects.last())
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
def activitiessave(request):
    path = Path.objects.last()
    activities = request.data["activities"]
    for activity in activities:
        serializer = ActivitiesSerializer(data=activity)
        if serializer.is_valid():
            serializer.save()
            path.activities.add(Activity.objects.last())
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
def transportsave(request):
    path = Path.objects.last()
    transportations = request.data["transportation"]
    for transportation in transportations:
        serializer = TransportationSerializer(data=transportation)
        if serializer.is_valid():
            serializer.save()
            path.transportation.add(Transport.objects.last())
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def pathsave(request):
    iteninary = Iteninary.objects.last()
    paths = request.data["paths"]
    for path in paths:
        serializer = PathsSerializer(data=path)
        if serializer.is_valid():
            serializer.save()
            iteninary.paths.add(Path.objects.last())
            pathhousingsave(path)
            pathactivitiessave(path)
            pathtransportsave(path)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def pathhousingsave(sentpath):
    path = Path.objects.last()
    housings = sentpath["housing"]
    for housing in housings:
        serializer = HousingSerializer(data=housing)
        if serializer.is_valid():
            serializer.save()
            path.housing.add(Housing.objects.last())
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def pathtransportsave(sentpath):
    path = Path.objects.last()
    transportations = sentpath["transportation"]
    for transportation in transportations:
        serializer = TransportationSerializer(data=transportation)
        if serializer.is_valid():
            serializer.save()
            path.transportation.add(Transport.objects.last())
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def pathactivitiessave(sentpath):
    path = Path.objects.last()
    activities = sentpath["activities"]
    for activity in activities:
        serializer = ActivitiesSerializer(data=activity)
        if serializer.is_valid():
            serializer.save()
            path.activities.add(Activity.objects.last())
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class HousingList(APIView):
    
    def get(self, request):
        housings = Housing.objects.all()
        serializer = HousingSerializer(housings, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = HousingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivityList(APIView):

    def get(self, request):
        activities = Activity.objects.all()
        serializer = ActivitiesSerializer(activities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ActivitiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransportList(APIView):

    def get(self, request):
        transports = Transport.objects.all()
        serializer = TransportationSerializer(transports, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TransportationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PathList(APIView):

    def get(self, request):
        paths = Path.objects.all()
        serializer = PathsSerializer(paths, many=True)
        return Response(serializer.data)
    def post(self, request):
        path_serializer = PathsSerializer(data=request.data)
        if path_serializer.is_valid():
            path_serializer.save()
        else:
            return Response(path_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        housingsave(request)
        activitiessave(request)
        transportsave(request)
        return Response(path_serializer.data, status=status.HTTP_201_CREATED)


class IteninaryList(APIView):

    def get(self, request):
        iteninaries = Iteninary.objects.all()
        serializer = IteninarySerializer(iteninaries, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = IteninarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        pathsave(request)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

