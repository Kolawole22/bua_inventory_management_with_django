from datetime import datetime
from django.db import models

# Create your models here.


class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(null=True, blank=True)
    equipment = models.CharField(max_length=100, null=True, blank=True)
    purpose = models.CharField(max_length=100, null=True, blank=True)
    os = models.CharField(max_length=100, null=True, blank=True)
    user = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    computer_name = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    serial_number = models.CharField(max_length=100, null=True, blank=True)
    vendor = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    assigned = models.BooleanField(default=True)

    # date_received = models.DateField()
    # date_deployed = models.DateField()

    def __str__(self):
        return f"{self.equipment} - {self.model}"
