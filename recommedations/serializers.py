from rest_framework import serializers
from .models import Location


class LocationBasedRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"