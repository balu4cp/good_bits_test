from django.urls import path
from app_finance.views import site

urlpatterns = [
    path("", site.LoginView.as_view(), name="login",),
    path("logout", site.LogoutView.as_view(), name="logout",),
    path("invoices", site.InvoiceListView.as_view(), name="invoices",),
    path("create", site.CreateInvoiceView.as_view(), name="create_invoice",),
    path("payment/invoice/<id>", site.InvoicePaymentView.as_view(), name="invoice_payment",),
    path("success", site.PaymentSuccessView.as_view(), name="success",),
    path("failure", site.PaymentFailureView.as_view(), name="failure",),
]
