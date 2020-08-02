from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from app_finance.serializers.invoice_management import (
    InvoiceCreateSerializer,
    InvoiceListSerializer,
    InvoiceDetialSerializer,
    InvoicePaymentSerializer
)

from app_finance.services.invoice_management import (
    create_invoice,
    get_invoice_list,
    pay_invoice,
    send_payment_link_mail
)

class InvoiceListGetAPI(APIView):
    """API for getting invoice list."""
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        invoices = get_invoice_list()
        serializer = InvoiceListSerializer(invoices, many=True)
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)


class InvoiceCreateAPI(APIView):
    """API for creating new invoice."""
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = InvoiceCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_invoice(**serializer.validated_data)
        return Response(status=status.HTTP_200_OK, data="Invoice Created successfully.")


class PayInvoiceAPI(APIView):
    """API for making payment of invoice."""
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = InvoicePaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pay_invoice(**serializer.validated_data)
        return Response(status=status.HTTP_200_OK, data="Invoice payment done successfully.")


class EmailPaymentLinkAPI(APIView):
    """API for sending payment link as email to customer."""
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        invoice_number=request.query_params.get("invoice_number")
        details = send_payment_link_mail(invoice_number)
        return Response(status=status.HTTP_201_CREATED, data='Email  sent successfully')