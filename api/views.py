# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model  # User = get_user_model()
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.permissions import (
    DjangoModelPermissionsOrAnonReadOnly,
)
from .filters import CustomUserFilter
from .serializers import UserSerializer, UserProfileSerializer
from drivingschool.models import UserProfile

CustomUser = get_user_model()


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CustomUserFilter


class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    # filterset_class = CustomUserFilter
