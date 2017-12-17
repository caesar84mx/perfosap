import django_filters

from procura.models import Contract


class ContractFilter(django_filters.FilterSet):
    number = django_filters.CharFilter(label='Number:', lookup_expr='istartswith')
    name = django_filters.CharFilter(label='Name:', lookup_expr='icontains')
    start_date = django_filters.DateFilter(label='Starts:', lookup_expr='iexact')
    expiry_date = django_filters.DateFilter(label='Ends:', lookup_expr='iexact')

    class Meta:
        model = Contract
        fields = ['number', 'name', 'start_date', 'expiry_date', ]