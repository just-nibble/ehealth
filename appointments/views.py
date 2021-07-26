from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import AppointmentSerializer
from .models import Appointment
# Create your views here.


class AppointmentListAPIView(ListCreateAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class AppointmentDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
