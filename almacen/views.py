from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404
from django.views import generic

import datetime

# Create your views here.
from django.views.generic import DeleteView, CreateView, UpdateView

from almacen.models import Contract, StoredItem, Provider, Item
from .forms import EditContractForm, NewContractForm


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
class CreateProvider(CreateView):
    model = Provider
    fields = '__all__'


class UpdateProvider(UpdateView):
    model = Provider
    fields = '__all__'


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
class CreateItem(CreateView):
    model = Item
    fields = '__all__'


class UpdateItem(UpdateView):
    model = Item
    fields = '__all__'


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
class CreateStoredItem(CreateView):
    model = StoredItem
    fields = '__all__'


class UpdateStoredItem(UpdateView):
    model = StoredItem
    fields = '__all__'


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