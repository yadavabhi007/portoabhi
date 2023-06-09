from .models import *
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail, send_mass_mail


@receiver(post_save, sender=SiteVisitedIPs)
def site_visiter_ip(sender, instance, created, **kwargs):
    if created:
        ip = instance.ip
        device = instance.device
        device_type = instance.device_type
        city = instance.city
        country = instance.country
        browser_type = instance.browser_type
        browser_version = instance.browser_version
        os_type = instance.os_type
        os_version = instance.os_version
        send_mail(
        'Abhishek Yadav Portfolio',
        f'Hey Abhishek Yadav! You have a visitor from: \n\nIP - {ip}\n\nDevice - {device}\n\nDevice Type - {device_type}\n\nCity - {city}\n\nCountry - {country}\n\nBrowser Type - {browser_type}\n\nBrowser Version - {browser_version}\n\nOS Type - {os_type}\n\nOS Version - {os_version}',
        'EMAIL_HOST_USER',
        ['abhishek8894434487@gmail.com'],
        fail_silently=False,
        )


@receiver(post_save, sender=Enquiry)
def enquiry_person_ip(sender, instance, created, **kwargs):
    if created:
        name = instance.name
        mobile_number = instance.mobile_number
        email = instance.email
        ip = instance.ip
        device = instance.device
        device_type = instance.device_type
        city = instance.city
        country = instance.country
        browser_type = instance.browser_type
        browser_version = instance.browser_version
        os_type = instance.os_type
        os_version = instance.os_version
        subject = instance.subject
        message = instance.message
        message1 = (
            "Abhishek Yadav Portfolio",
            f"Hey Abhishek Yadav! You have an enquiry from:\n\nName - {name}\n\nMobile Number - {mobile_number}\n\nEmail - {email}\n\nIP - {ip}\n\nDevice - {device}\n\nDevice Type - {device_type}\n\nCity - {city}\n\nCountry - {country}\n\nBrowser Type - {browser_type}\n\nBrowser Version - {browser_version}\n\nOS Type - {os_type}\n\nOS Version - {os_version}\n\nSubject - {subject}\n\nMessage - {message}",
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
