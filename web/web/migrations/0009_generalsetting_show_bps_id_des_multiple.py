# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-23 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20180221_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalsetting',
            name='show_bps_id_des_multiple',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'Filter Multiple BPS ID (Desa, separate BPS ID with comma)'),
        ),
    ]
