# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-23 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0021_auto_20170623_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
    ]