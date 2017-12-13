from django.contrib import admin

# Register your models here.
from procura.models import Contract, Provider, Item

admin.site.register(Contract)
admin.site.register(Provider)
admin.site.register(Item)