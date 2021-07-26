from django.db import models
from accounts.models import CustomUser
# Create your models here.


class Favourites(models.Model):
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
