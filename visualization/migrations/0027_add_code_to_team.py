# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-23 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0026_add_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='country_code',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]