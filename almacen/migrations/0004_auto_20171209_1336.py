# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0003_auto_20171208_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='expiry_date',
            field=models.DateField(default=django.utils.timezone.now, help_text='Expiry date'),
            preserve_default=False,
        ),
    ]
