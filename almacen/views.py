from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import generic
# Create your views here.
from django.views.generic import DeleteView

from almacen.models import StoredItem
from procura.models import Provider
from .forms import NewOrEditStoredItemForm
from .services import store_item


def index(request):
    stored_items_num = len([x for x in StoredItem.objects.all() if x.quantity > 0])
    providers_num = Provider.objects.all().count()

    return render(request,
                  'almacen_static_pages/index.html',
                  context={
                      'stored_items_num': stored_items_num,
                      'providers_num': providers_num
                  })


# Stored items related ---------------------------------------------------------------------
@login_required
def new_storeditem(request):
    if request.method == 'POST':
        form = NewOrEditStoredItemForm(request.POST)
        if form.is_valid():
            storeditem = StoredItem()
            storeditem.item = form.cleaned_data['item']
            storeditem.quantity = form.cleaned_data['quantity']
            store_item(storeditem)
            return HttpResponseRedirect(reverse('almacen:storeditems'))
    else:
        form = NewOrEditStoredItemForm()

    return render(request, 'almacen/storeditem_new.html', {'form':form})


@login_required
def edit_storeditem(request, pk):
    storeditem = get_object_or_404(StoredItem, pk=pk)
    if request.method == 'POST':
        form = NewOrEditStoredItemForm(request.POST)
        if form.is_valid():
            storeditem.item = form.cleaned_data['item']
            storeditem.quantity = form.cleaned_data['quantity']
            storeditem.save()
            return HttpResponseRedirect(reverse('almacen:storeditem-detail', args=[pk]))
    else:
        form = NewOrEditStoredItemForm(initial={
            'item': storeditem.item,
            'quantity': storeditem.quantity,
        })

    return render(request, 'almacen/storeditem_edit.html', {'form': form, 'storeditem': storeditem})


@method_decorator(login_required, name='dispatch')
class DeleteStoredItem(DeleteView):
    model = StoredItem
    success_url = reverse_lazy('almacen:storeditems')


@method_decorator(login_required, name='dispatch')
class StoredItemListView(generic.ListView):
    model = StoredItem
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
class StoredItemDetailView(generic.DetailView):
    model = StoredItem
