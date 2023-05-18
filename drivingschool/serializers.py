# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model  # User = get_user_model()
from django.contrib.auth.password_validation import validate_password
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueValidator

from drivingschool.models import Bar, Order, OrderItem, Reference, Stock


class RegisterSerializer(serializers.ModelSerializer):
    User = get_user_model()
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        # model = User
        fields = (
            "username",
            "password",
            "password2",
            "email",
            "first_name",
            "last_name",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        del validated_data["password2"]
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class ReferenceSerializer(serializers.ModelSerializer):
    availability = serializers.SerializerMethodField()
    where = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.OBJECT)
    def get_availability(self, obj):
        return sum([s.stock for s in obj.stock_set.all()])

    @extend_schema_field(OpenApiTypes.OBJECT)
    def get_where(self, obj):
        return [s.bar.name for s in obj.stock_set.all()]

    class Meta:
        model = Reference
        fields = ("id", "ref", "name", "description", "availability", "where")


class BarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bar
        fields = ["id", "name"]


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ("reference", "bar", "stock")


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    order_items = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="order-item-detail"
    )

    def create(self, validated_data):
        data = validated_data.pop("data")
        order_items = data.get("items")
        bar = Bar.objects.get(id=data.get("bar"))
        order = Order.objects.create(**validated_data)
        for item in order_items:
            reference = Reference.objects.get(id=item["reference"])
            if reference is not None:
                OrderItem.objects.create(
                    bar=bar, order=order, reference=reference, count=item["count"]
                )
            return order

        return order

    class Meta:
        model = Order
        fields = ["id", "order_date", "order_items"]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
