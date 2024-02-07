# Generated by Django 4.2.7 on 2023-12-09 15:38

import datetime
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [

        migrations.CreateModel(
            name="Inventory",
            fields=[
                ("tag_number", models.CharField(
                    max_length=50, primary_key=True)),
                ("_id", models.UUIDField(
                    default=uuid.uuid4, editable=False, )),
                ("date", models.DateField(blank=True, null=True)),
                ("equipment", models.CharField(
                    blank=True, max_length=100, null=True)),
                (
                    "purpose",
                    models.CharField(
                        blank=True, default="Official", max_length=100, null=True
                    ),
                ),
                ("os", models.CharField(blank=True, max_length=100, null=True)),
                ("user", models.CharField(blank=True, max_length=100, null=True)),
                ("department", models.CharField(
                    blank=True, max_length=100, null=True)),
                (
                    "computer_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("model", models.CharField(blank=True, max_length=100, null=True)),
                ("color", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "serial_number",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("vendor", models.CharField(blank=True, max_length=100, null=True)),
                ("created_at", models.DateTimeField(
                    default=django.utils.timezone.now)),
                ("assigned", models.BooleanField(
                    blank=True, default=True, null=True)),
                (
                    "subsidiary",
                    models.CharField(
                        blank=True, default=None, max_length=30, null=True
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True, default=None, max_length=100, null=True
                    ),
                ),

            ],
        ),
    ]
