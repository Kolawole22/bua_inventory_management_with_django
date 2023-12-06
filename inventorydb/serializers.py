from rest_framework import serializers
from .models import Inventory  # Assuming your models are in the same directory


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = fields = ['id', 'date', 'equipment', 'purpose', 'os', 'user',
                           'department', 'computer_name', 'model', 'color', 'serial_number', 'vendor']
