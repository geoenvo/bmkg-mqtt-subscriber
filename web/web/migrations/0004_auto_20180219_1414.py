# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-19 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20180219_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalsetting',
            name='client_id',
            field=models.CharField(max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='generalsetting',
            name='client_id_sub',
            field=models.CharField(max_length=255),
            preserve_default=False,
        ),
    ]
