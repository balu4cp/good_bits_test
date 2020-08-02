from django.urls import path
from app_finance.views.apis import invoice_management

urlpatterns = [
    path("api/invoice/create", invoice_management.InvoiceCreateAPI.as_view(), name="create_invoice",),
    path("api/invoice/list/get", invoice_management.InvoiceListGetAPI.as_view(), name="invoice_list",),
    path("api/invoice/pay", invoice_management.PayInvoiceAPI.as_view(), name="invoice_pay",),
    path("api/invoice/paylink/email", invoice_management.EmailPaymentLinkAPI.as_view(), name="email_link",),

]
