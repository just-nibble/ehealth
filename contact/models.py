from django.db import models
from django.db.models.signals import post_save
from django.core.mail import EmailMessage
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)


@receiver(post_save, sender=Contact)
def send_contact_email(sender, instance, **kwargs):
    name = instance.name
    email_address = instance.email_address
    phone_number = instance.phone_number
    message = instance.message

    html_content = "Dear %s, we have recieved your opinion and would carefully go through it"
    message=EmailMessage(subject='New Opinion',body=html_content %(name),to=[email_address])
    message.content_subtype='html'
    message.send()
