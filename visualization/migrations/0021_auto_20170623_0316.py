# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-23 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0020_auto_20170620_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='gender',
            field=models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male')], max_length=1, null=True),
        ),
    ]
