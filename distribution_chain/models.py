from django.db import models
from django.db.models import ManyToManyField
from django.utils import timezone

from users.models import User


# Create your models here.

class Product(models.Model):
    """Модель представления продукта"""
    name = models.CharField(max_length=255, verbose_name="Название")
    model = models.CharField(max_length=255, verbose_name="Модель")
    release_date = models.DateTimeField(verbose_name="Дата выхода на рынок", default=timezone.now)

    def __str__(self):
        return self.name


class ChainLink(models.Model):
    """Модель представления объекта сети"""
    class Level(models.IntegerChoices):
        FACTORY = 0, "Завод"
        DISTRIBUTOR = 1, "Дистрибьютор"
        DEALERSHIP = 2, "Дилерский центр"
        RETAIL_CHAIN = 3, "Крупная розничная сеть"
        SOLE_PROPRIETOR = 4, "Индивидуальный предприниматель"

    name = models.CharField(max_length=255, verbose_name="Название")
    level = models.PositiveSmallIntegerField(choices=Level.choices, verbose_name="Уровень")
    email = models.EmailField(verbose_name="Электронная почта", null=True, blank=True)
    country = models.CharField(max_length=255, verbose_name="Страна", null=True, blank=True)
    city = models.CharField(max_length=255, verbose_name="Город", null=True, blank=True)
    street = models.CharField(max_length=255, verbose_name="Улица", null=True, blank=True)
    street_number = models.CharField(max_length=255, verbose_name="Номер дома", null=True, blank=True)
    employees = ManyToManyField(User, verbose_name="Сотрудники", blank=True)
    products = ManyToManyField(Product, verbose_name="Продукт", blank=True)
    owed = models.DecimalField(max_digits=19, decimal_places=2, verbose_name="Задолженность", default=0.00)
    supplier = models.ForeignKey("self", verbose_name="Поставщик", on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name
