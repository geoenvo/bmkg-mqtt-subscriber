from django.db import models


class GeneralSetting(models.Model):
    address = models.CharField(
        max_length=255,
        default='localhost',
        verbose_name="Broker Address",
    )
    keepalive = models.IntegerField(
        default=60,
        verbose_name="Broker Keepalive",
    )
    user = models.CharField(
        max_length=255,
        verbose_name="Broker User",
    )
    password = models.CharField(
        max_length=255,
        verbose_name="Broker Password",
    )
    client_id = models.CharField(
        max_length=255,
        verbose_name="Broker Client ID",
    )
    client_id_sub = models.CharField(
        max_length=255,
        verbose_name="Broker Client ID Sub",
    )
    title = models.CharField(
        max_length=255,
        default='BMKG MQTT',
        verbose_name="Site Title",
    )
    refresh = models.IntegerField(
        default=300,
        verbose_name="Refresh (s)",
    )


class TopicSetting(models.Model):
    topic = models.CharField(
        max_length=255,
        blank=True,
    )
    subscribe = models.BooleanField(
        default=False,
    )
    TABLE_CHOICES = (
        ('digital_forecast', 'Digital Forecast'),
        ('maritim_cuaca_pelayanan', 'Maritim Cuaca Pelayanan'),
        ('maritim_cuaca_pelabuhan', 'Maritim Cuaca Pelabuhan'),
        ('maritim_cuaca_penyebrangan', 'Maritim Cuaca Penyebrangan'),
        ('maritim_wisata_bahari', 'Maritim Wisata Bahari'),
        ('satelit_hotspot_modis', 'Satelit Hotspot Modis'),
        ('satelit_himawari_8_natural_color', 'Satelit Himawari 8 Naturan Color'),
        ('satelit_himawari_8_ir_enhanced', 'Satelit Himawari 8 IR Enhanced'),
        ('gempa_terkini', 'Gempa Terkini'),
        ('gempa_terkini_csv', 'Gempa Terkini CSV'),
        ('gempa_dirasakan', 'Gempa Dirasakan'),
        ('iklim_kabupaten_csv', 'Iklim Kabupaten CSV'),
        ('iklim_kecamatan_csv', 'Iklim Kecamatan CSV'),
        ('iklim_desa_csv', 'Iklim Desa CSV'),
    )
    table = models.CharField(
        max_length=255,
        blank=True,
        choices=TABLE_CHOICES,
        default='digital_forecast',
    )
