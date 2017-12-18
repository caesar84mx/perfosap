import json

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

OPERATIONS = 'OPS'
PROCUREMENT = 'PRO'
GS = 'SGS'
HR = 'RHS'
FINANCES = 'FZS'
PLANNING = 'PLA'
ADVISER = 'ASE'
LEGAL = 'LEG'
STORE = 'ALM'
SD = 'DSI'
IT = 'AIT'
HSE = 'HSE'

DEPARTMENT_CHOICE = {
    (OPERATIONS, 'Operaciones'),
    (PROCUREMENT, 'Procura'),
    (GS, 'SSGG'),
    (HR, 'RRHH'),
    (FINANCES, 'Finanzas'),
    (PLANNING, 'Planificacion'),
    (ADVISER, 'Asesoria'),
    (LEGAL, 'LEGAL'),
    (STORE, 'Almacen'),
    (SD, 'DSI'),
    (IT, 'AIT'),
    (HSE, 'HSE'),
}

PENDING = 'PEN'
DISPATCHED = 'DIS'
SUSPENDED = 'SUS'

ORDER_STATUS = {
    (PENDING, 'Pendiente'),
    (DISPATCHED, 'Despachado'),
    (SUSPENDED, 'Suspendido')
}


class HandoutOrder(models.Model):
    department = models.CharField(max_length=3, choices=DEPARTMENT_CHOICE, default=OPERATIONS)
    datetime_registered = models.DateTimeField()
    status = models.CharField(max_length=3, choices=ORDER_STATUS, default=PENDING)
    change_status_datetime = models.DateTimeField()
    #items list will be json and must have the following format "[{stored_item.pk: quantity}, ...]"
    items = models.TextField()

    def setitems(self, items_string):
        self.items = json.dumps(items_string)

    def getitems(self):
        return json.loads(self.items)

    class Meta:
        ordering = ['-datetime_registered']