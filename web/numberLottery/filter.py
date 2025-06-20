from django_filters import rest_framework as filters

#Project
from numberLottery.models import NumberLottery, PrototypeNumberLottery

class CharIgnoreNoneFilter(filters.CharFilter):
    """
    Filter that ignores if value is 'none'
    """
    empty_value = 'none'

    def filter(self, qs, value):
        if value != self.empty_value:
            return super().filter(qs, value)
        return qs.distinct() if self.distinct else qs

class NumberListFilter(filters.FilterSet):
    shop    = filters.CharFilter(field_name="idShop", lookup_expr='exact')
    number  = CharIgnoreNoneFilter(field_name="numberLottery", lookup_expr='icontains')

    class Meta:
        model = NumberLottery
        fields = ['numberLottery', 'shop']

class NumberMatchingListFilter(filters.FilterSet):
    number = filters.CharFilter(method='filter_by_number')
    numberLottery = filters.CharFilter(method='filter_by_number')

    class Meta:
        model = PrototypeNumberLottery
        fields = []

    def filter_by_number(self, queryset, name, value):
        return queryset.filter(numberLottery__icontains=value)