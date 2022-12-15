# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-04 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KmetApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='picture',
            field=models.ImageField(null=True, upload_to='KmetApp/Media/'),
        ),
        migrations.AlterField(
            model_name='order_basket',
            name='date_completed',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='order_product',
            name='date_completed',
            field=models.DateTimeField(null=True),
        ),
    ]