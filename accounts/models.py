from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


user_type = (
    ("patient", "Patient"), ("doctor", "Doctor"), ("organization", "Organization")
)

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    USERNAME_FIELD = 'email'
    email = models.EmailField(_('email address'), unique=True)

    type = models.CharField(max_length=20, choices=user_type, default="patient")

    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)



class MedicalRecord(models.Model):
    patient = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.PROTECT, related_name="patient")
    marital_status = models.CharField(max_length=20, null=True, blank=True)
    previous_doctor = models.ForeignKey(CustomUser ,null=True, blank=True, on_delete=models.PROTECT, verbose_name="previous or referring doctor", related_name="doctor")
    date_of_last_exam = models.DateField()
    problems = models.TextField(null=True, blank=True)
    blood_transfusion = models.BooleanField(default=False)
