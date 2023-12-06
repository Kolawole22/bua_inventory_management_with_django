# Generated by Django 4.2.7 on 2023-12-01 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventorydb", "0005_alter_inventory_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inventory",
            name="color",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="computer_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="department",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="equipment",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="model",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="os",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="purpose",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="serial_number",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="user",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="vendor",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
