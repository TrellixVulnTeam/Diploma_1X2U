# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KmetApp', '0009_auto_20170314_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selling',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='KmetApp/Media/'),
        ),
    ]
