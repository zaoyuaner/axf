# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-08 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.CharField(default='axf.png', max_length=100),
        ),
    ]
