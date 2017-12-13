import datetime

from django.db import models

# Create your models here.
from django.urls import reverse


class LegalEntity(models.Model):
    name = models.CharField(max_length=100, help_text="Name")
    rif = models.CharField(max_length=11, help_text="RIF")
    address = models.TextField(help_text="Address")
    phone_num = models.CharField(max_length=15, help_text="Phone number")

    def __str__(self):
        pass


class Contract(models.Model):
    name = models.CharField(max_length=100, help_text="Name")
    number = models.CharField(max_length=50, help_text="Contract number")
    description = models.TextField(help_text="Contract description")
    start_date = models.DateField(help_text="Start date")
    expiry_date = models.DateField(help_text="Expiry date")

    class Meta:
        ordering = ["-expiry_date", "start_date", "name"]

    @property
    def is_expired(self):
        return self.expiry_date < datetime.date.today()

    def __str__(self):
        return "number: {0}, " \
               "name: \"{1}\", " \
               "starts: {2}, " \
               "expires: {3}."\
            .format(self.number, self.name, self.start_date, self.expiry_date)

    def get_absolute_url(self):
        return reverse('procura:contract-detail', args=[str(self.id)])


class Provider(LegalEntity):
    contract = models.ForeignKey(Contract)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return "name: \"{0}\", " \
               "RIF: {1}, " \
               "phone: {2}."\
            .format(self.name, self.rif, self.phone_num)

    def get_absolute_url(self):
        return reverse('procura:provider-detail', args=[str(self.id)])


class Item(models.Model):
    name = models.CharField(max_length=100, help_text="Name")
    serial = models.CharField(max_length=50, help_text="Serial No.")
    manufacturer = models.CharField(max_length=50, help_text="Manufacturer")
    provider = models.ForeignKey(Provider)

    class Meta:
        ordering = ["provider", "name"]

    def __str__(self):
        return "name: \"{0}\", " \
               "serial: {1}, " \
               "manufacturer: {2}," \
               "provider: {3}."\
            .format(self.name, self.serial, self.manufacturer, self.provider.name)

    def get_absolute_url(self):
        return reverse('procura:item-detail', args=[str(self.id)])