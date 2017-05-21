# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-18 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0014_auto_20170518_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desk',
            name='active_node',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='desk', to='visualization.Node'),
        ),
        migrations.AlterField(
            model_name='desk',
            name='contestant',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='desk', to='visualization.Contestant'),
        ),
    ]