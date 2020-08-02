from rest_framework import serializers

class InvoiceCreateSerializer(serializers.Serializer):
    """Serializer to create invoice."""

    name = serializers.CharField()
    project = serializers.CharField()
    email = serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)


class InvoiceListSerializer(serializers.Serializer):
    """Serializer to get invoice list."""

    invoice_number = serializers.CharField()
    client_name = serializers.CharField()
    project_name = serializers.CharField()
    email = serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    payment_link = serializers.CharField()
    status = serializers.CharField()


class InvoiceDetialSerializer(serializers.Serializer):
    """Serializer to get the  invoice details."""

    invoice_number = serializers.CharField()
    client_name = serializers.CharField()
    project_name = serializers.CharField()
    email = serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    payment_link = serializers.CharField()


class InvoicePaymentSerializer(serializers.Serializer):
    """Serializer to pay amount of invoice."""

    invoice_number = serializers.CharField()
    stripeToken = serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
