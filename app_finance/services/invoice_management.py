import sys
import traceback
import os
import string

from django.db import transaction
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import EmailMessage

from app_finance.models import (
    Invoice
    )

import pyshorteners
import stripe

def create_invoice(name: str, project: str,email: str,amount: float,):
    """Creatton of invoice."""
    try:
        with transaction.atomic():
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

def get_invoice_list():
    """Get the list of all invoices."""
    try:
        invoices=Invoice.objects.all().order_by('-id')
        return invoices
    except Exception as e:
        raise ValidationError(e)

def generate_payment_link(invoice_number):
    """URL shortening using bit.ly """
    try:
        url_shortner = pyshorteners.Shortener(api_key=settings.BITLY_ACCESS_TOKEN)
        link=url_shortner.bitly.short('http://'+settings.EMAIL_URL+'/payment/invoice/'+invoice_number)
        return link
    except Exception as e:
        raise ValidationError(e)

def pay_invoice(amount:float,stripeToken:str,invoice_number:str):
    """ collecting invoice amount using stripe."""
    try:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        with transaction.atomic():
            try:
                charge=stripe.Charge.create(
                  amount=int(amount)*100,
                  currency="inr",
                  source=stripeToken,
                  description="Payement of "+invoice_number,
                )
            except stripe.error.StripeError as e:
                raise ValidationError(e)
            invoice=Invoice.objects.get(invoice_number=invoice_number)
            invoice.status='COMPLETED'
            invoice.transaction_id=charge.id
            invoice.save()
    except Exception as e:
        raise ValidationError(e)

def send_payment_link_mail(invoice_number):
    """ send payment_link as email to customer."""
    try:
        invoice=Invoice.objects.get(invoice_number=invoice_number)
        subject = 'Payment link'
        content = ''
        content += "<br>Please use below link to complete paymentt."
        content += "<br><a target='_blank' href=\""
        content += invoice.payment_link
        content += "\"><br>"+invoice.payment_link+"</a><br>"
        content += '<br><br />'
        from_email = settings.EMAIL_HOST_USER
        e_msg = EmailMessage(subject, content, from_email, [invoice.email])
        e_msg.content_subtype = "html"
        e_msg.send()
    except Exception as e:
        raise ValidationError(e)




