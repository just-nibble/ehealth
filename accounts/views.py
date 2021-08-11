from re import I
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer
from .models import CustomUser
#from django_filters import rest_framework as filters

# Create your views here.

class UserListAPIView(ListCreateAPIView):
	serializer_class = UserSerializer
	queryset = CustomUser.objects.all()


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
	serializer_class = UserSerializer
	queryset = CustomUser.objects.all()
