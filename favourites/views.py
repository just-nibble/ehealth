from django.shortcuts import render
from .serializers import FavouriteSerializer
from .models import Favourites
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.


class FavouriteListAPIView(ListCreateAPIView):
    serializer_class  = FavouriteSerializer
    queryset = Favourites.objects.all()


class FavouriteDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = FavouriteSerializer
    queryset = Favourites.objects.all()
