from django.db import models
from django.contrib.auth.models import AbstractUser
import pytz
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


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
    def create_user(self, email, username, password, **extra_fields):
        """
        Create and save a User with the given username, email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
                )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password=None):
        """
        Create and save a superuser with the given username, email and password.
        """
        user = self.create_user(email, username, password=password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()
        return user


class Education(models.Model):
    degree = models.CharField(max_length=5000)
    college = models.CharField(max_length=5000)
    grad_year = models.DateField()

    def __str__(self):
        return self.degree +' @ '+ self.college


class Experience(models.Model):
    work_place = models.CharField(max_length=5000)
    role = models.CharField(max_length=5000)
    start_year = models.DateField()
    end_year = models.DateField()

    def __str__(self):
        return self.role + ' @ ' + self.work_place


class CustomUser(AbstractUser):
    name = models.CharField(max_length=500, null=True)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(unique=True, max_length=15)
    type = models.CharField(max_length=20, choices=user_type, default="patient")
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=gender_choices, default="M", null=True)
    country = models.CharField(max_length=2, choices=pytz.country_names.items(), null=True)
    address = models.CharField(max_length=5000, null=True)
    phone = PhoneNumberField(null=True)
    education = models.ForeignKey(Education, on_delete=models.CASCADE, null=True)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, null=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]
    objects = CustomUserManager()
    def __str__(self):
        return str(self.email)


