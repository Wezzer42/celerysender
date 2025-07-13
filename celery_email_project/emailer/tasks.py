from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email_task(email, subject, message):
    send_mail(
        subject,
        message,
        None,  # From email (будет DEFAULT_FROM_EMAIL)
        [email],
        fail_silently=False,
    )
