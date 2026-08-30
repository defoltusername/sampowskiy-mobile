from rest_framework import serializers
from .models import User, Address


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "phone",
            "avatar",
        ]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "user",
            "country",
            "city",
            "street",
            "house",
            "apartment",
            "postal_code",
            "is_default",
        ]
