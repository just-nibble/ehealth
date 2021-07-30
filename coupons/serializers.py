from rest_framework import serializers
from .models import Coupon

class CouponSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ("__all__")
