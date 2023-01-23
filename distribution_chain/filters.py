import django_filters
from django.db.models import Avg
from django_filters.rest_framework import FilterSet

from distribution_chain.models import ChainLink


class OwedFilter(FilterSet):
    """Фильтрация объектов с задолженностью выше среднего среди всех объектов"""
    owed_above_avg = django_filters.BooleanFilter(field_name="owed", method="filter_above_avg")

    class Meta:
        model = ChainLink
        fields = ["owed"]

    def filter_above_avg(self, queryset, name, value):
        average = queryset.aggregate(Avg("owed"))["owed__avg"]
        return queryset.filter(owed__gt=average)
