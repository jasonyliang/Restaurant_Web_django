# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-11 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20180111_0613'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='category',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
