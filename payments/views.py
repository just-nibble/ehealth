from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PaymentPlanSerializer
from djangoflutterwave.models import FlwPlanModel


# Create your views here.


class PlanListAPIView(ListCreateAPIView):
	serializer_class = PaymentPlanSerializer
	queryset = FlwPlanModel.objects.all()


class PlanDetailAPIView(RetrieveUpdateDestroyAPIView):
	serializer_class = PaymentPlanSerializer
	queryset = FlwPlanModel.objects.all()
