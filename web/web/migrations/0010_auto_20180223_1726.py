# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-23 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_generalsetting_show_bps_id_des_multiple'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalsetting',
            name='show_bps_id_kab_multiple',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'Filter Multiple BPS ID (Kabupaten, separate BPS ID with comma)'),
        ),
        migrations.AddField(
            model_name='generalsetting',
            name='show_bps_id_kec_multiple',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'Filter Multiple BPS ID (Kecamatan, separate BPS ID with comma)'),
        ),
    ]
