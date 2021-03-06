import re

from django import forms
from django.core.exceptions import ValidationError
from django.forms import SelectDateWidget
from django.utils.translation import ugettext_lazy as _

from procura.models import Contract, Provider


class NewContractForm(forms.Form):
    number = forms.CharField()
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())
    start_date = forms.DateField(widget=SelectDateWidget())
    expiry_date = forms.DateField(widget=SelectDateWidget())

    def clean_expiry_date(self):
        exp_date = self.cleaned_data['expiry_date']
        st_date = self.cleaned_data['start_date']
        if exp_date is not None:
            if exp_date is not None:
                if exp_date <= st_date:
                    raise ValidationError(_("Invalid date - the contract can not expire before it started"
                                            " or expire the same day!"))

        return exp_date


class EditContractForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea, help_text="Enter contract description")
    start_date = forms.DateField(widget=SelectDateWidget(), help_text="Enter contract start date")
    expiry_date = forms.DateField(widget=SelectDateWidget(), help_text="Enter contract expiry date", required=False)

    def clean_expiry_date(self):
        exp_date = self.cleaned_data['expiry_date']
        st_date = self.cleaned_data['start_date']
        if exp_date is not None:
            if exp_date <= st_date:
                raise ValidationError(_("Invalid date - the contract can not expire before it started"
                                        " or expire the same day!"))

        return exp_date


class NewOrEditProviderForm(forms.Form):
    name = forms.CharField()
    rif = forms.CharField(max_length=11)
    address = forms.CharField(widget=forms.Textarea())
    phone_num = forms.CharField(max_length=13)
    contract = forms.ModelChoiceField(queryset=Contract.objects.all())

    def clean_phone_num(self):
        ph_num = self.cleaned_data['phone_num']
        p = re.compile(r'^\+\d{10,13}$')
        if not p.search(ph_num):
            raise ValidationError(_('Invalid phone number: amust start from \+ and the numeric part be '
                                    '10 - 13 digits long'))

        return ph_num

    def clean_rif(self):
        rif = self.cleaned_data['rif']
        p = re.compile(r'^(E-|P-|J-|V-|G-|C-)\d{9}$')
        if not p.search(rif):
            raise ValidationError(_('Invalid RIF format: must begin from one of these: "E-", "P-", '
                                    '"J-", "V-", "G-" or "C-" '
                                    'and the numeric part be 9 digits long'))

        return rif


class NewOrEditItemForm(forms.Form):
    serial = forms.CharField()
    name = forms.CharField()
    manufacturer = forms.CharField()
    provider = forms.ModelChoiceField(queryset=Provider.objects.all())