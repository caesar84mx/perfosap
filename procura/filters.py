import django_filters
from django.forms import SelectDateWidget
from django.forms.fields import DateField

from procura.models import Contract, Provider, Item


class SelectDateField(DateField):
    widget = SelectDateWidget


class SelectDateFilter(django_filters.DateFilter):
    field_class = SelectDateField


class ContractFilter(django_filters.FilterSet):
    number = django_filters.CharFilter(label='Number:', lookup_expr='istartswith')
    name = django_filters.CharFilter(label='Name:', lookup_expr='icontains')
    start_date = SelectDateFilter(label='Starts:')
    expiry_date = SelectDateFilter(label='Ends:')

    class Meta:
        model = Contract
        fields = ['number', 'name', 'start_date', 'expiry_date', ]

class ProviderFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Name', lookup_expr='istartswith')
    rif = django_filters.CharFilter(label='RIF', lookup_expr='istartswith')
    contract = django_filters.CharFilter(name='contract__number', label='Contract No.', lookup_expr='istartswith')

    class Meta:
        model = Provider
        fields = ['name', 'rif', 'contract']


class ItemsNomenclatureFilter(django_filters.FilterSet):
    serial = django_filters.CharFilter(label='Serial No.', lookup_expr='istartswith')
    name = django_filters.CharFilter(label='Name', lookup_expr='icontains')
    manufacturer = django_filters.CharFilter(label='Manufacturer', lookup_expr='icontains')
    provider = django_filters.CharFilter(name='provider__name', label='Provider', lookup_expr='icontains')

    class Meta:
        model = Item
        fields = ['serial', 'name', 'manufacturer', 'provider']