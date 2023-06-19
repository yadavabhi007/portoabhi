from .models import *
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail, send_mass_mail



@receiver(post_save, sender=Enquiry)
def enquiry_person_ip(sender, instance, created, **kwargs):
    if created:
        name = instance.name
        mobile_number = instance.mobile_number
        email = instance.email
        ip = instance.ip
        city = instance.city
        country = instance.country
        device_type = instance.device_type
        os_type = instance.os_type
        subject = instance.subject
        message = instance.message
        message1 = (
            "Abhishek Yadav Portfolio",
            f"Hey Abhishek Yadav! You have an enquiry from:\n\nName - {name}\n\nMobile Number - {mobile_number}\n\nEmail - {email}\n\nIP - {ip}\n\nCity - {city}\n\nCountry - {country}\n\nDevice Type - {device_type}\n\nOS Type - {os_type}\n\nSubject - {subject}\n\nMessage - {message}",
            "EMAIL_HOST_USER",
            ["abhishek8894434487@gmail.com"],
        )
        message2 = (
            "Abhishek Yadav Portfolio",
            f"Hey {name}!\n\nThanks For Contacting Me. I Will Revert Back To You Soon.",
            "EMAIL_HOST_USER",
            [email],
        )
        send_mass_mail((message1, message2), fail_silently=False)
