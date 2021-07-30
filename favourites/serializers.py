from rest_framework import serializers
from .models import Favourites


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourites
