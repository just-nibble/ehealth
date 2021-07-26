from re import I
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import UserSerializer
from django.contrib.auth import get_user_model as User
from django_filters import rest_framework as filters

# Create your views here.

class UserListSeriializer(ListCreateAPIView):
	pass
	#serializer_class = UserSerializer
	#queryset = User.objects.all()
	#filter

