from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from accounts.models import CustomUser
from .serializers import LocationBasedRecommendationSerializer
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import fromstr

from django.contrib.gis.geos import Point
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import get_object_or_404

# Create your views here.


class LocationRecommendationListAPIView(APIView):

    def get(self, request, format=None):
        
        current_user = self.request.user
        #longitude = -80.191788
        #latitude = 25.761681

        #user_location = Point(longitude, latitude, srid=4326)
        #current_user = CustomUser.objects.get(id=self.request.user.id)
        #current_user = get_object_or_404(CustomUser, pk=1)
        #user_longitude = current_user.longitude
        #user_latitude = current_user.latitude
        user_location = current_user.location
        doctors = CustomUser.objects.annotate(distance=Distance('location', user_location)).exclude(email=current_user.email).exclude(latitude=0.0)

        

        serializer = LocationBasedRecommendationSerializer(doctors, many=True)
        #permission_classes = (permissions.IsAuthenticated,)
        return Response(serializer.data)


class DoctorLocationRecommendationListAPIView(APIView):

    def get(self, request, format=None):
        
        current_user = self.request.user
        #longitude = -80.191788
        #latitude = 25.761681

        #user_location = Point(longitude, latitude, srid=4326)
        #current_user = CustomUser.objects.get(id=self.request.user.id)
        #current_user = get_object_or_404(CustomUser, pk=1)
        #user_longitude = current_user.longitude
        #user_latitude = current_user.latitude
        user_location = current_user.location
        doctors = CustomUser.objects.annotate(distance=Distance('location', user_location)).exclude(email=current_user.email).exclude(latitude=0.0).filter(type="Doctor")

        

        serializer = LocationBasedRecommendationSerializer(doctors, many=True)
        #permission_classes = (permissions.IsAuthenticated,)
        return Response(serializer.data)


class HospitalLocationRecommendationListAPIView(APIView):

    def get(self, request, format=None):
        
        current_user = self.request.user
        user_location = current_user.location
        doctors = CustomUser.objects.annotate(distance=Distance('location', user_location)).exclude(email=current_user.email).exclude(latitude=0.0).filter(type="Organization")

        

        serializer = LocationBasedRecommendationSerializer(doctors, many=True)
        #permission_classes = (permissions.IsAuthenticated,)
        return Response(serializer.data)
