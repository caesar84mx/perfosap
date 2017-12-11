# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 19:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contract',
            options={'ordering': ['expiry_date', 'start_date', 'name'], 'permissions': (('can_some_shit', 'Can do some shit'),)},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['provider', 'name']},
        ),
        migrations.AlterModelOptions(
            name='provider',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='storeditem',
            options={'ordering': ['item']},
        ),
    ]
