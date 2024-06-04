from django.forms import ValidationError
from rest_framework import serializers, viewsets
# Assuming your models are in the same directory
from .models import Inventory
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        # fields = ['id', 'date', 'equipment', 'purpose', 'os', 'user',
        #           'department', 'computer_name', 'model', 'color', 'serial_number', 'vendor']
        user = serializers.CharField(allow_null=True, required=False)
        email = serializers.EmailField(allow_null=True, required=False)
        fields = '__all__'

        # def create(self, validated_data):
        #     user = self.context['request'].User

        #     if user.is_annymous:
        #         raise PermisionDenied(
        #             'You must be'
        #         )




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # serializer_class =


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(
            username=data.get('username'), password=data.get('password'))
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        return user


# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = '__all__'


# class UserSerializer(serializers.ModelSerializer):
#     profile = UserProfileSerializer()

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'profile']


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email']
