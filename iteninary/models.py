from django.db import models


class Activity(models.Model):

    HIKING = 'Hiking'
    CAMPING = 'Camping'
    SIGHTSEEING = 'Sightseeing'
    MOUNTAINING = 'Mountaining'
    SAILING = 'Sailing'
    BIKING = 'Biking'
    FISHING = 'Fishing'

    ACTIVITY_CHOICES = (
        (HIKING, 'Hiking'),
        (CAMPING, 'Camping'),
        (SIGHTSEEING, 'Sightseeing'),
        (MOUNTAINING, 'Mountaining'),
        (SAILING, 'Sailing'),
        (BIKING, 'Biking'),
        (FISHING, 'Fishing'),
    )

    location = models.CharField(max_length=255)
    type = models.CharField(max_length=11,choices=ACTIVITY_CHOICES)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.type + "-" + self.location

class Housing(models.Model):
    HOSTEL = 'Hostel'
    HOTEL = 'Hotel'
    
    HOUSING_CHOICES = (
        (HOSTEL, 'Hostel'),
        (HOTEL, 'Hotel'),
    )

    location = models.CharField(max_length=255)
    type = models.CharField(max_length=6,choices=HOUSING_CHOICES)
    price = models.FloatField()

    def __str__(self):
        return self.type + "-" + self.location


class Transport(models.Model):
    BUS = 'Bus'
    TAXI = 'Taxi'
    CAR = 'Car'
    TRAIN = 'Train'
    PLANE = 'Plane'
    
    TRANSPORTATION_CHOICES = (
        (BUS, 'Bus'),
        (TAXI, 'Taxi'),
        (CAR, 'Car'),
        (TRAIN, 'Train'),
        (PLANE, 'Plane'),
    )

    type = models.CharField(max_length=5,choices=TRANSPORTATION_CHOICES)
    price = models.FloatField()
    provider = models.CharField(max_length=70)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.type + "-" + self.provider

class Path(models.Model):
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    open = models.BooleanField()
    transportation = models.ManyToManyField(Transport)
    housing = models.ManyToManyField(Housing)
    activities = models.ManyToManyField(Activity)

    def __str__(self):
        return self.origin + "-" + self.destination

class Iteninary(models.Model):
    title = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    paths = models.ManyToManyField(Path)

    def __str__(self):
        return self.title