import sys
import traceback
import os
import string
from django.db import transaction
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from app_finance.models import (
    Invoice
    )

from pyshorteners import Shortener 
import pyshorteners
from django.conf import settings
import stripe
from django.core.mail import EmailMessage

from django.contrib.auth import login  # Vishnupriya
from django.contrib.auth import logout  # Vishnupriya
from django.contrib.auth import authenticate  # Vishnupriya
def user_login(
    username: str,
    password: str,

):

    try:
        with transaction.atomic():
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active==True:
                    login(request,user)
            invoice_object=Invoice(
                client_name=name,
                project_name=project,
                email=email,
                amount=amount)
            invoice_object.save()
            payment_link=generate_payment_link(invoice_object.invoice_number)
            invoice_object.payment_link=payment_link
            invoice_object.save()


    except Exception as e:
        raise ValidationError(e)

