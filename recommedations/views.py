from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from accounts.models import CustomUser
from .serializers import LocationBasedRecommendationSerializer
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import fromstr

from django.contrib.gis.geos import Point
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class LocationRecommendationListAPIView(APIView):

    def get(self, request, format=None):
        #current_user_loc = self.request.user.location
        longitude = -80.191788
        latitude = 25.761681

        user_location = Point(longitude, latitude, srid=4326)

        doctors = CustomUser.objects.annotate(distance=Distance('location', user_location))

        serializer = LocationBasedRecommendationSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LocationBasedRecommendationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)