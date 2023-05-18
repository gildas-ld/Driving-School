from django_filters import rest_framework as filters
from .models import Order, Reference, Stock


class ReferenceFilter(filters.FilterSet):
    id = filters.NumberFilter()
    ref = filters.CharFilter(lookup_expr="icontains")
    name = filters.CharFilter(lookup_expr="icontains")
    description = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Reference
        fields = ["id", "ref", "name", "description"]


class StockFilter(filters.FilterSet):
    id = filters.NumberFilter()
    reference = filters.NumberFilter()
    bar = filters.NumberFilter()
    stock = filters.NumberFilter()

    class Meta:
        model = Stock
        fields = ("id", "reference", "bar", "stock")


class OrderFilter(filters.FilterSet):
    id = filters.NumberFilter()
    order_date = filters.DateFilter()

    class Meta:
        model = Order
        fields = ("id", "order_date")
