# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KmetApp', '0010_auto_20170314_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_selling',
            name='date_Completed',
            field=models.DateTimeField(blank=True),
        ),
    ]
