# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-01 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_admin', '0009_auto_20170319_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskrunset',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
