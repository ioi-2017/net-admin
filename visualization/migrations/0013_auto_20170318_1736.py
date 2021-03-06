# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-18 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import visualization.models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0012_auto_20170318_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desk',
            name='x',
            field=models.FloatField(default=0.5, validators=[visualization.models.xy_range_validator]),
        ),
        migrations.AlterField(
            model_name='desk',
            name='y',
            field=models.FloatField(default=0.5, validators=[visualization.models.xy_range_validator]),
        ),
    ]
