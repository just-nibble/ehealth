from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CouponSerilaizer
from .models import Coupon
# Create your views here.


class CouponListAPIView(ListCreateAPIView):
    serializer_class = CouponSerilaizer
    queryset = Coupon.objects.all()



class CouponDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CouponSerilaizer
    queryset = Coupon.objects.all()