# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model  # User = get_user_model()
from django.db.models import Count
from django_filters import rest_framework as filters
from rest_framework import generics, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import (
    AllowAny,
    DjangoModelPermissions,
    DjangoModelPermissionsOrAnonReadOnly,
    IsAdminUser,
)
from rest_framework.response import Response

from drivingschool.models import Bar, Order, Reference, Stock
from drivingschool.serializers import (
    BarSerializer,
    OrderSerializer,
    ReferenceSerializer,
    StockSerializer,
)

from .filters import OrderFilter, ReferenceFilter, StockFilter
from .pagination import CustomPagination
from .serializers import RegisterSerializer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ReferenceViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ReferenceFilter


class BarViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Bar.objects.all()
    serializer_class = BarSerializer


class StockViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = StockSerializer
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = StockFilter


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [
        DjangoModelPermissions,
    ]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = OrderFilter
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(data=self.request.data)

    def perform_update(self, serializer):
        serializer.save(data=self.request.data)

    def get_permissions(self):
        global permission_classes
        if self.action == "list":
            permission_classes = [
                IsAdminUser,
            ]
        elif self.action == "create":
            permission_classes = [
                AllowAny,
            ]
        return [permission() for permission in permission_classes]


class StatisticsView(GenericAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        reference_count = Reference.objects.all().count()
        all_stock = (
            Stock.objects.extra(select={"bar__name": "bar"})
            .values("bar")
            .annotate(total=Count("bar"))
            .filter(total=reference_count)
        )
        all_stock = list(all_stock)

        miss_at_least_one = (
            Stock.objects.extra(select={"bar__name": "bar"})
            .values("bar")
            .annotate(total=Count("bar"))
            .filter(total__lt=reference_count)
        )
        miss_at_least_one = list(miss_at_least_one)
        missing_stock = []
        for bar in miss_at_least_one:
            missing_stock.append(
                {
                    "bar": bar["bar"],
                    "missing": Reference.objects.exclude(
                        id__in=Stock.objects.filter(bar=bar["bar"]).values_list(
                            "reference_id", flat=True
                        )
                    ).values_list("name", flat=True),
                }
            )

        return Response(
            {
                "all_stock": {
                    "description": "Liste des comptoirs qui ont toutes les références en stock",
                    "nombre": len(all_stock),
                    "bar": all_stock,
                },
                "miss_at_least_one": {
                    "description": "Liste des comptoirs qui ont au moins une référence épuisée",
                    "nombre": len(miss_at_least_one),
                    "bar": miss_at_least_one,
                },
                "list_of_missing_references": {
                    "description": "Liste des références manquantes par bar",
                    "nombre": len(missing_stock),
                    "references": {
                        "count": len(missing_stock),
                        "bar": missing_stock,
                    },
                },
            }
        )
