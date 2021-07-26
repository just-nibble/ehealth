from django.db import models
from accounts.models import CustomUser
from django.db.models.signals import post_save
from django.core.mail import EmailMessage
from django.dispatch import receiver
# Create your models here.


class Appointment(models.Model):
    appointment_status = (("pending", "Pending"), ("accept", "Accept"), ("cancel", "Cancel"),  )
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name="patient_for_appointment")
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name="doctor_booked")
    book_date = models.DateTimeField(verbose_name="booking date", null=True, blank=True, unique=True)
    appt_date = models.DateTimeField(verbose_name="appointment date", null=True, blank=True, auto_now_add=True)
    purpose = models.CharField(max_length=300, null=True, blank=True)
    type = models.CharField(max_length=300, null=True, blank=True)
    paid_amount = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=7, blank=True, choices=appointment_status)

    def __str__(self):
        return str(self.patient)

    class Meta:
        ordering = ["appt_date"]

@receiver(post_save,sender=Appointment)
def send_doctor_notification(sender, instance, **kwargs):
    status = instance.status
    patient = instance.patient.name
    doctor_email = instance.doctor.email
    patient_email = instance.patient.email
    phone = instance.patient.phone
    date = instance.appt_date
    html_content = "You have a new appointment scheduled for %s by %s with details: %s %s , please review in dashboard"
    message=EmailMessage(subject='New Appointment',body=html_content %(date,patient,patient_email,phone ),to=[doctor_email])
    message.content_subtype='html'
    message.send()

@receiver(post_save,sender=Appointment)
def send_patient_notification(sender, instance, **kwargs):
    status = instance.status
    patient = instance.patient.name
    doctor_name = instance.doctor.name
    patient_email = instance.patient.email
    phone = instance.patient.phone
    date = instance.appt_date
    html_content = "You scheduled a new appointment for %s by %s with %s , please review in dashboard"
    message=EmailMessage(subject='New Appointment Created By You',body=html_content %(date,patient,doctor_name),to=[patient_email])
    message.content_subtype='html'
    message.send()
