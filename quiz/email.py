import random

from django.core.mail import send_mail

from quiz.models import User
from root import settings


def send_otp_via_email(email, otp):
    subject = f"Your account verification email"
    massage = f"Your otp is {otp}"
    email_from = settings.EMAIL_HOST
    send_mail(subject, massage, email_from, [email])
    user_odj = User.objects.get(email=email)
    user_odj.otp = otp
    user_odj.save()
