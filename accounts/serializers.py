from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from .models import CustomUser


class RegistrationSerializer(RegisterSerializer):
    username = None
    type = serializers.CharField(required=True)

    def custom_signup(self, request, user):
        user.type = self.validated_data.get('type', '')  
        user.save(update_fields=['type'])
