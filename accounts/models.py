from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django_google_maps import fields as map_fields
import pytz


### Create your models here.

user_type = (
    ("patient", "Patient"), ("doctor", "Doctor"), ("organization", "Organization")
)
gender_choices = (
    ("F", "Female"),
    ("M", "Male")
)


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given username, email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(
            email=email
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        """
        Create and save a superuser with the given username, email and password.
        """
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()
        return user



class CustomUser(AbstractUser):
    # General
    username = None
    USERNAME_FIELD = 'email'
    profile_picture = models.ImageField(upload_to="profile_pictures", null=True, blank=True)
    name = models.CharField(max_length=500, null=True)
    email = models.EmailField(unique=True)
    type = models.CharField(max_length=20, choices=user_type, default="patient")
    dob = models.CharField(null=True, blank=True, max_length=200)
    gender = models.CharField(max_length=1, choices=gender_choices, default="M", null=True)
    country = models.CharField(max_length=200, choices=pytz.country_names.items(), null=True)
    phone = PhoneNumberField(null=True)
    address = map_fields.AddressField(max_length=200, null=True, blank=True)
    latitude = models.FloatField(default=0.000, blank=True)
    longitude = models.FloatField(default=0.000, blank=True)
    location = models.PointField(null=True, blank=True)
    #geolocation = map_fields.GeoLocationField(max_length=100, null=True, blank=True)

    # Doctor
    '''
    degree = models.CharField(max_length=5000, null=True, blank=True)
    college = models.CharField(max_length=5000, null=True, blank=True)
    grad_year = models.CharField(null=True, blank=True, max_length=200)

    work_position = models.CharField(max_length=5000, null=True, blank=True)
    work_place = models.CharField(max_length=5000, verbose_name="place of work", null=True, blank=True)
    '''
    #work_start_year = models.DateField(null=True, blank=True)
    #work_end_year = models.DateField(null=True, blank=True)

    #Patient
    diabetes = models.BooleanField(default=False)
    asthma = models.BooleanField(default=False)
    blind = models.BooleanField(default=False)
    hypertension = models.BooleanField(default=False)
    spectacle_use = models.BooleanField(default=False)
    epilepsy = models.BooleanField(default=False)
    disabilities = models.BooleanField(default=False)
    sickle_cell = models.BooleanField(default=False)
    allergies = models.BooleanField(default=False)
    previous_surgery = models.BooleanField(default=False)

    moi = models.FileField(upload_to="identification_documents", verbose_name="Means of identification", null=True, blank=True)
    
    # Doctor
    experience = models.TextField(null=True, blank=True)
    education = models.TextField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    valid_license = models.FileField(upload_to="license", verbose_name="doctor's license", null=True, blank=True)
    doctor_certificate = models.FileField(upload_to="certificate", verbose_name="doctor's certificate", null=True, blank=True)
  
    #Business
    business_email = models.EmailField(unique=True, null=True, blank=True)
    business_name = models.CharField(max_length=500, null=True)
    prop_name = models.CharField(max_length=500, null=True, verbose_name="Director / Proprietor's Name")
    country_bus = models.CharField(max_length=500, null=True, verbose_name="Country business is based")
    how = models.CharField(max_length=500, null=True, verbose_name="How did you hear about Evoke e-health")
    cac = models.FileField(upload_to="license", verbose_name="CAC Certificate", null=True, blank=True)
    d_id = models.FileField(upload_to="license", verbose_name="Director's ID", null=True, blank=True)
    o_l = models.FileField(upload_to="license", verbose_name="Valid Operating License", null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)


class Education(models.Model):
    #doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    degree = models.CharField(max_length=5000, null=True, blank=True)
    college = models.CharField(max_length=5000, null=True, blank=True)
    grad_year = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return str(self.degree) +' @ '+ str(self.college)


class Experience(models.Model):
    #doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    position = models.CharField(max_length=5000, null=True, blank=True)
    work_place = models.CharField(max_length=5000, verbose_name="place of work", null=True, blank=True)
    start_year = models.CharField(null=True, blank=True, max_length=200)
    end_year = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.position + ' @ ' + self.work_place


class Symptoms(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)


class DoctorReport(models.Model):
	#doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    doctor = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class MedicalRecord(models.Model):
    patient = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.PROTECT, related_name="patient")
    marital_status = models.CharField(max_length=20, null=True, blank=True)
    previous_doctor = models.ForeignKey(CustomUser ,null=True, blank=True, on_delete=models.PROTECT, verbose_name="previous or referring doctor", related_name="doctor")
    date_of_last_exam = models.DateField()
    problems = models.TextField(null=True, blank=True)
    blood_transfusion = models.BooleanField(default=False)


class Profile(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True, blank=True, related_name="owner")
    patient = models.ManyToManyField(CustomUser, blank=True, related_name="patients")
