# Generated by Django 4.2.7 on 2023-12-01 09:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("inventorydb", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="inventory",
            name="serial_number",
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]