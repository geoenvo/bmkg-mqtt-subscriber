"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin

from .views import (
    gempa_dirasakan,
    gempa_terkini,
    satelit_hotspot_modis,
    satelit_himawari_8_natural_color,
    satelit_himawari_8_ir_enhanced,
    maritim_cuaca_pelabuhan,
    maritim_cuaca_pelayanan,
    maritim_cuaca_penyebrangan,
    maritim_wisata_bahari,
    digital_forecast,
    iklim_kabupaten_csv,
    iklim_kecamatan_csv,
    iklim_desa_csv,
    digital_forecast_info,
    digital_forecast_info2,
    maritim_cuaca_pelayanan_info,
    maritim_cuaca_pelabuhan_info,
    maritim_cuaca_penyebrangan_info,
    maritim_wisata_bahari_info,
    iklim_kabupaten_csv_info,
    iklim_kecamatan_csv_info,
    iklim_desa_csv_info
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', digital_forecast_info, name='home'),
    url(r'^gempa/gempadirasakan$', gempa_dirasakan, name='gempa_dirasakan'),
    url(r'^gempa/gempaterkini$', gempa_terkini, name='gempa_terkini'),
    url(r'^cuaca/citrasatelit/hotspotmodis$', satelit_hotspot_modis, name='satelit_hotspot_modis'),
    url(r'^cuaca/citrasatelit/naturalcolor$', satelit_himawari_8_natural_color, name='satelit_himawari_8_natural_color'),
    url(r'^cuaca/citrasatelit/irenhanced$', satelit_himawari_8_ir_enhanced, name='satelit_himawari_8_ir_enhanced'),
    url(r'^cuaca/maritim/pelabuhan$', maritim_cuaca_pelabuhan, name='maritim_cuaca_pelabuhan'),
    url(r'^cuaca/maritim/pelayanan$', maritim_cuaca_pelayanan, name='maritim_cuaca_pelayanan'),
    url(r'^cuaca/maritim/penyebrangan$', maritim_cuaca_penyebrangan, name='maritim_cuaca_penyebrangan'),
    url(r'^cuaca/maritim/wisata_bahari$', maritim_wisata_bahari, name='maritim_wisata_bahari'),
    url(r'^cuaca/digitalforecast$', digital_forecast, name='digital_forecast'),
    url(r'^iklim/kabupaten$', iklim_kabupaten_csv, name='iklim_kabupaten_csv'),
    url(r'^iklim/kecamatan$', iklim_kecamatan_csv, name='iklim_kecamatan_csv'),
    url(r'^iklim/desa$', iklim_desa_csv, name='iklim_desa_csv'),
    url(r'^cuaca/digitalforecast/info$', digital_forecast_info, name='digital_forecast_info'),
    url(r'^cuaca/digitalforecast/info2$', digital_forecast_info2, name='digital_forecast_info2'),
    url(r'^cuaca/maritim/pelayanan/info$', maritim_cuaca_pelayanan_info, name='maritim_cuaca_pelayanan_info'),
    url(r'^cuaca/maritim/pelabuhan/info$', maritim_cuaca_pelabuhan_info, name='maritim_cuaca_pelabuhan_info'),
    url(r'^cuaca/maritim/penyebrangan/info$', maritim_cuaca_penyebrangan_info, name='maritim_cuaca_penyebrangan_info'),
    url(r'^cuaca/maritim/wisata_bahari/info$', maritim_wisata_bahari_info, name='maritim_wisata_bahari_info'),
    url(r'^iklim/kabupaten/info$', iklim_kabupaten_csv_info, name='iklim_kabupaten_csv_info'),
    url(r'^iklim/kecamatan/info$', iklim_kecamatan_csv_info, name='iklim_kecamatan_csv_info'),
    url(r'^iklim/desa/info$', iklim_desa_csv_info, name='iklim_desa_csv_info'),
]

# Allow dev server to serve media files
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
elif getattr(settings, 'FORCE_SERVE_STATIC', False): # Force dev server to serve static files
    settings.DEBUG = True
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    settings.DEBUG = False
