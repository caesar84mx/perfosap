from django.conf.urls import url

import procura.views
from . import views

app_name = 'procura'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # Providers related urls
    url(r'^provider/new/$', procura.views.new_provider, name='new-provider'),
    url(r'^provider/(?P<pk>\d+)/edit$', procura.views.edit_provider, name='edit-provider'),
    url(r'^provider/(?P<pk>\d+)/delete$', procura.views.DeleteProvider.as_view(), name='delete-provider'),
    url(r'^providers/$', procura.views.provider_filter, name='providers'),
    url(r'^provider/(?P<pk>\d+)$', procura.views.ProviderDetailView.as_view(), name='provider-detail'),
    # Items nomenclature related urls
    url(r'^item/new$', procura.views.CreateItem.as_view(), name='new-item'),
    url(r'^item/(?P<pk>\d+)/edit$', procura.views.UpdateItem.as_view(), name='edit-item'),
    url(r'^item/(?P<pk>\d+)/delete$', procura.views.DeleteItem.as_view(), name='delete-item'),
    url(r'^items/$', procura.views.item_filter, name='items'),
    url(r'^item/(?P<pk>\d+)$', procura.views.ItemDetailView.as_view(), name='item-detail'),
    # Contracts related urls
    url(r'^contracts$', procura.views.contract_filter, name='contracts'),
    url(r'^contract/(?P<pk>\d+)$', procura.views.ContractDetailView.as_view(), name='contract-detail'),
    url(r'^contract/(?P<pk>\d+)/edit$', procura.views.edit_contract, name='edit-contract'),
    url(r'^contract/new$', procura.views.new_contract, name='new-contract'),
    url(r'^contract/(?P<pk>\d+)/delete$', procura.views.DeleteContract.as_view(), name='delete-contract'),
]
