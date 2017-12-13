from django.db import models
from django.urls import reverse


# Create your models here.
from procura.models import Item


class StoredItem(models.Model):
    item = models.ForeignKey(Item)
    quantity = models.IntegerField(default=0)

    class Meta:
        ordering = ["item"]

    def __str__(self):
        return "{0} - {1}, {2} pcs.".format(self.item.serial, self.item.name, self.quantity)

    def get_absolute_url(self):
        return reverse('almacen:storeditem-detail', args=[str(self.id)])