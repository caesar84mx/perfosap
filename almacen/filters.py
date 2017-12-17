import django_filters

from almacen.models import StoredItem


class StoredItemsFilter(django_filters.FilterSet):
    item_serial = django_filters.CharFilter(name='item__serial', label='Serial No.', lookup_expr='istartswith')
    item_name = django_filters.CharFilter(name='item__name', label='Name', lookup_expr='icontains')
    item_manufacturer = django_filters.CharFilter(name='item__manufacturer', label='Manufacturer', lookup_expr='icontains')
    item_provider = django_filters.CharFilter(name='item__provider__name', label='Provider', lookup_expr='icontains')

    class Meta:
        model = StoredItem
        fields = ['item_serial', 'item_name', 'item_manufacturer', 'item_provider']