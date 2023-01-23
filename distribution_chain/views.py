from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from distribution_chain.filters import OwedFilter
from distribution_chain.models import ChainLink, Product
from distribution_chain.serializers import ChainLinkSerializer, ProductSerializer
from users.permissions import IsActivePermission


# Create your views here.

class ProductCreateView(generics.CreateAPIView):
    """Представление для создания продукта"""
    model = Product
    permission_classes = [IsAuthenticated, IsActivePermission]
    serializer_class = ProductSerializer


class ProductView(generics.RetrieveUpdateDestroyAPIView):
    """Представление для просмотра, обновления и удаления продукта"""
    model = Product
    permission_classes = [IsAuthenticated, IsActivePermission]
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter()


class ChainLinkCreateView(generics.CreateAPIView):
    """Представление для создания объекта сети"""
    model = ChainLink
    permission_classes = [IsAuthenticated, IsActivePermission]
    serializer_class = ChainLinkSerializer


class ChainLinkListView(generics.ListAPIView):
    """Представление для просмотра объектов сети в списке
    Примеры запросов для фильтрации
    1. По названию страны: distribution/link/list/?chainlink_country=Россия
    2. По id продукта: link/list/?products_product_id=1
    3. Задолженность выже среднего: link/list/?owed_above_avg=True"""
    model = ChainLink
    queryset = ChainLink.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = ChainLinkSerializer
    filterset_class = OwedFilter
    filterset_fields = ['chainlink_country', 'products_product_id', "owed"]


class ChainLinkView(generics.RetrieveUpdateDestroyAPIView):
    """Представление для просмотра, обновления и удаления объекта сети"""
    model = ChainLink
    permission_classes = [IsAuthenticated, IsActivePermission]
    serializer_class = ChainLinkSerializer

    def get_queryset(self):
        return ChainLink.objects.filter()
