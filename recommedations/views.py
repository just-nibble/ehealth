from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Location
from .serializers import LocationBasedRecommendationSerializer
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos.point import Point
# Create your views here.


class LocationRecommendationListAPIView(ListCreateAPIView):
    longitude = -80.191788
    latitude = 25.761681
    user_location = Point(longitude, latitude, srid=4326)
    serializer_class = LocationBasedRecommendationSerializer
    queryset = Location.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:6]