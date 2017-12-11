from django.conf.urls import url

from . import views

app_name = 'almacen'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # Providers related urls
    url(r'^provider/new/$', views.new_provider, name='new-provider'),
    url(r'^provider/(?P<pk>\d+)/edit$', views.edit_provider, name='edit-provider'),
    url(r'^provider/(?P<pk>\d+)/delete$', views.DeleteProvider.as_view(), name='delete-provider'),
    url(r'^providers/$', views.ProviderListView.as_view(), name='providers'),
    url(r'^provider/(?P<pk>\d+)$', views.ProviderDetailView.as_view(), name='provider-detail'),
    # Items nomenclature related urls
    url(r'^item/new$', views.CreateItem.as_view(), name='new-item'),
    url(r'^item/(?P<pk>\d+)/edit$', views.UpdateItem.as_view(), name='edit-item'),
    url(r'^item/(?P<pk>\d+)/delete$', views.DeleteItem.as_view(), name='delete-item'),
    url(r'^items/$', views.ItemListView.as_view(), name='items'),
    url(r'^item/(?P<pk>\d+)$', views.ItemDetailView.as_view(), name='item-detail'),
    # Stored items related urls
    url(r'^storeditem/new$', views.new_storeditem, name='new-storeditem'),
    url(r'^storeditem/(?P<pk>\d+)/edit$', views.edit_storeditem, name='edit-storeditem'),
    url(r'^storeditem/(?P<pk>\d+)/delete$', views.DeleteStoredItem.as_view(), name='delete-storeditem'),
    url(r'^storeditems/$', views.StoredItemListView.as_view(), name='storeditems'),
    url(r'^storeditem/(?P<pk>\d+)$', views.StoredItemDetailView.as_view(), name='storeditem-detail'),
    # Contracts related urls
    url(r'^contracts/$', views.ContractListView.as_view(), name='contracts'),
    url(r'^contract/(?P<pk>\d+)$', views.ContractDetailView.as_view(), name='contract-detail'),
    url(r'^contract/(?P<pk>\d+)/edit$', views.edit_contract, name='edit-contract'),
    url(r'^contract/new$', views.new_contract, name='new-contract'),
    url(r'^contract/(?P<pk>\d+)/delete$', views.DeleteContract.as_view(), name='delete-contract'),
]
