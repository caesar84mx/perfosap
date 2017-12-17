from django.conf.urls import url

from . import views

app_name = 'almacen'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # Stored items related urls
    url(r'^storeditem/new$', views.new_storeditem, name='new-storeditem'),
    url(r'^storeditem/(?P<pk>\d+)/edit$', views.edit_storeditem, name='edit-storeditem'),
    url(r'^storeditem/(?P<pk>\d+)/delete$', views.DeleteStoredItem.as_view(), name='delete-storeditem'),
    url(r'^storeditems/$', views.StoredItemListView.as_view(), name='storeditems'),
    url(r'^storeditem/(?P<pk>\d+)$', views.StoredItemDetailView.as_view(), name='storeditem-detail'),
]
