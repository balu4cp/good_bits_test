from django.db import models
from app_finance .models import TimeStamp

class Invoice(models.Model):

    """Model definition for TimeStamp.
       Abstract model that can be inhertied by all other models.
       Refers to fields present in all models.
    """

    def generate_invoice_number():
        count = Invoice.objects.all().count() + 1
        return "INV" + str(count).zfill(5)

    invoice_number = models.CharField(max_length=10,default=generate_invoice_number,unique=True)
    client_name = models.CharField(max_length=30)
    project_name = models.CharField(max_length=50)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_link = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=20,default='PENDING')
    transaction_id = models.TextField(null=True,blank=True)

    class Meta:
        """Meta definition for Invoice."""

        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

    def __str__(self):
        """Unicode representation of Invoice."""
        return str(self.id)

    def save(self, *args, **kwargs):
        """Overriding the default save method."""
        self.full_clean()
        return super().save(*args, **kwargs)






