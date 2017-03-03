# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 20:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_admin', '0006_auto_20170303_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskrun',
            name='run_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taskruns', to='task_admin.TaskRunSet'),
        ),
    ]
