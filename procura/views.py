import datetime

from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import DeleteView, CreateView, UpdateView

from procura.filters import ContractFilter, ProviderFilter
from procura.forms import NewContractForm, EditContractForm, NewOrEditProviderForm
from procura.models import Contract, Provider, Item


def index(request):
    return render(request, 'procura_static_pages/index.html')


@permission_required('procura.create_contract')
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
            return HttpResponseRedirect(reverse('procura:contracts'))
    else:
        today = datetime.date.today()
        form = NewContractForm(initial={
            'start_date': today,
            'expiry_date': datetime.date(today.year + 1, today.month, today.day)
        })
        return render(request, 'procura/contract_new.html', {'form':form})


@permission_required('procura.change_contract')
def edit_contract(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        form = EditContractForm(request.POST)
        if form.is_valid():
            contract.description = form.cleaned_data['description']
            contract.start_date = form.cleaned_data['start_date']
            contract.expiry_date = form.cleaned_data['expiry_date']
            contract.save()
            return HttpResponseRedirect(reverse('procura:contract-detail', args=[pk]))
    else:
        today = datetime.date.today()
        form = EditContractForm(initial={
            'description': contract.description,
            'start_date': today,
            'expiry_date': contract.expiry_date
        })
    return render(request, 'procura/contract_edit.html', {'form': form, 'contract': contract})


@method_decorator(login_required, name='dispatch')
class DeleteContract(DeleteView):
    model = Contract
    success_url = reverse_lazy('procura:contracts')


# @method_decorator(login_required, name='dispatch')
# class ContractListView(generic.ListView):
#     model = Contract
#     paginate_by = 10

@login_required()
def contract_filter(request):
    f = ContractFilter(request.GET, queryset=Contract.objects.all())
    return render_to_response('procura/contract_list.html', {'filter': f})



@method_decorator(login_required, name='dispatch')
class ContractDetailView(generic.DetailView):
    model = Contract


@login_required
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
            return HttpResponseRedirect(reverse('procura:providers'))
    else:
        form = NewOrEditProviderForm()

    return render(request, 'procura/provider_new.html', {'form':form})


@login_required
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
            return HttpResponseRedirect(reverse('procura:provider-detail', args=[pk]))
    else:
        form = NewOrEditProviderForm(initial={
            'name': provider.name,
            'rif': provider.rif,
            'address': provider.address,
            'phone_num': provider.phone_num,
            'contract': provider.contract
        })

    return render(request, 'procura/provider_edit.html', {'form': form, 'provider': provider})


@method_decorator(login_required, name='dispatch')
class DeleteProvider(DeleteView):
    model = Provider
    success_url = reverse_lazy('procura:providers')


# @method_decorator(login_required, name='dispatch')
# class ProviderListView(generic.ListView):
#     model = Provider
#     paginate_by = 10

@login_required()
def provider_filter(request):
    f = ProviderFilter(request.GET, queryset=Provider.objects.all())
    return render_to_response('procura/provider_list.html', {'filter': f})


@method_decorator(login_required, name='dispatch')
class ProviderDetailView(generic.DetailView):
    model = Provider


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
    success_url = reverse_lazy('procura:items')


@method_decorator(login_required, name='dispatch')
class ItemListView(generic.ListView):
    model = Item
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
class ItemDetailView(generic.DetailView):
    model = Item
