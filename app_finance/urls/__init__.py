from django.conf.urls import url, include

urlpatterns = [
    url("", include("app_finance.urls.site")),
    url("", include("app_finance.urls.invoice_management")),
]