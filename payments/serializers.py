from rest_framework import serializers
from djangoflutterwave.models import FlwPlanModel


class PaymentPlanSerializer(serializers.ModelSerializer):
	class Meta:
		model = FlwPlanModel
		fields = ("__all__")
