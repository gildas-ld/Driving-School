from django.contrib.auth import get_user_model  # User = get_user_model()
from rest_framework import serializers
from drivingschool.models import UserProfile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name")
        read_only_fields = ("id",)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id", "user_type", "remaining_hours", "user_id")
        read_only_fields = ("id",)
