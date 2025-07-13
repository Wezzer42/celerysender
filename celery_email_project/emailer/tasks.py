from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email_task(email, subject, message):
    send_mail(
        subject,
        message,
        "noreply@yourdomain.com",  # FROM email
        [email],
        fail_silently=False,
    )
