from django.db import models
from django.contrib.auth.models import User

class TimeStamp(models.Model):
    """Model definition for TimeStamp.
       Abstract model that can be inhertied by all other models.
       Refers to fields present in all models.
    """

    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for TimeStamp."""

        abstract = True
        verbose_name = "TimeStamp"
        verbose_name_plural = "TimeStamps"