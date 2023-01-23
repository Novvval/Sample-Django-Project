from rest_framework import serializers

from distribution_chain.models import Product, ChainLink
from users.models import User


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для представления о продуктах"""
    class Meta:
        model = Product
        read_only_fields = ["id"]
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    """Сериализатор для сотрудников"""
    class Meta:
        model = User
        read_only_fields = ["id", "is_active", "is_staff"]
        fields = ["id", "is_active", "is_staff", "username", "first_name", "last_name"]


class ChainLinkSerializer(serializers.ModelSerializer):
    """Сериализатор для объекта сети"""
    products = ProductSerializer(many=True)
    employees = EmployeeSerializer(many=True)

    class Meta:
        model = ChainLink
        read_only_fields = ["created", "id", "owed"]
        fields = "__all__"
