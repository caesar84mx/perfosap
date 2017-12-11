from .models import Contract, Provider, Item, StoredItem
from django.contrib import admin

# Register your models here.
admin.site.register(Contract)
admin.site.register(Provider)
admin.site.register(Item)
admin.site.register(StoredItem)