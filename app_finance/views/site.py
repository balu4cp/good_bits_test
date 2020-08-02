from django.shortcuts import render,reverse,redirect
from django.views import View
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login ,logout,authenticate

from django.contrib.auth.mixins import LoginRequiredMixin
from app_finance.models import (
    Invoice
    )

class LoginView(View):
    """
    Display the login form and handle the login action.
    """
    template_name = "login.html"

    def get(self, request):
        """Display login page. """
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('invoices'))
        return render(request, self.template_name)

    def post(self,request):
        """Perform logim action. """
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active==True:
                login(request,user)
                return HttpResponseRedirect(reverse('invoices'))
        return render( request,self.template_name,{ "error_msg": 'Invalid credentials.'})


class LogoutView(View):
    """Logout functionality of user."""
    template_name = "login.html"

    def get(self, request):
        logout(request)
        return render(request, self.template_name)


class InvoiceListView(LoginRequiredMixin,View):
    """ Display invoice list """
    template_name = "invoice_list.html"

    def get(self, request):
        return render(request, self.template_name)


class CreateInvoiceView(LoginRequiredMixin,View):
    """ Display invoice create page. """
    template_name = "invoice_create.html"

    def get(self, request):
        return render(request, self.template_name)


class InvoicePaymentView(View):
    """ Display payment page."""
    template_name = "invoice_payment.html"

    def get(self, request,id):
        invoice=Invoice.objects.filter(invoice_number=id)
        if invoice.exists():
            invoice=invoice[0]
            if invoice.status=='PENDING':
                return render(request, self.template_name,{'invoice':invoice})
            else:
                html = "<html><body><h1>Payment already completed</h1></body></html>"
                return HttpResponse(html)
        html = "<html><body><h1>Invalid page</h1></body></html>"
        return HttpResponse(html)


class PaymentSuccessView(View):
    """ Display success page."""
    template_name = "success.html"

    def get(self, request):
        return render(request, self.template_name)


class PaymentFailureView(View):
    """ Display success page."""
    template_name = "failure.html"

    def get(self, request):
        return render(request, self.template_name)


