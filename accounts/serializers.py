from django.db.models import fields
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from phonenumber_field.serializerfields import PhoneNumberField
from .models import Education, Experience

User = get_user_model()

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
    


class RegistrationSerializer(RegisterSerializer):

    type = serializers.CharField(required=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    name = serializers.CharField(required=False) 
    dob = serializers.DateField(required=True)
    gender = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    phone = PhoneNumberField()
    education = EducationSerializer(required=False)
    experience = ExperienceSerializer(required=False)
 
        
    def custom_signup(self, request, user):
        user.type = self.validated_data.get('type', '')
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')  
        user.gender = self.validated_data.get('gender', '')
        user.phone = self.validated_data.get('phone', '')
        user.address = self.validated_data.get('address', '')
        user.country = self.validated_data.get('country', '')
        user.dob = self.validated_data.get('dob', '')
        education = self.validated_data['education']
        edu = Education.objects.create(**education)
        user.education = edu
        experience = self.validated_data['experience']
        exp = Experience.objects.create(**experience)
        user.experience = exp
        user.save()
        
    