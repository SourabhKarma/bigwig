
import random 
from django.core.mail import send_mail
from django.conf import settings
from .models import User


def send_mail_otp(email):
        subject = 'bigwig'
        otp =  random.randint(100000 ,999999)
        # user = User.objects.get(username = )

        message = f'Your  OTP is - {otp}' 
        email_from = settings.EMAIL_HOST
        # recipient_list = [User.email, ]
        send_mail( subject, message, email_from, [email] )
        user_obj = User.objects.get(email= email)

        user_obj.otp = otp
        # user_obj.password = otp

        user_obj.save()

