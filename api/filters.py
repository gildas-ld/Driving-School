from django_filters import rest_framework as filters
from django.contrib.auth import get_user_model  # User = get_user_model()

CustomUser = get_user_model()


class CustomUserFilter(filters.FilterSet):
    username = filters.CharFilter(lookup_expr="icontains")
    email = filters.CharFilter(lookup_expr="icontains")
    first_name = filters.CharFilter(lookup_expr="icontains")
    last_name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = CustomUser
        fields = ["username", "email", "first_name", "last_name"]
