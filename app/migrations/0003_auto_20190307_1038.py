# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-07 02:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_musbuy_nav'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Musbuy',
            new_name='Mustbuy',
        ),
        migrations.AlterModelTable(
            name='mustbuy',
            table='axf_mustbuy',
        ),
    ]