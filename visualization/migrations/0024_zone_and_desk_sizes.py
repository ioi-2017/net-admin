# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-23 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0023_auto_20170623_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='zone',
            name='desk_height',
            field=models.FloatField(default=10),
        ),
        migrations.AddField(
            model_name='zone',
            name='desk_width',
            field=models.FloatField(default=20),
        ),
        migrations.AddField(
            model_name='zone',
            name='height',
            field=models.FloatField(default=480),
        ),
        migrations.AddField(
            model_name='zone',
            name='width',
            field=models.FloatField(default=640),
        ),
    ]
