from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

# Contract related forms
from procura.models import Item


# Stored items related forms
class NewOrEditStoredItemForm(forms.Form):
    item = forms.ModelChoiceField(queryset=Item.objects.all())
    quantity = forms.IntegerField()

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 0:
            raise ValidationError(_("Items quantity can not be negative!"))
        return quantity
