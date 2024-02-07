from datetime import datetime
from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
import uuid
import random


# Create your models here.


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)


class Inventory(models.Model):
    # id = models.AutoField(primary_key=True)
    _id = models.UUIDField(
        default=uuid.uuid4, editable=False)
    tag_number = models.CharField(
        max_length=50, primary_key=True)
    date = models.DateField(null=True, blank=True)
    equipment = models.CharField(max_length=100, null=True, blank=True)
    purpose = models.CharField(
        max_length=100, null=True, blank=True, default='Official')
    os = models.CharField(max_length=100, null=True, blank=True)
    user = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    computer_name = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    serial_number = models.CharField(max_length=100, null=True, blank=True)
    vendor = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(
        default=timezone.now)
    assigned = models.BooleanField(default=True, null=True, blank=True)
    subsidiary = models.CharField(
        max_length=30, null=True, blank=True, default=None)
    location = models.CharField(
        max_length=100, blank=True, null=True, default=None)
    email = models.EmailField(null=True, blank=True)
    cost_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=None, blank=True)

    def __str__(self):
        return f"{self.equipment} - {self.model} - {self.user}"


class ActionLog(models.Model):
    # id = models.UUIDField(
    #     default=uuid.uuid4, editable=False)
    # id = models.AutoField()
    tag_number_key = models.ForeignKey(
        Inventory, on_delete=models.CASCADE, null=True)
    equipment = models.CharField(max_length=100, null=True, blank=True)
    # purpose = models.CharField(
    # max_length=100, null=True, blank=True, default='Official')
    # os = models.CharField(max_length=100, null=True, blank=True)
    retrieved_from = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    # computer_name = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    # color = models.CharField(max_length=100, null=True, blank=True)
    serial_number = models.CharField(max_length=100, null=True, blank=True)
    vendor = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    # assigned = models.BooleanField(default=True, null=True, blank=True)
    subsidiary = models.CharField(
        max_length=30, null=True, blank=True, default=None)
    location = models.CharField(
        max_length=100, blank=True, null=True, default=None)
    remark = models.CharField(max_length=100, null=True, default=None)
    action_type = models.CharField(max_length=20, blank=True, null=True)
    date_retrieved = models.DateField(null=True, blank=True,)


class APILog(models.Model):
    API_TYPES = (
        ('POST', 'POST'),
        ('PATCH', 'PATCH'),
        ('PUT', 'PUT'),
    )

    api_type = models.CharField(max_length=10, choices=API_TYPES)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    changes_made = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.api_type} API Log - {self.created_at}"
