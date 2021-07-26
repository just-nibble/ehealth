from django.db import models
from accounts.models import CustomUser
# Create your models here.


class Pricing(models.Model):
    treatment = models.CharField(max_length=500, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.treatment)
