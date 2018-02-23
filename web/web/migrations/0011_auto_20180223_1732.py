# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-23 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20180223_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalsetting',
            name='show_area_id_multiple',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'Filter Multiple Area ID (separate Area IDs with comma)'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='show_bps_id_des_multiple',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'Filter Multiple BPS ID (Desa, separate BPS IDs with comma)'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='show_bps_id_kab_multiple',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'Filter Multiple BPS ID (Kabupaten, separate BPS IDs with comma)'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='show_bps_id_kec_multiple',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'Filter Multiple BPS ID (Kecamatan, separate BPS IDs with comma)'),
        ),
    ]
