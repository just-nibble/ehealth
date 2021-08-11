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

    username = None
    type = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    #name = serializers.CharField(required=False) 
    dob = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    phone = PhoneNumberField(required=False)

    #patient
    diabetes = serializers.BooleanField(default=False)
    asthma = serializers.BooleanField(default=False)
    blind = serializers.BooleanField(default=False)
    hypertension = serializers.BooleanField(default=False)
    spectacle_use = serializers.BooleanField(default=False)
    epilepsy = serializers.BooleanField(default=False)
    disabilities = serializers.BooleanField(default=False)
    sickle_cell = serializers.BooleanField(default=False)
    allergies = serializers.BooleanField(default=False)
    previous_surgery = serializers.BooleanField(default=False)

    #doctor
    education = serializers.JSONField(allow_null=True, required=False)
    experience = serializers.JSONField(allow_null=True, required=False)

    business_email = serializers.EmailField(required=False)
    business_name = serializers.CharField(required=False)
    prop_name = serializers.CharField(label="Director / Proprietor's Name", required=False)
    country_bus = serializers.CharField(label="Country business is based", required=False)
    how = serializers.CharField(label="How did you hear about Evoke e-health", required=False)
    cac = serializers.FileField(required=False, label="CAC Certificate", allow_null=True)
    d_id = serializers.FileField(required=False, label="Director's ID", allow_null=True)
    o_l = serializers.FileField(required=False, label="Valid Operating License", allow_null=True)
 

    def custom_signup(self, request, user):
        #general
        user.type = self.validated_data.get('type', '')
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')  
        user.gender = self.validated_data.get('gender', '')
        user.phone = self.validated_data.get('phone', '')
        user.address = self.validated_data.get('address', '')
        user.country = self.validated_data.get('country', '')
        user.dob = self.validated_data.get('dob', '')

        #doctor
        #user.degree = self.validated_data.get('degree', '')
        #user.college = self.validated_data.get('college', '')
        #user.grad_year = self.validated_data.get('grad_year', '')
        #user.work_position = self.validated_data.get('work_position', '')
        #user.work_place = self.validated_data.get('work_place', '')
        #user.work_start_year = self.validated_data.get('work_start_year', '')
        #user.work_end_year = self.validated_data.get('work_end_year', '')
        user.education = self.validated_data.get('education', '')
        user.experience = self.validated_data.get('experience', '')


        #patient
        user.diabetes = self.validated_data.get('diabetes', '')
        user.asthma = self.validated_data.get('asthma', '')
        user.blind = self.validated_data.get('blind', '')
        user.hypertension = self.validated_data.get('hypertension', '')
        user.spectacle_use = self.validated_data.get('spectacle_use', '')
        user.epilepsy = self.validated_data.get('epilepsy', '')
        user.disabilities = self.validated_data.get('disabilities', '')
        user.sickle_cell = self.validated_data.get('sickle_cell', '')
        user.allergies = self.validated_data.get('allergies', '')
        user.previous_surgery = self.validated_data.get('previous_surgery', '')

        #organization
        user.business_email = self.validated_data.get('business_email', '')
        user.business_name = self.validated_data.get('business_name', '')
        user.prop_name = self.validated_data.get('prop_name', '')
        user.country_bus = self.validated_data.get('country_bus', '')
        user.how = self.validated_data.get('how', '')
        user.cac = self.validated_data.get('cac', '')
        user.d_id = self.validated_data.get('d_id', '')
        user.o_l = self.validated_data.get('o_l', '')
        
        user.save()

        
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model
        fields = "__all__"