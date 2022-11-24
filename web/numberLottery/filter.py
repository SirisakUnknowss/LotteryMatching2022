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
    shop    = filters.ModelMultipleChoiceFilter(field_name="idShop", queryset=NumberLottery.objects.all(), to_field_name='idShop')
    number  = CharIgnoreNoneFilter(field_name="numberLottery", lookup_expr='icontains')

    class Meta:
        model = NumberLottery
        fields = ['numberLottery']

class NumberMatchingListFilter(filters.FilterSet):
    number  = CharIgnoreNoneFilter(field_name="numberLottery", lookup_expr='icontains')

    class Meta:
        model = PrototypeNumberLottery
        fields = ['numberLottery']