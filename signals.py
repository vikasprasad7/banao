import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        # Call your Serverless Email API
        payload = {
            "email": instance.email,
            "username": instance.username,
            "role": instance.role
        }
        # In local testing, this points to your serverless-offline endpoint
        requests.post("http://localhost:3000/dev/sendEmail", json=payload)
