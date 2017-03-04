# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KmetApp', '0003_auto_20170228_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='origin',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='basket',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, max_length=10),
        ),
        migrations.AlterField(
            model_name='order_basket',
            name='price_Order',
            field=models.DecimalField(decimal_places=2, max_digits=5, max_length=10),
        ),
        migrations.AlterField(
            model_name='order_selling',
            name='price_Order',
            field=models.DecimalField(decimal_places=2, max_digits=5, max_length=10),
        ),
        migrations.AlterField(
            model_name='selling',
            name='origin',
            field=models.CharField(max_length=50),
        ),
    ]
