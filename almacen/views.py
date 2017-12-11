import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import generic
# Create your views here.
from django.views.generic import DeleteView, CreateView, UpdateView

from almacen.models import Contract, StoredItem, Provider, Item
from .forms import EditContractForm, NewContractForm, NewOrEditProviderForm, NewOrEditStoredItemForm


def index(request):
    stored_items_num = len([x for x in StoredItem.objects.all() if x.quantity > 0])
    providers_num = Provider.objects.all().count()

    return render(request,
                  'index.html',
                  context={
                      'stored_items_num': stored_items_num,
                      'providers_num': providers_num
                  })


# Contract related ------------------------------------------------------------------------
@permission_required('almacen.create_contract')
def new_contract(request):
    if request.method == 'POST':
        form = NewContractForm(request.POST)
        if form.is_valid():
            contract = Contract()
            contract.number = form.cleaned_data['number']
            contract.name = form.cleaned_data['name']
            contract.description = form.cleaned_data['description']
            contract.start_date = form.cleaned_data['start_date']
            contract.expiry_date = form.cleaned_data['expiry_date']
            contract.save()
            return HttpResponseRedirect(reverse('almacen:contracts'))
    else:
        today = datetime.date.today()
        form = NewContractForm(initial={
            'start_date': today,
            'expiry_date': datetime.date(today.year + 1, today.month, today.day)
        })
        return render(request, 'almacen/contract_new.html', {'form':form})


@permission_required('almacen.change_contract')
def edit_contract(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        form = EditContractForm(request.POST)
        if form.is_valid():
            contract.description = form.cleaned_data['description']
            contract.start_date = form.cleaned_data['start_date']
            contract.expiry_date = form.cleaned_data['expiry_date']
            contract.save()
            return HttpResponseRedirect(reverse('almacen:contract-detail', args=[pk]))
    else:
        today = datetime.date.today()
        form = EditContractForm(initial={
            'description': contract.description,
            'start_date': today,
            'expiry_date': contract.expiry_date
        })
    return render(request, 'almacen/contract_edit.html', {'form': form, 'contract': contract})


class DeleteContract(DeleteView):
    model = Contract
    success_url = reverse_lazy('almacen:contracts')


@method_decorator(login_required, name='dispatch')
class ContractListView(generic.ListView):
    model = Contract
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
class ContractDetailView(generic.DetailView):
    model = Contract


# Provider related ------------------------------------------------------------------------
# @method_decorator(login_required, name='dispatch')
# class CreateProvider(CreateView):
#     model = Provider
#     fields = '__all__'

def new_provider(request):
    if request.method == 'POST':
        form = NewOrEditProviderForm(request.POST)
        if form.is_valid():
            provider = Provider()
            provider.name = form.cleaned_data['name']
            provider.rif = form.cleaned_data['rif']
            provider.address = form.cleaned_data['address']
            provider.phone_num = form.cleaned_data['phone_num']
            provider.contract = form.cleaned_data['contract']
            provider.save()
            return HttpResponseRedirect(reverse('almacen:providers'))
    else:
        form = NewOrEditProviderForm()

    return render(request, 'almacen/provider_new.html', {'form':form})


def edit_provider(request, pk):
    provider = get_object_or_404(Provider, pk=pk)
    if request.method == 'POST':
        form = NewOrEditProviderForm(request.POST)
        if form.is_valid():
            provider.name = form.cleaned_data['name']
            provider.rif = form.cleaned_data['rif']
            provider.address = form.cleaned_data['address']
            provider.phone_num = form.cleaned_data['phone_num']
            provider.contract = form.cleaned_data['contract']
            provider.save()
            return HttpResponseRedirect(reverse('almacen:provider-detail', args=[pk]))
    else:
        form = NewOrEditProviderForm(initial={
            'name': provider.name,
            'rif': provider.rif,
            'address': provider.address,
            'phone_num': provider.phone_num,
            'contract': provider.contract
        })

    return render(request, 'almacen/provider_edit.html', {'form': form, 'provider': provider})

# @method_decorator(login_required, name='dispatch')
# class UpdateProvider(UpdateView):
#     model = Provider
#     fields = '__all__'


@method_decorator(login_required, name='dispatch')
class DeleteProvider(DeleteView):
    model = Provider
    success_url = reverse_lazy('almacen:providers')


@method_decorator(login_required, name='dispatch')
class ProviderListView(generic.ListView):
    model = Provider
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
class ProviderDetailView(generic.DetailView):
    model = Provider


# Items nomenclature related --------------------------------------------------------------
@method_decorator(login_required, name='dispatch')
class CreateItem(CreateView):
    model = Item
    fields = '__all__'


@method_decorator(login_required, name='dispatch')
class UpdateItem(UpdateView):
    model = Item
    fields = '__all__'


@method_decorator(login_required, name='dispatch')
class DeleteItem(DeleteView):
    model = Item
    success_url = reverse_lazy('almacen:items')


@method_decorator(login_required, name='dispatch')
class ItemListView(generic.ListView):
    model = Item
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
class ItemDetailView(generic.DetailView):
    model = Item


# Stored items related ---------------------------------------------------------------------
def new_storeditem(request):
    if request.method == 'POST':
        form = NewOrEditStoredItemForm(request.POST)
        if form.is_valid():
            storeditem = StoredItem()
            storeditem.item = form.cleaned_data['item']
            storeditem.quantity = form.cleaned_data['quantity']
            storeditem.save()
            return HttpResponseRedirect(reverse('almacen:storeditems'))
    else:
        form = NewOrEditStoredItemForm()

    return render(request, 'almacen/storeditem_new.html', {'form':form})


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
# @method_decorator(login_required, name='dispatch')
# class CreateStoredItem(CreateView):
#     model = StoredItem
#     fields = '__all__'
#
#
# @method_decorator(login_required, name='dispatch')
# class UpdateStoredItem(UpdateView):
#     model = StoredItem
#     fields = '__all__'


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
