"""
BMKG MQTT Template Views
"""

import sqlite3
import json
import ast
import operator

from django.conf import settings
from django.shortcuts import render

from datetime import datetime, date, timedelta

from templatetags.helper import (
        weather_image,
        get_timestamp,
        wind_direction,
        strip_tags,
        get_category,
        get_month_year,
        get_timestampfull
    )


def gempa_dirasakan(request):
    """
    Gempa Dirasakan
    """
    gempa_dirasakan = []

    # Connect to databases
    SQLITE_DB = settings.DATABASES['bmkg_mqtt']['NAME']
    connection = sqlite3.connect(SQLITE_DB)
    cursor = connection.cursor()
    latest = request.GET.get('latest')
    if latest:
        query = (
            "SELECT tanggal, lintang, bujur, "
            "magnitude, magnitude_unit, "
            "kedalaman, kedalaman_unit, "
            "keterangan, dirasakan, batch_time "
            "FROM gempa_dirasakan "
            "WHERE batch_time = (SELECT MAX(batch_time) FROM gempa_dirasakan)"
            "ORDER BY batch_time DESC "
        )
    else:
        query = (
            "SELECT tanggal, lintang, bujur, "
            "magnitude, magnitude_unit, "
            "kedalaman, kedalaman_unit, "
            "keterangan, dirasakan, batch_time "
            "FROM gempa_dirasakan ORDER BY batch_time DESC "
        )
    cursor.execute(query)

    # Append Record
    for value in cursor:
        tanggal_fmt = datetime.strftime(datetime.strptime(value[0], '%Y-%m-%d %H:%M:%S'), "%Y%m%d%H%M%S")
        if value[1] < 0:
            lintang = abs(value[1])
            lintang_unit = "LS"
        else:
            lintang = value[1]
            lintang_unit = "LU"
        if value[2] < 0:
            bujur = abs(value[2])
            bujur_unit = "BB"
        else:
            bujur = value[2]
            bujur_unit = "BT"
        record = {
            'tanggal_fmt': tanggal_fmt,
            'tanggal': value[0],
            'lintang': lintang,
            'lintang_unit': lintang_unit,
            'bujur': bujur,
            'bujur_unit': bujur_unit,
            'magnitude': value[3],
            'magnitude_unit': value[4],
            'kedalaman': value[5],
            'kedalaman_unit': value[6],
            'keterangan': value[7],
            'dirasakan': filter(None, value[8].replace(' ', '').split(',')),
            'batch_time': value[9]
        }
        gempa_dirasakan.append(record)
    cursor.close()
    connection.close()
    return render(request, 'gempa_dirasakan.html', {'gempa_dirasakan': gempa_dirasakan})


def gempa_terkini(request):
    """
    Gempa Terkini
    """
    gempa_terkini = []

    # Connect to databases
    SQLITE_DB = settings.DATABASES['bmkg_mqtt']['NAME']
    connection = sqlite3.connect(SQLITE_DB)
    cursor = connection.cursor()
    latest = request.GET.get('latest')
    if latest:
        query = (
            "SELECT datetime, src, eqid, "
            "longitude, latitude, "
            "magnitude, depth, "
            "region, batch_time  "
            "FROM gempa_terkini_csv "
            "WHERE batch_time = (SELECT MAX(batch_time) FROM gempa_terkini_csv)"
            "ORDER BY batch_time DESC "
        )
    else:
        query = (
            "SELECT datetime, src, eqid, "
            "longitude, latitude, "
            "magnitude, depth, "
            "region, batch_time  "
            "FROM gempa_terkini_csv ORDER BY batch_time DESC "
        )
    cursor.execute(query)

    # Append Record
    for value in cursor:
        record = {
            'tanggal': value[0],
            'src': value[1],
            'eqid': value[2],
            'bujur': value[3],
            'lintang': value[4],
            'magnitude': value[5],
            'kedalaman': value[6],
            'wilayah': value[7],
            'batch_time': value[8]
        }
        gempa_terkini.append(record)
    cursor.close()
    connection.close()
    return render(request, 'gempa_terkini.html', {'gempa_terkini': gempa_terkini})


def satelit_hotspot_modis(request):
    """
    Satelit Hotspot Modis
    """
    satelit_hotspot_modis = []

    # Connect to databases
    SQLITE_DB = settings.DATABASES['bmkg_mqtt']['NAME']
    connection = sqlite3.connect(SQLITE_DB)
    cursor = connection.cursor()
    latest = request.GET.get('latest')
    if latest:
        query = (
            "SELECT judul, narasi, lokasi, file, batch_time  "
            "FROM satelit_hotspot_modis WHERE "
            "batch_time = (SELECT MAX(batch_time) FROM satelit_hotspot_modis) "
            "ORDER BY batch_time DESC "
        )
    else:
        query = (
            "SELECT judul, narasi, lokasi, file, batch_time  "
            "FROM satelit_hotspot_modis ORDER BY batch_time DESC "
        )
    cursor.execute(query)

    # Append Record
    for value in cursor:
        record = {
            'judul': value[0],
            'narasi': value[1],
            'lokasi': value[2],
            'file': value[3],
            'batch_time': value[4]
        }
        satelit_hotspot_modis.append(record)
    cursor.close()
    connection.close()
    return render(request, 'satelit_hotspot_modis.html', {'satelit_hotspot_modis': satelit_hotspot_modis})


def satelit_himawari_8_natural_color(request):
    """
    Satelit Himawari 8 Natural Color
    """
    satelit_himawari_8_natural_color = []

    # Connect to databases
    SQLITE_DB = settings.DATABASES['bmkg_mqtt']['NAME']
    connection = sqlite3.connect(SQLITE_DB)
    cursor = connection.cursor()
    latest = request.GET.get('latest')
    if latest:
        query = (
            "SELECT judul, narasi, lokasi, file, batch_time  "
            "FROM satelit_himawari_8_natural_color WHERE "
            "batch_time = (SELECT MAX(batch_time) FROM satelit_himawari_8_natural_color) "
            "ORDER BY batch_time DESC "
        )
    else:
        query = (
            "SELECT judul, narasi, lokasi, file, batch_time  "
            "FROM satelit_himawari_8_natural_color ORDER BY batch_time DESC "
        )
    cursor.execute(query)

    # Append Record
    for value in cursor:
        record = {
            'judul': value[0],
            'narasi': value[1],
            'lokasi': value[2],
            'file': value[3],
            'batch_time': value[4]
        }
        satelit_himawari_8_natural_color.append(record)
    cursor.close()
    connection.close()
    return render(request, 'satelit_himawari_8_natural_color.html', {'satelit_himawari_8_natural_color': satelit_himawari_8_natural_color})


def satelit_himawari_8_ir_enhanced(request):
    """
    Satelit Himawari 8 IR Enhanced
    """
    satelit_himawari_8_ir_enhanced = []

    # Connect to databases
    SQLITE_DB = settings.DATABASES['bmkg_mqtt']['NAME']
    connection = sqlite3.connect(SQLITE_DB)
    cursor = connection.cursor()
    latest = request.GET.get('latest')
    if latest:
        query = (
            "SELECT judul, narasi, lokasi, file, batch_time  "
            "FROM satelit_himawari_8_ir_enhanced "
            "WHERE batch_time = (SELECT MAX(batch_time) FROM satelit_himawari_8_ir_enhanced)"
            "ORDER BY batch_time DESC "
        )
    else:
        query = (
            "SELECT judul, narasi, lokasi, file, batch_time  "
            "FROM satelit_himawari_8_ir_enhanced ORDER BY batch_time DESC "
        )
    cursor.execute(query)

    # Append Record
    for value in cursor:
        record = {
            'judul': value[0],
            'narasi': value[1],
            'lokasi': value[2],
            'file': value[3],
            'batch_time': value[4]
        }
        satelit_himawari_8_ir_enhanced.append(record)
    cursor.close()
    connection.close()
    return render(request, 'satelit_himawari_8_ir_enhanced.html', {'satelit_himawari_8_ir_enhanced': satelit_himawari_8_ir_enhanced})


def maritim_cuaca_pelabuhan(request):
    """
    Maritim Cuaca Pelabuhan
    """
    maritim_cuaca_pelabuhan = []

    # Connect to databases
    SQLITE_DB = settings.DATABASES['bmkg_mqtt']['NAME']
    connection = sqlite3.connect(SQLITE_DB)
    cursor = connection.cursor()
    latest = request.GET.get('latest')
    if latest:
        query = (
            "SELECT station_id, shortname, port_name, "
            "weather_icon, wd_from_icon_id, wd_to_icon_id, "
            "ws_min, ws_max, wave_min, wave_max, "
            "visibility, tmin, tmax, humin, humax, "
            "pasang_max, pasang_max_datemin, pasang_max_datemax, pasang_max_zona, "
            "pasang_min, pasang_min_datemin, pasang_min_datemax, pasang_min_zona, batch_time  "
            "FROM maritim_cuaca_pelabuhan WHERE batch_time = "
            "(SELECT MAX(batch_time) FROM maritim_cuaca_pelabuhan) ORDER BY batch_time DESC "
        )
    else:
        query = (
            "SELECT station_id, shortname, port_name, "
            "weather_icon, wd_from_icon_id, wd_to_icon_id, "
            "ws_min, ws_max, wave_min, wave_max, "
            "visibility, tmin, tmax, humin, humax, "
            "pasang_max, pasang_max_datemin, pasang_max_datemax, pasang_max_zona, "
            "pasang_min, pasang_min_datemin, pasang_min_datemax, pasang_min_zona, batch_time  "
            "FROM maritim_cuaca_pelabuhan ORDER BY batch_time DESC "
        )
    cursor.execute(query)

    # Append Record
    for value in cursor:
        if value[16]:
            pasang_max_datemin = datetime.strftime(datetime.strptime(value[16], '%Y-%m-%d %H:%M:%S'), "%H:%M:%S")
        else:
            pasang_max_datemin = None
        if value[17]:
            pasang_max_datemax = datetime.strftime(datetime.strptime(value[16], '%Y-%m-%d %H:%M:%S'), "%H:%M:%S")
        else:
            pasang_max_datemax = None
        if value[16]:
            pasang_min_datemin = datetime.strftime(datetime.strptime(value[16], '%Y-%m-%d %H:%M:%S'), "%H:%M:%S")
        else:
            pasang_min_datemin = None
        if value[17]:
            pasang_min_datemax = datetime.strftime(datetime.strptime(value[16], '%Y-%m-%d %H:%M:%S'), "%H:%M:%S")
        else:
            pasang_min_datemax = None
        record = {
            'station_id': value[0],
            'shortname': value[1],
            'port_name': value[2],
            'weather_icon': value[3],
            'wd_from_icon_id': value[4],
            'wd_to_icon_id': value[5],
            'ws_min': value[6],
            'ws_max': value[7],
            'wave_min': value[8],
            'wave_max': value[9],
            'visibility': value[10],
            'tmin': value[11],
            'tmax': value[12],
            'humin': value[12],
            'humax': value[14],
            'pasang_max': value[15],
            'pasang_max_datemin': pasang_max_datemin,
            'pasang_max_datemax': pasang_max_datemax,
            'pasang_max_zona': value[18],
            'pasang_min': value[19],
            'pasang_min_datemin': pasang_min_datemin,
            'pasang_min_datemax': pasang_min_datemax,
            'pasang_min_zona': value[22],
            'batch_time': value[23]
        }
        maritim_cuaca_pelabuhan.append(record)
    cursor.close()
    connection.close()
    return render(request, 'maritim_cuaca_pelabuhan.html', {'maritim_cuaca_pelabuhan': maritim_cuaca_pelabuhan})


def maritim_cuaca_pelabuhan_info(request):
    """
    Maritim Cuaca Pelabuhan Info
    """
    maritim_cuaca_pelabuhan_info = []

    # Connect to databases
    SQLITE_DB = settings.DATABASES['bmkg_mqtt']['NAME']
    connection = sqlite3.connect(SQLITE_DB)
    cursor = connection.cursor()
    query = (
        "SELECT station_id, shortname, timestamp, port_id, port_name, "
        "weather_icon, wd_from_icon_id, wd_to_icon_id, "
        "ws_min, ws_max, wave_min, wave_max, pasang_min_description, batch_time "
        "FROM maritim_cuaca_pelabuhan WHERE batch_time = "
        "(SELECT MAX(batch_time) FROM maritim_cuaca_pelabuhan) "
        "ORDER BY batch_time DESC, shortname "
    )
    cursor.execute(query)
    stasion = {}
    last_station_id = None
    cur_stasion_id = None
    # Append Record
    for value in cursor:
        cur_stasion_id = value[0]
        if last_station_id and last_station_id != cur_stasion_id:
            maritim_cuaca_pelabuhan_info.append(stasion)
            stasion = {}
        timestamp_1 = datetime.strptime(value[2], '%Y-%m-%d %H:%M:%S')
        if value[13]:
            batch_time = datetime.strptime(value[13], '%Y-%m-%d %H:%M:%S.%f')
            batch_time = get_timestampfull(batch_time)
        else:
            batch_time = None
        try:
            weather_icon = value[5].lower() + '-am.png'
        except:
            weather_icon = None
        record = {
            'station_id': value[0],
            'shortname': value[1],
            'timestamp_1': get_timestamp(timestamp_1),
            'port_id': value[3],
            'port_name': value[4],
            'weather_icon_id': value[5],
            'wd_from_icon_id': value[6],
            'wd_to_icon_id': value[7],
            'ws_min': value[8],
            'ws_max': value[9],
            'wave_min': value[10],
            'wave_max': value[11],
            'pasang_min_description': value[12],
            'batch_time': value[13],
            'weather_icon': weather_icon,
        }
        stasion.update({value[3]: record})
        last_station_id = value[0]
    # Last Append
    maritim_cuaca_pelabuhan_info.append(stasion)
    context = {
        'maritim_cuaca_pelabuhan_info': maritim_cuaca_pelabuhan_info,
        'batch_time': batch_time
    }

    cursor.close()
    connection.close()
    return render(request, 'maritim_cuaca_pelabuhan_info.html', context)


def maritim_cuaca_pelayanan(request):
    """
    Maritim Cuaca Pelayanan
    """
    maritim_cuaca_pelayanan = []

    # Connect to databases
    SQLITE_DB = settings.DATABASES['bmkg_mqtt']['NAME']
    connection = sqlite3.connect(SQLITE_DB)
    cursor = connection.cursor()
    latest = request.GET.get('latest')
    if latest:
        query = (
            "SELECT station_id, shortname, validfrom, validto, timezone, area_name, "
            "weather_icon_id, wd_from_icon_id, wd_to_icon_id, "
            "ws_min, ws_max, wave_min, wave_max, batch_time "
            "FROM maritim_cuaca_pelayanan WHERE batch_time = "
            "(SELECT MAX(batch_time) FROM maritim_cuaca_pelayanan) "
            "ORDER BY batch_time DESC "
        )
    else:
        query = (
            "SELECT station_id, shortname, validfrom, validto, timezone, area_name, "
            "weather_icon_id, wd_from_icon_id, wd_to_icon_id, "
            "ws_min, ws_max, wave_min, wave_max, batch_time "
            "FROM maritim_cuaca_pelayanan ORDER BY batch_time DESC "
        )
    cursor.execute(query)

    # Append Record
    for value in cursor:
        if value[2]:
            validfromdate = datetime.strftime(datetime.strptime(value[2], '%Y-%m-%d %H:%M:%S'), "%d/%m/%Y")
            validfromhour = datetime.strftime(datetime.strptime(value[2], '%Y-%m-%d %H:%M:%S'), "%H:%M:%S")
        else:
            validfromdate = None
            validfromhour = None
        if value[3]:
            validtodate = datetime.strftime(datetime.strptime(value[3], '%Y-%m-%d %H:%M:%S'), "%d/%m/%Y")
            validtohour = datetime.strftime(datetime.strptime(value[3], '%Y-%m-%d %H:%M:%S'), "%H:%M:%S")
        else:
            validtodate = None
            validtohour = None
        record = {
            'station_id': value[0],
            'shortname': value[1],
            'validfromdate': validfromdate,
            'validfromhour': validfromhour,
            'validtodate': validtodate,
            'validtohour': validtohour,
            'timezone': value[4],
            'area_name': value[5],
            'weather_icon_id': value[6],
            'wd_from_icon_id': value[7],
            'wd_to_icon_id': value[8],
            'ws_min': value[9],
            'ws_max': value[10],
            'wave_min': value[11],
            'wave_max': value[12],
            'batch_time': value[13]
        }
        maritim_cuaca_pelayanan.append(record)
    cursor.close()
    connection.close()
    return render(request, 'maritim_cuaca_pelayanan.html', {'maritim_cuaca_pelayanan': maritim_cuaca_pelayanan})


def maritim_cuaca_pelayanan_info(request):
    """
    Maritim Cuaca Pelayanan Info
    """
    maritim_cuaca_pelayanan_info = []

    # Connect to databases
    SQLITE_DB = settings.DATABASES['bmkg_mqtt']['NAME']
    connection = sqlite3.connect(SQLITE_DB)
    cursor = connection.cursor()
    query = (
        "SELECT station_id, shortname, timestamp, area_id, area_name, "
        "weather_icon_id, wd_from_icon_id, wd_to_icon_id, "
        "ws_min, ws_max, wave_min, wave_max, status_warning, hari, batch_time, peringatan_dini "
        "FROM maritim_cuaca_pelayanan WHERE batch_time = "
        "(SELECT MAX(batch_time) FROM maritim_cuaca_pelayanan) "
        "ORDER BY batch_time DESC, shortname "
    )
    cursor.execute(query)
    stasion = {}
    category = {}
    last_station_id = None
    cur_stasion_id = None
    # Append Record
    for value in cursor:
        cur_stasion_id = value[0]
        if last_station_id and last_station_id != cur_stasion_id:
            maritim_cuaca_pelayanan_info.append(stasion)
            stasion = {}
        timestamp_1 = datetime.strptime(value[2], '%Y-%m-%d %H:%M:%S')
        timestamp_2 = datetime.strptime(value[2], '%Y-%m-%d %H:%M:%S') + timedelta(days=1)
        timestamp_3 = datetime.strptime(value[2], '%Y-%m-%d %H:%M:%S') + timedelta(days=2)
        timestamp_4 = datetime.strptime(value[2], '%Y-%m-%d %H:%M:%S') + timedelta(days=3)
        if value[14]:
            batch_time = datetime.strptime(value[14], '%Y-%m-%d %H:%M:%S.%f')
            batch_time = get_timestampfull(batch_time)
        else:
            batch_time = None
        try:
            weather_icon = value[5].lower() + '-am.png'
        except:
            weather_icon = None
        record = {
            'station_id': value[0],
            'shortname': value[1],
            'timestamp_1': get_timestamp(timestamp_1),
            'timestamp_2': get_timestamp(timestamp_2),
            'timestamp_3': get_timestamp(timestamp_3),
            'timestamp_4': get_timestamp(timestamp_4),
            'area_id': value[3],
            'area_name': value[4],
            'weather_icon_id': value[5],
            'wd_from_icon_id': value[6],
            'wd_to_icon_id': value[7],
            'ws_min': value[8],
            'ws_max': value[9],
            'wave_min': value[10],
            'wave_max': value[11],
            'status_warning': value[12],
            'hari': value[13],
            'batch_time': batch_time,
            'weather_icon': weather_icon,
            'peringatan_dini':  strip_tags(value[15]),
        }
        if value[13] == "hari_ini":
            category = {}
            category.update({value[13]: record})
            stasion.update({value[3]: category})
        else:
            category.update({value[13]: record})
            stasion.update({value[3]: category})
        last_station_id = value[0]
    # Last Append
    maritim_cuaca_pelayanan_info.append(stasion)
    context = {
        'maritim_cuaca_pelayanan_info': maritim_cuaca_pelayanan_info,
        'batch_time': batch_time
    }

    cursor.close()
    connection.close()
    return render(request, 'maritim_cuaca_pelayanan_info.html',context)


def maritim_cuaca_penyebrangan(request):
    """
    Maritim Cuaca Penyebrangan
    """
    maritim_cuaca_penyebrangan = []

    # Connect to databases
    SQLITE_DB = settings.DATABASES['bmkg_mqtt']['NAME']
    connection = sqlite3.connect(SQLITE_DB)
    cursor = connection.cursor()
    latest = request.GET.get('latest')
    if latest:
        query = (
            "SELECT station_id, shortname, validfrom, validto, timezone, "
            "area_name_id, area_habor_from, area_habor_to, "
            "weather_icon, wd_from_icon_id, wd_to_icon_id, "
            "ws_min, ws_max, wave_min, wave_max, batch_time "
            "FROM maritim_cuaca_penyebrangan WHERE "
            "batch_time = (SELECT MAX(batch_time) FROM maritim_cuaca_penyebrangan)"
            "ORDER BY batch_time DESC "
        )
    else:
        query = (
            "SELECT station_id, shortname, validfrom, validto, timezone, "
            "area_name_id, area_habor_from, area_habor_to, "
            "weather_icon, wd_from_icon_id, wd_to_icon_id, "
            "ws_min, ws_max, wave_min, wave_max, batch_time "
            "FROM maritim_cuaca_penyebrangan ORDER BY batch_time DESC "
        )
    cursor.execute(query)

    # Append Record
    for value in cursor:
        if value[2]:
            validfromdate = datetime.strftime(datetime.strptime(value[2], '%Y-%m-%d %H:%M:%S'), "%d/%m/%Y")
            validfromhour = datetime.strftime(datetime.strptime(value[2], '%Y-%m-%d %H:%M:%S'), "%H:%M:%S")
        else:
            validfromdate = None
            validfromhour = None
        if value[3]:
            validtodate = datetime.strftime(datetime.strptime(value[3], '%Y-%m-%d %H:%M:%S'), "%d/%m/%Y")
            validtohour = datetime.strftime(datetime.strptime(value[3], '%Y-%m-%d %H:%M:%S'), "%H:%M:%S")
        else:
            validtodate = None
            validtohour = None
        record = {
            'station_id': value[0],
            'shortname': value[1],
            'validfromdate': validfromdate,
            'validfromhour': validfromhour,
            'validtodate': validtodate,
            'validtohour': validtohour,
            'timezone': value[4],
            'area_name': value[5],
            'area_habor_from': value[6],
            'area_habor_to': value[7],
            'weather_icon': value[8],
            'wd_from_icon_id': value[9],
            'wd_to_icon_id': value[10],
            'ws_min': value[11],
            'ws_max': value[12],
            'wave_min': value[13],
            'wave_max': value[14],
            'batch_time': value[15]
        }
        maritim_cuaca_penyebrangan.append(record)
    cursor.close()
    connection.close()
    return render(request, 'maritim_cuaca_penyebrangan.html', {'maritim_cuaca_penyebrangan': maritim_cuaca_penyebrangan})


def maritim_cuaca_penyebrangan_info(request):
    """
    Maritim Cuaca Penyebrangan Info
    """
    maritim_cuaca_penyebrangan_info = []

    # Connect to databases
    SQLITE_DB = settings.DATABASES['bmkg_mqtt']['NAME']
    connection = sqlite3.connect(SQLITE_DB)
    cursor = connection.cursor()
    query = (
        "SELECT station_id, shortname, timestamp, area_id, area_name_id, "
        "weather_icon, wd_from_icon_id, wd_to_icon_id, "
        "ws_min, ws_max, wave_min, wave_max, wave_min_description, batch_time "
        "FROM maritim_cuaca_penyebrangan WHERE batch_time = "
        "(SELECT MAX(batch_time) FROM maritim_cuaca_penyebrangan) "
        "ORDER BY batch_time DESC, shortname "
    )
    cursor.execute(query)
    stasion = {}
    last_station_id = None
    cur_stasion_id = None
    # Append Record
    for value in cursor:
        cur_stasion_id = value[0]
        if last_station_id and last_station_id != cur_stasion_id:
            maritim_cuaca_penyebrangan_info.append(stasion)
            stasion = {}
        timestamp_1 = datetime.strptime(value[2], '%Y-%m-%d %H:%M:%S')
        if value[13]:
            batch_time = datetime.strptime(value[13], '%Y-%m-%d %H:%M:%S.%f')
            batch_time = get_timestampfull(batch_time)
        else:
            batch_time = None
        try:
            weather_icon = value[5].lower() + '-am.png'
        except:
            weather_icon = None
        record = {
            'station_id': value[0],
            'shortname': value[1],
            'timestamp_1': get_timestamp(timestamp_1),
            'area_id': value[3],
            'area_name_id': value[4],
            'weather_icon_id': value[5],
            'wd_from_icon_id': value[6],
            'wd_to_icon_id': value[7],
            'ws_min': value[8],
            'ws_max': value[9],
            'wave_min': value[10],
            'wave_max': value[11],
            'wave_min_description': value[12],
            'batch_time': batch_time,
            'weather_icon': weather_icon,
        }
        stasion.update({value[3]: record})
        last_station_id = value[0]
    # Last Append
    maritim_cuaca_penyebrangan_info.append(stasion)
    context = {
        'maritim_cuaca_penyebrangan_info': maritim_cuaca_penyebrangan_info,
        'batch_time': batch_time
    }

    cursor.close()
    connection.close()
    return render(request, 'maritim_cuaca_penyebrangan_info.html', context)


def maritim_wisata_bahari(request):
    """
    Maritim Wisata Bahari
    """
    maritim_wisata_bahari = []

    # Connect to databases
    SQLITE_DB = settings.DATABASES['bmkg_mqtt']['NAME']
    connection = sqlite3.connect(SQLITE_DB)
    cursor = connection.cursor()
    latest = request.GET.get('latest')
    if latest:
        query = (
            "SELECT station_id, shortname, "
            "beach_name, datetime, weather, "
            "wd_deg, wd_card, ws_kt, "
            "wave_deg, wave_direction, wave_height_meter, batch_time "
            "FROM maritim_wisata_bahari WHERE "
            "batch_time = (SELECT MAX(batch_time) FROM maritim_wisata_bahari)"
            "ORDER BY batch_time DESC "
        )
    else:
        query = (
            "SELECT station_id, shortname, "
            "beach_name, datetime, weather, "
            "wd_deg, wd_card, ws_kt, "
            "wave_deg, wave_direction, wave_height_meter, batch_time "
            "FROM maritim_wisata_bahari ORDER BY batch_time DESC "
        )
    cursor.execute(query)

    # Append Record
    for value in cursor:
        if value[3]:
            datetime_date = datetime.strftime(datetime.strptime(value[3], '%Y-%m-%d %H:%M:%S'), "%d/%m/%Y")
            datetime_hour = datetime.strftime(datetime.strptime(value[3], '%Y-%m-%d %H:%M:%S'), "%H:%M:%S")
        else:
            datetime_date = None
            datetime_hour = None
        record = {
            'station_id': value[0],
            'shortname': value[1],
            'beach_name': value[2],
            'datetime_date': datetime_date,
            'datetime_hour': datetime_hour,
            'weather': value[4],
            'wd_deg': value[5],
            'wd_card': value[6],
            'ws_kt': value[7],
            'wave_deg': value[8],
            'wave_direction': value[9],
            'wave_height_meter': value[10],
            'batch_time': value[11]
        }
        maritim_wisata_bahari.append(record)
    cursor.close()
    connection.close()
    return render(request, 'maritim_wisata_bahari.html', {'maritim_wisata_bahari': maritim_wisata_bahari})


def maritim_wisata_bahari_info(request):
    """
    Maritim Wisata Bahari Info
    """
    maritim_wisata_bahari_info = []

    # Connect to databases
    SQLITE_DB = settings.DATABASES['bmkg_mqtt']['NAME']
    connection = sqlite3.connect(SQLITE_DB)
    cursor = connection.cursor()
    query = (
        "SELECT station_id, shortname, timestamp, beach_id, beach_name, "
        "weather, wd_card, wd_card, "
        "ws_kt, ws_kt, wave_height_meter, wave_height_meter, wave_height_description, batch_time "
        "FROM maritim_wisata_bahari WHERE batch_time = "
        "(SELECT MAX(batch_time) FROM maritim_wisata_bahari) "
        "ORDER BY batch_time DESC, shortname "
    )
    cursor.execute(query)
    stasion = {}
    last_station_id = None
    cur_stasion_id = None
    # Append Record
    for value in cursor:
        cur_stasion_id = value[0]
        if last_station_id and last_station_id != cur_stasion_id:
            maritim_wisata_bahari_info.append(stasion)
            stasion = {}
        timestamp_1 = datetime.strptime(value[2], '%Y-%m-%d %H:%M:%S')
        if value[13]:
            batch_time = datetime.strptime(value[13], '%Y-%m-%d %H:%M:%S.%f')
            batch_time = get_timestampfull(batch_time)
        else:
            batch_time = None
        try:
            # weather_icon = value[5].lower() + '-am.png'
            weather_icon = weather_image(str(value[5]), "am")
        except:
            weather_icon = None
        record = {
            'station_id': value[0],
            'shortname': value[1],
            'timestamp_1': get_timestamp(timestamp_1),
            'area_id': value[3],
            'area_name_id': value[4],
            'weather': weather_icon[:-7],
            'wd_card': wind_direction(value[6]),
            'wd_card': wind_direction(value[7]),
            'ws_kt': value[8],
            'ws_kt': value[9],
            'wave_height_meter': value[10],
            'wave_height_meter': value[11],
            'wave_height_description': value[12],
            'batch_time': batch_time,
            'weather_icon': weather_icon,
        }
        stasion.update({value[3]: record})
        last_station_id = value[0]
    # Last Append
    maritim_wisata_bahari_info.append(stasion)
    context = {
        'maritim_wisata_bahari_info': maritim_wisata_bahari_info,
        'batch_time': batch_time
    }

    cursor.close()
    connection.close()
    return render(request, 'maritim_wisata_bahari_info.html', context)


def digital_forecast(request):
    """
    Digital Forecast
    """
    digital_forecast = []

    # Connect to databases
    SQLITE_DB = settings.DATABASES['bmkg_mqtt']['NAME']
    connection = sqlite3.connect(SQLITE_DB)
    cursor = connection.cursor()
    latest = request.GET.get('latest')
    if settings.SHOW_AREA_ID:
        area_id = settings.SHOW_AREA_ID
        if latest:
            query = (
                "SELECT area_id, area_domain, area_name_en, timestamp, "
                "weather_00, weather_06, weather_12, weather_18, "
                "weather_24, weather_30, weather_36, weather_42, "
                "humin_1, humax_1, humin_2, humax_2, "
                "tmin_1_c, tmax_1_c, tmin_2_c, tmax_2_c, batch_time "
                "FROM digital_forecast WHERE area_id = '%s' AND "
                "batch_time = (SELECT MAX(batch_time) FROM digital_forecast) "
                "ORDER BY batch_time DESC" % str(area_id)
            )
        else:
            query = (
                "SELECT area_id, area_domain, area_name_en, timestamp, "
                "weather_00, weather_06, weather_12, weather_18, "
                "weather_24, weather_30, weather_36, weather_42, "
                "humin_1, humax_1, humin_2, humax_2, "
                "tmin_1_c, tmax_1_c, tmin_2_c, tmax_2_c, batch_time "
                "FROM digital_forecast WHERE area_id = '%s' ORDER BY batch_time DESC" % str(area_id)
            )
    else:
        if latest:
            query = (
                "SELECT area_id, area_domain, area_name_en, timestamp, "
                "weather_00, weather_06, weather_12, weather_18, "
                "weather_24, weather_30, weather_36, weather_42, "
                "humin_1, humax_1, humin_2, humax_2, "
                "tmin_1_c, tmax_1_c, tmin_2_c, tmax_2_c, batch_time "
                "FROM digital_forecast WHERE batch_time = (SELECT MAX(batch_time) FROM digital_forecast) "
                "ORDER BY batch_time DESC "
            )
        else:
            query = (
                "SELECT area_id, area_domain, area_name_en, timestamp, "
                "weather_00, weather_06, weather_12, weather_18, "
                "weather_24, weather_30, weather_36, weather_42, "
                "humin_1, humax_1, humin_2, humax_2, "
                "tmin_1_c, tmax_1_c, tmin_2_c, tmax_2_c, batch_time "
                "FROM digital_forecast ORDER BY batch_time DESC "
            )
    cursor.execute(query)

    # Append Record
    for value in cursor:
        if value[3]:
            timestamp_1 = datetime.strftime(datetime.strptime(value[3], '%Y-%m-%d %H:%M:%S'), "%d/%m/%Y")
            timestamp_2 = datetime.strftime(datetime.strptime(value[3], '%Y-%m-%d %H:%M:%S') + timedelta(days=1), "%d/%m/%Y")
        else:
            timestamp_1 = None
            timestamp_2 = None

        record = {
            'area_id': value[0],
            'area_domain': value[1],
            'area_name_en': value[2],
            'timestamp_1': timestamp_1,
            'timestamp_2': timestamp_2,
            'weather_00': weather_image(str(value[4]), 'am'),
            'weather_06': weather_image(str(value[5]), 'am'),
            'weather_12': weather_image(str(value[6]), 'pm'),
            'weather_18': weather_image(str(value[7]), 'pm'),
            'weather_24': weather_image(str(value[8]), 'am'),
            'weather_30': weather_image(str(value[9]), 'am'),
            'weather_36': weather_image(str(value[10]), 'pm'),
            'weather_42': weather_image(str(value[11]), 'pm'),
            'humin_1': value[12],
            'humax_1': value[13],
            'humin_2': value[14],
            'humax_2': value[15],
            'tmin_1_c': value[16],
            'tmax_1_c': value[17],
            'tmin_2_c': value[18],
            'tmax_2_c': value[19],
            'batch_time': value[20]
        }
        digital_forecast.append(record)
    cursor.close()
    connection.close()
    return render(request, 'digital_forecast.html', {'digital_forecast': digital_forecast})


def digital_forecast_info(request):
    """
    Digital Forecast Info
    """
    digital_forecast_info = []

    # Connect to databases
    SQLITE_DB = settings.DATABASES['bmkg_mqtt']['NAME']
    connection = sqlite3.connect(SQLITE_DB)
    cursor = connection.cursor()
    if settings.SHOW_AREA_ID:
        area_id = settings.SHOW_AREA_ID
        query = (
            "SELECT area_id, area_domain, area_name_en, timestamp, "
            "weather_00, weather_06, weather_12, weather_18, "
            "weather_24, weather_30, weather_36, weather_42, batch_time "
            "FROM digital_forecast WHERE area_id = '%s' AND "
            "batch_time = (SELECT MAX(batch_time) FROM digital_forecast) "
            "ORDER BY batch_time DESC" % str(area_id)
        )
    else:
        query = (
            "SELECT area_id, area_domain, area_name_en, timestamp, "
            "weather_00, weather_06, weather_12, weather_18, "
            "weather_24, weather_30, weather_36, weather_42, batch_time "
            "FROM digital_forecast WHERE batch_time = (SELECT MAX(batch_time) FROM digital_forecast) "
            "ORDER BY batch_time DESC "
        )
    cursor.execute(query)

    # Append Record
    for value in cursor:
        if value[3]:
            timestamp_1 = datetime.strptime(value[3], '%Y-%m-%d %H:%M:%S')
            timestamp_1_fmt = get_timestamp(timestamp_1)
            timestamp_2 = datetime.strptime(value[3], '%Y-%m-%d %H:%M:%S') + timedelta(days=1)
            timestamp_2_fmt = get_timestamp(timestamp_2)
        else:
            timestamp_1_fmt = None
            timestamp_2_fmt = None
        if value[12]:
            batch_time = datetime.strptime(value[12], '%Y-%m-%d %H:%M:%S.%f')
            batch_time = get_timestampfull(batch_time)
        else:
            batch_time = None
        record = {
            'area_id': value[0],
            'area_domain': value[1],
            'area_name_en': value[2],
            'timestamp_1': timestamp_1_fmt,
            'timestamp_2': timestamp_2_fmt,
            'weather_00': weather_image(str(value[4]), 'am'),
            'weather_06': weather_image(str(value[5]), 'am'),
            'weather_12': weather_image(str(value[6]), 'pm'),
            'weather_18': weather_image(str(value[7]), 'pm'),
            'weather_24': weather_image(str(value[8]), 'am'),
            'weather_30': weather_image(str(value[9]), 'am'),
            'weather_36': weather_image(str(value[10]), 'pm'),
            'weather_42': weather_image(str(value[11]), 'pm'),
            'batch_time': batch_time
        }
        digital_forecast_info.append(record)
    cursor.close()
    connection.close()
    return render(request, 'digital_forecast_info.html', {'digital_forecast_info': digital_forecast_info})


def digital_forecast_info2(request):
    """
    Digital Forecast Info 2
    """
    digital_forecast_info2 = []

    # Connect to databases
    SQLITE_DB = settings.DATABASES['bmkg_mqtt']['NAME']
    connection = sqlite3.connect(SQLITE_DB)
    cursor = connection.cursor()
    if settings.SHOW_AREA_ID:
        area_id = settings.SHOW_AREA_ID
        query = (
            "SELECT area_id, area_domain, area_name_en, timestamp, "
            "weather_00, weather_06, weather_12, weather_18, "
            "t_00_c, t_06_c, t_12_c, t_18_c, "
            "hu_00, hu_06, hu_12, hu_18, "
            "ws_00_kph, ws_06_kph, ws_12_kph, ws_18_kph, batch_time"
            "humin_1, humax_1, tmin_1_c, tmax_1_c, "
            "wd_00_card, wd_06_card, wd_12_card, wd_18_card "
            "FROM digital_forecast WHERE area_id = '%s' AND "
            "batch_time = (SELECT MAX(batch_time) FROM digital_forecast) "
            "ORDER BY batch_time DESC" % str(area_id)
        )
    else:
        query = (
            "SELECT area_id, area_domain, area_name_en, timestamp, "
            "weather_00, weather_06, weather_12, weather_18, "
            "t_00_c, t_06_c, t_12_c, t_18_c, "
            "hu_00, hu_06, hu_12, hu_18, "
            "ws_00_kph, ws_06_kph, ws_12_kph, ws_18_kph, batch_time, "
            "humin_1, humax_1, tmin_1_c, tmax_1_c, "
            "wd_00_card, wd_06_card, wd_12_card, wd_18_card "
            "FROM digital_forecast WHERE batch_time = (SELECT MAX(batch_time) FROM digital_forecast) "
            "ORDER BY batch_time DESC "
        )
    cursor.execute(query)

    # Append Record
    for value in cursor:
        if value[3]:
            timestamp_1 = datetime.strptime(value[3], '%Y-%m-%d %H:%M:%S')
            timestamp_1_fmt = get_timestamp(timestamp_1)
            timestamp_2 = datetime.strptime(value[3], '%Y-%m-%d %H:%M:%S') + timedelta(days=1)
            timestamp_2_fmt = get_timestamp(timestamp_2)
        else:
            timestamp_1_fmt = None
            timestamp_2_fmt = None
        if value[20]:
            batch_time = datetime.strptime(value[20], '%Y-%m-%d %H:%M:%S.%f')
            batch_time = get_timestampfull(batch_time)
        else:
            batch_time = None
        local_time = datetime.now()
        if local_time.hour >= 0 and local_time.hour < 6:
            time_period = "pagi"
        elif local_time.hour >= 6 and local_time.hour < 12:
            time_period = "siang"
        elif local_time.hour >= 12 and local_time.hour < 18:
            time_period = "malam"
        else:
            time_period = "dini hari"

        record = {
            'area_id': value[0],
            'area_domain': value[1],
            'area_name_en': value[2],
            'timestamp_1': timestamp_1_fmt,
            'timestamp_2': timestamp_2_fmt,
            'weather_00': weather_image(str(value[4]), 'am'),
            'weather_06': weather_image(str(value[5]), 'am'),
            'weather_12': weather_image(str(value[6]), 'pm'),
            'weather_18': weather_image(str(value[7]), 'pm'),
            't_00_c': value[8],
            't_06_c': value[9],
            't_12_c': value[10],
            't_18_c': value[11],
            'hu_00': value[12],
            'hu_06': value[13],
            'hu_12': value[14],
            'hu_18': value[15],
            'ws_00_kph': value[16],
            'ws_06_kph': value[17],
            'ws_12_kph': value[18],
            'ws_18_kph': value[19],
            'batch_time': batch_time,
            'humin_1': value[21],
            'humax_1': value[22],
            'tmin_1_c': value[23],
            'tmax_1_c': value[24],
            'wd_00_name': wind_direction(value[25]),
            'wd_00_card': value[25],
            'wd_06_name': wind_direction(value[26]),
            'wd_06_card': value[26],
            'wd_12_name': wind_direction(value[27]),
            'wd_12_card': value[27],
            'wd_18_name': wind_direction(value[28]),
            'wd_18_card': value[28],
            'time_period': time_period
        }
        digital_forecast_info2.append(record)
    cursor.close()
    connection.close()
    return render(request, 'digital_forecast_info2.html', {'digital_forecast_info2': digital_forecast_info2})


def iklim_kabupaten_csv(request):
    """
    Iklim Kabupaten CSV
    """
    iklim_kabupaten_csv = []

    # Connect to databases
    SQLITE_DB = settings.DATABASES['bmkg_mqtt']['NAME']
    connection = sqlite3.connect(SQLITE_DB)
    cursor = connection.cursor()
    latest = request.GET.get('latest')
    if settings.SHOW_BPS_ID_KAB:
        id_kab = settings.SHOW_BPS_ID_KAB
        if latest:
            query = (
                "SELECT provinsi, id_kabupaten_kota, kabupaten_kota, month, "
                "ach_1_sbk, ach_1_sb, ach_1_sbb, ach_1_m, "
                "ash_1_sbk, ash_1_sb, ash_1_sbb, ash_1_m, "
                "pch_1_sbk, pch_1_sb, pch_1_sbb, pch_1_m, "
                "psh_1_sbk, psh_1_sb, psh_1_sbb, psh_1_m, "
                "pch_2_sbk, pch_2_sb, pch_2_sbb, pch_2_m, "
                "psh_2_sbk, psh_2_sb, psh_2_sbb, psh_2_m, "
                "pch_3_sbk, pch_3_sb, pch_3_sbb, pch_3_m, "
                "psh_3_sbk, psh_3_sb, psh_3_sbb, psh_3_m, batch_time "
                "FROM iklim_kabupaten_csv WHERE id_kabupaten_kota = '%s' "
                "AND batch_time = (SELECT MAX(batch_time) from iklim_kabupaten_csv) "
                "ORDER BY batch_time DESC" % str(id_kab)
            )
        else:
            query = (
                "SELECT provinsi, id_kabupaten_kota, kabupaten_kota, month, "
                "ach_1_sbk, ach_1_sb, ach_1_sbb, ach_1_m, "
                "ash_1_sbk, ash_1_sb, ash_1_sbb, ash_1_m, "
                "pch_1_sbk, pch_1_sb, pch_1_sbb, pch_1_m, "
                "psh_1_sbk, psh_1_sb, psh_1_sbb, psh_1_m, "
                "pch_2_sbk, pch_2_sb, pch_2_sbb, pch_2_m, "
                "psh_2_sbk, psh_2_sb, psh_2_sbb, psh_2_m, "
                "pch_3_sbk, pch_3_sb, pch_3_sbb, pch_3_m, "
                "psh_3_sbk, psh_3_sb, psh_3_sbb, psh_3_m, batch_time "
                "FROM iklim_kabupaten_csv WHERE id_kabupaten_kota = '%s' ORDER BY batch_time DESC" % str(id_kab)
            )
    else:
        if latest:
            query = (
                "SELECT provinsi, id_kabupaten_kota, kabupaten_kota, month, "
                "ach_1_sbk, ach_1_sb, ach_1_sbb, ach_1_m, "
                "ash_1_sbk, ash_1_sb, ash_1_sbb, ash_1_m, "
                "pch_1_sbk, pch_1_sb, pch_1_sbb, pch_1_m, "
                "psh_1_sbk, psh_1_sb, psh_1_sbb, psh_1_m, "
                "pch_2_sbk, pch_2_sb, pch_2_sbb, pch_2_m, "
                "psh_2_sbk, psh_2_sb, psh_2_sbb, psh_2_m, "
                "pch_3_sbk, pch_3_sb, pch_3_sbb, pch_3_m, "
                "psh_3_sbk, psh_3_sb, psh_3_sbb, psh_3_m, batch_time "
                "FROM iklim_kabupaten_csv WHERE batch_time = "
                "(SELECT MAX(batch_time) FROM iklim_kabupaten_csv) ORDER BY batch_time DESC "
            )
        else:
            query = (
                "SELECT provinsi, id_kabupaten_kota, kabupaten_kota, month, "
                "ach_1_sbk, ach_1_sb, ach_1_sbb, ach_1_m, "
                "ash_1_sbk, ash_1_sb, ash_1_sbb, ash_1_m, "
                "pch_1_sbk, pch_1_sb, pch_1_sbb, pch_1_m, "
                "psh_1_sbk, psh_1_sb, psh_1_sbb, psh_1_m, "
                "pch_2_sbk, pch_2_sb, pch_2_sbb, pch_2_m, "
                "psh_2_sbk, psh_2_sb, psh_2_sbb, psh_2_m, "
                "pch_3_sbk, pch_3_sb, pch_3_sbb, pch_3_m, "
                "psh_3_sbk, psh_3_sb, psh_3_sbb, psh_3_m, batch_time "
                "FROM iklim_kabupaten_csv ORDER BY batch_time DESC "
            )
    cursor.execute(query)

    # Append Record
    for value in cursor:
        record = {
            'provinsi': value[0],
            'id_kabupaten_kota': value[1],
            'kabupaten_kota': value[2],
            'month': value[3],
            'ach_1_sbk': value[4],
            'ach_1_sb': value[5],
            'ach_1_sbb': value[6],
            'ach_1_m': value[7],
            'ash_1_sbk': value[8],
            'ash_1_sb': value[9],
            'ash_1_sbb': value[10],
            'ash_1_m': value[11],
            'pch_1_sbk': value[12],
            'pch_1_sb': value[13],
            'pch_1_sbb': value[14],
            'pch_1_m': value[15],
            'psh_1_sbk': value[16],
            'psh_1_sb': value[17],
            'psh_1_sbb': value[18],
            'psh_1_m': value[19],
            'pch_2_sbk': value[20],
            'pch_2_sb': value[21],
            'pch_2_sbb': value[22],
            'pch_2_m': value[23],
            'psh_2_sbk': value[24],
            'psh_2_sb': value[25],
            'psh_2_sbb': value[26],
            'psh_2_m': value[27],
            'pch_3_sbk': value[28],
            'pch_3_sb': value[29],
            'pch_3_sbb': value[30],
            'pch_3_m': value[31],
            'psh_3_sbk': value[32],
            'psh_3_sb': value[33],
            'psh_3_sbb': value[34],
            'psh_3_m': value[35],
            'batch_time': value[36]
        }
        iklim_kabupaten_csv.append(record)
    cursor.close()
    connection.close()
    return render(request, 'iklim_kabupaten_csv.html', {'iklim_kabupaten_csv': iklim_kabupaten_csv})


def iklim_kabupaten_csv_info(request):
    """
    Iklim Kabupaten CSV Info
    """
    iklim_kabupaten_csv_info = []

    # Connect to databases
    SQLITE_DB = settings.DATABASES['bmkg_mqtt']['NAME']
    connection = sqlite3.connect(SQLITE_DB)
    cursor = connection.cursor()
    if settings.SHOW_BPS_ID_KAB:
        id_kab = settings.SHOW_BPS_ID_KAB
        query = (
            "SELECT provinsi, id_kabupaten_kota, kabupaten_kota, month, year, batch_time, "
            "pch_1_sbk, pch_1_sb, pch_1_sbb, pch_1_m, "
            "pch_2_sbk, pch_2_sb, pch_2_sbb, pch_2_m, "
            "pch_3_sbk, pch_3_sb, pch_3_sbb, pch_3_m "
            "FROM iklim_kabupaten_csv WHERE id_kabupaten_kota = '%s' "
            "AND batch_time = (SELECT MAX(batch_time) from iklim_kabupaten_csv) "
            "ORDER BY batch_time DESC" % str(id_kab)
        )
    else:
        query = (
            "SELECT provinsi, id_kabupaten_kota, kabupaten_kota, month, year, batch_time, "
            "pch_1_sbk, pch_1_sb, pch_1_sbb, pch_1_m, "
            "pch_2_sbk, pch_2_sb, pch_2_sbb, pch_2_m, "
            "pch_3_sbk, pch_3_sb, pch_3_sbb, pch_3_m "
            "FROM iklim_kabupaten_csv WHERE batch_time = "
            "(SELECT MAX(batch_time) FROM iklim_kabupaten_csv) ORDER BY batch_time DESC "
        )
    cursor.execute(query)

    # Append Record
    for value in cursor:
        pch_1_value = {}
        pch_1_sbk = ast.literal_eval(value[6])
        pch_1_sb = ast.literal_eval(value[7])
        pch_1_sbb = ast.literal_eval(value[8])
        pch_1_m = ast.literal_eval(value[9])
        pch_1_value.update(pch_1_sbk)
        pch_1_value.update(pch_1_sb)
        pch_1_value.update(pch_1_sbb)
        pch_1_value.update(pch_1_m)
        pch_1_value = get_category(pch_1_value)
        pch_2_value = {}
        pch_2_sbk = ast.literal_eval(value[10])
        pch_2_sb = ast.literal_eval(value[11])
        pch_2_sbb = ast.literal_eval(value[12])
        pch_2_m = ast.literal_eval(value[13])
        pch_2_value.update(pch_2_sbk)
        pch_2_value.update(pch_2_sb)
        pch_2_value.update(pch_2_sbb)
        pch_2_value.update(pch_2_m)
        pch_2_value = get_category(pch_2_value)
        pch_3_value = {}
        pch_3_sbk = ast.literal_eval(value[14])
        pch_3_sb = ast.literal_eval(value[15])
        pch_3_sbb = ast.literal_eval(value[16])
        pch_3_m = ast.literal_eval(value[17])
        pch_3_value.update(pch_3_sbk)
        pch_3_value.update(pch_3_sb)
        pch_3_value.update(pch_3_sbb)
        pch_3_value.update(pch_3_m)
        pch_3_value = get_category(pch_3_value)
        if value[5]:
            batch_time = datetime.strptime(value[5], '%Y-%m-%d %H:%M:%S.%f')
            batch_time = get_timestampfull(batch_time)
        else:
            batch_time = None
        record = {
            'provinsi': value[0],
            'id_kabupaten_kota': value[1],
            'kabupaten_kota': value[2],
            'month_year_1': get_month_year(value[3] + 1, value[4]),
            'month_year_2': get_month_year(value[3] + 2, value[4]),
            'month_year_3': get_month_year(value[3] + 3, value[4]),
            'batch_time': batch_time,
            'pch_1_value': sorted(pch_1_value.items(), key=operator.itemgetter(1), reverse=True),
            'pch_2_value': sorted(pch_2_value.items(), key=operator.itemgetter(1), reverse=True),
            'pch_3_value': sorted(pch_3_value.items(), key=operator.itemgetter(1), reverse=True),
        }
        iklim_kabupaten_csv_info.append(record)
    cursor.close()
    connection.close()
    return render(request, 'iklim_kabupaten_csv_info.html', {'iklim_kabupaten_csv_info': iklim_kabupaten_csv_info})


def iklim_kecamatan_csv(request):
    """
    Iklim Kecamatan CSV
    """
    iklim_kecamatan_csv = []

    # Connect to databases
    SQLITE_DB = settings.DATABASES['bmkg_mqtt']['NAME']
    connection = sqlite3.connect(SQLITE_DB)
    cursor = connection.cursor()
    latest = request.GET.get('latest')
    if settings.SHOW_BPS_ID_KEC:
        id_kec = settings.SHOW_BPS_ID_KEC
        if latest:
            query = (
                "SELECT provinsi, id_kabupaten_kota, kabupaten_kota, id_kecamatan, kecamatan, month, "
                "ach_1_sbk, ach_1_sb, ach_1_sbb, ach_1_m, "
                "ash_1_sbk, ash_1_sb, ash_1_sbb, ash_1_m, "
                "pch_1_sbk, pch_1_sb, pch_1_sbb, pch_1_m, "
                "psh_1_sbk, psh_1_sb, psh_1_sbb, psh_1_m, "
                "pch_2_sbk, pch_2_sb, pch_2_sbb, pch_2_m, "
                "psh_2_sbk, psh_2_sb, psh_2_sbb, psh_2_m, "
                "pch_3_sbk, pch_3_sb, pch_3_sbb, pch_3_m, "
                "psh_3_sbk, psh_3_sb, psh_3_sbb, psh_3_m, batch_time "
                "FROM iklim_kecamatan_csv WHERE id_kecamatan = '%s' "
                "AND batch_time = (SELECT MAX(batch_time) FROM iklim_kecamatan_csv) "
                "ORDER BY batch_time DESC" % str(id_kec)
            )
        else:
            query = (
                "SELECT provinsi, id_kabupaten_kota, kabupaten_kota, id_kecamatan, kecamatan, month, "
                "ach_1_sbk, ach_1_sb, ach_1_sbb, ach_1_m, "
                "ash_1_sbk, ash_1_sb, ash_1_sbb, ash_1_m, "
                "pch_1_sbk, pch_1_sb, pch_1_sbb, pch_1_m, "
                "psh_1_sbk, psh_1_sb, psh_1_sbb, psh_1_m, "
                "pch_2_sbk, pch_2_sb, pch_2_sbb, pch_2_m, "
                "psh_2_sbk, psh_2_sb, psh_2_sbb, psh_2_m, "
                "pch_3_sbk, pch_3_sb, pch_3_sbb, pch_3_m, "
                "psh_3_sbk, psh_3_sb, psh_3_sbb, psh_3_m, batch_time "
                "FROM iklim_kecamatan_csv WHERE id_kecamatan = '%s' ORDER BY batch_time DESC" % str(id_kec)
            )
    else:
        if latest:
           query = (
                "SELECT provinsi, id_kabupaten_kota, kabupaten_kota, id_kecamatan, kecamatan, month, "
                "ach_1_sbk, ach_1_sb, ach_1_sbb, ach_1_m, "
                "ash_1_sbk, ash_1_sb, ash_1_sbb, ash_1_m, "
                "pch_1_sbk, pch_1_sb, pch_1_sbb, pch_1_m, "
                "psh_1_sbk, psh_1_sb, psh_1_sbb, psh_1_m, "
                "pch_2_sbk, pch_2_sb, pch_2_sbb, pch_2_m, "
                "psh_2_sbk, psh_2_sb, psh_2_sbb, psh_2_m, "
                "pch_3_sbk, pch_3_sb, pch_3_sbb, pch_3_m, "
                "psh_3_sbk, psh_3_sb, psh_3_sbb, psh_3_m, batch_time "
                "FROM iklim_kecamatan_csv WHERE batch_time = "
                "(SELECT MAX(batch_time) FROM iklim_kecamatan_csv) ORDER BY batch_time DESC "
            ) 
        else:
            query = (
                "SELECT provinsi, id_kabupaten_kota, kabupaten_kota, id_kecamatan, kecamatan, month, "
                "ach_1_sbk, ach_1_sb, ach_1_sbb, ach_1_m, "
                "ash_1_sbk, ash_1_sb, ash_1_sbb, ash_1_m, "
                "pch_1_sbk, pch_1_sb, pch_1_sbb, pch_1_m, "
                "psh_1_sbk, psh_1_sb, psh_1_sbb, psh_1_m, "
                "pch_2_sbk, pch_2_sb, pch_2_sbb, pch_2_m, "
                "psh_2_sbk, psh_2_sb, psh_2_sbb, psh_2_m, "
                "pch_3_sbk, pch_3_sb, pch_3_sbb, pch_3_m, "
                "psh_3_sbk, psh_3_sb, psh_3_sbb, psh_3_m, batch_time "
                "FROM iklim_kecamatan_csv ORDER BY batch_time DESC "
            )
    cursor.execute(query)

    # Append Record
    for value in cursor:
        record = {
            'provinsi': value[0],
            'id_kabupaten_kota': value[1],
            'kabupaten_kota': value[2],
            'id_kecamatan': value[3],
            'kecamatan': value[4],
            'month': value[5],
            'ach_1_sbk': value[6],
            'ach_1_sb': value[7],
            'ach_1_sbb': value[8],
            'ach_1_m': value[9],
            'ash_1_sbk': value[10],
            'ash_1_sb': value[11],
            'ash_1_sbb': value[12],
            'ash_1_m': value[13],
            'pch_1_sbk': value[14],
            'pch_1_sb': value[15],
            'pch_1_sbb': value[16],
            'pch_1_m': value[17],
            'psh_1_sbk': value[18],
            'psh_1_sb': value[19],
            'psh_1_sbb': value[20],
            'psh_1_m': value[21],
            'pch_2_sbk': value[22],
            'pch_2_sb': value[23],
            'pch_2_sbb': value[24],
            'pch_2_m': value[25],
            'psh_2_sbk': value[26],
            'psh_2_sb': value[27],
            'psh_2_sbb': value[28],
            'psh_2_m': value[29],
            'pch_3_sbk': value[30],
            'pch_3_sb': value[31],
            'pch_3_sbb': value[32],
            'pch_3_m': value[33],
            'psh_3_sbk': value[34],
            'psh_3_sb': value[35],
            'psh_3_sbb': value[36],
            'psh_3_m': value[37],
            'batch_time': value[38]
        }
        iklim_kecamatan_csv.append(record)
    cursor.close()
    connection.close()
    return render(request, 'iklim_kecamatan_csv.html', {'iklim_kecamatan_csv': iklim_kecamatan_csv})


def iklim_kecamatan_csv_info(request):
    """
    Iklim Kecamatan CSV Info
    """
    iklim_kecamatan_csv_info = []

    # Connect to databases
    SQLITE_DB = settings.DATABASES['bmkg_mqtt']['NAME']
    connection = sqlite3.connect(SQLITE_DB)
    cursor = connection.cursor()
    if settings.SHOW_BPS_ID_KEC:
        id_kec = settings.SHOW_BPS_ID_KEC
        query = (
            "SELECT provinsi, id_kecamatan, kecamatan, month, year, batch_time, "
            "pch_1_sbk, pch_1_sb, pch_1_sbb, pch_1_m, "
            "pch_2_sbk, pch_2_sb, pch_2_sbb, pch_2_m, "
            "pch_3_sbk, pch_3_sb, pch_3_sbb, pch_3_m "
            "FROM iklim_kecamatan_csv WHERE id_kecamatan = '%s' "
            "AND batch_time = (SELECT MAX(batch_time) from iklim_kecamatan_csv) "
            "ORDER BY batch_time DESC" % str(id_kec)
        )
    else:
        query = (
            "SELECT provinsi, id_kecamatan, kecamatan, month, year, batch_time, "
            "pch_1_sbk, pch_1_sb, pch_1_sbb, pch_1_m, "
            "pch_2_sbk, pch_2_sb, pch_2_sbb, pch_2_m, "
            "pch_3_sbk, pch_3_sb, pch_3_sbb, pch_3_m "
            "FROM iklim_kecamatan_csv WHERE batch_time = "
            "(SELECT MAX(batch_time) FROM iklim_kecamatan_csv) ORDER BY batch_time DESC "
        )
    cursor.execute(query)

    # Append Record
    for value in cursor:
        pch_1_value = {}
        pch_1_sbk = ast.literal_eval(value[6])
        pch_1_sb = ast.literal_eval(value[7])
        pch_1_sbb = ast.literal_eval(value[8])
        pch_1_m = ast.literal_eval(value[9])
        pch_1_value.update(pch_1_sbk)
        pch_1_value.update(pch_1_sb)
        pch_1_value.update(pch_1_sbb)
        pch_1_value.update(pch_1_m)
        pch_1_value = get_category(pch_1_value)
        pch_2_value = {}
        pch_2_sbk = ast.literal_eval(value[10])
        pch_2_sb = ast.literal_eval(value[11])
        pch_2_sbb = ast.literal_eval(value[12])
        pch_2_m = ast.literal_eval(value[13])
        pch_2_value.update(pch_2_sbk)
        pch_2_value.update(pch_2_sb)
        pch_2_value.update(pch_2_sbb)
        pch_2_value.update(pch_2_m)
        pch_2_value = get_category(pch_2_value)
        pch_3_value = {}
        pch_3_sbk = ast.literal_eval(value[14])
        pch_3_sb = ast.literal_eval(value[15])
        pch_3_sbb = ast.literal_eval(value[16])
        pch_3_m = ast.literal_eval(value[17])
        pch_3_value.update(pch_3_sbk)
        pch_3_value.update(pch_3_sb)
        pch_3_value.update(pch_3_sbb)
        pch_3_value.update(pch_3_m)
        pch_3_value = get_category(pch_3_value)
        if value[5]:
            batch_time = datetime.strptime(value[5], '%Y-%m-%d %H:%M:%S.%f')
            batch_time = get_timestampfull(batch_time)
        else:
            batch_time = None
        record = {
            'provinsi': value[0],
            'id_kecamatan': value[1],
            'kecamatan': value[2],
            'month_year_1': get_month_year(value[3] + 1, value[4]),
            'month_year_2': get_month_year(value[3] + 2, value[4]),
            'month_year_3': get_month_year(value[3] + 3, value[4]),
            'batch_time': batch_time,
            'pch_1_value': sorted(pch_1_value.items(), key=operator.itemgetter(1), reverse=True),
            'pch_2_value': sorted(pch_2_value.items(), key=operator.itemgetter(1), reverse=True),
            'pch_3_value': sorted(pch_3_value.items(), key=operator.itemgetter(1), reverse=True),
        }
        iklim_kecamatan_csv_info.append(record)
    cursor.close()
    connection.close()
    return render(request, 'iklim_kecamatan_csv_info.html', {'iklim_kecamatan_csv_info': iklim_kecamatan_csv_info})


def iklim_desa_csv(request):
    """
    Iklim Desa CSV
    """
    iklim_desa_csv = []

    # Connect to databases
    SQLITE_DB = settings.DATABASES['bmkg_mqtt']['NAME']
    connection = sqlite3.connect(SQLITE_DB)
    cursor = connection.cursor()
    latest = request.GET.get('latest')
    if settings.SHOW_BPS_ID_DES:
        id_des = settings.SHOW_BPS_ID_DES
        if latest:
            query = (
                "SELECT provinsi, id_kabupaten_kota, kabupaten_kota, id_kecamatan, kecamatan, id_desa, desa, month, "
                "ach_1_sbk, ach_1_sb, ach_1_sbb, ach_1_m, "
                "ash_1_sbk, ash_1_sb, ash_1_sbb, ash_1_m, "
                "pch_1_sbk, pch_1_sb, pch_1_sbb, pch_1_m, "
                "psh_1_sbk, psh_1_sb, psh_1_sbb, psh_1_m, "
                "pch_2_sbk, pch_2_sb, pch_2_sbb, pch_2_m, "
                "psh_2_sbk, psh_2_sb, psh_2_sbb, psh_2_m, "
                "pch_3_sbk, pch_3_sb, pch_3_sbb, pch_3_m, "
                "psh_3_sbk, psh_3_sb, psh_3_sbb, psh_3_m, batch_time "
                "FROM iklim_desa_csv ASC WHERE id_desa = '%s' AND "
                "batch_time = (select MAX(batch_time) FROM iklim_desa_csv)" % str(id_des)
            )
        else:
            query = (
                "SELECT provinsi, id_kabupaten_kota, kabupaten_kota, id_kecamatan, kecamatan, id_desa, desa, month, "
                "ach_1_sbk, ach_1_sb, ach_1_sbb, ach_1_m, "
                "ash_1_sbk, ash_1_sb, ash_1_sbb, ash_1_m, "
                "pch_1_sbk, pch_1_sb, pch_1_sbb, pch_1_m, "
                "psh_1_sbk, psh_1_sb, psh_1_sbb, psh_1_m, "
                "pch_2_sbk, pch_2_sb, pch_2_sbb, pch_2_m, "
                "psh_2_sbk, psh_2_sb, psh_2_sbb, psh_2_m, "
                "pch_3_sbk, pch_3_sb, pch_3_sbb, pch_3_m, "
                "psh_3_sbk, psh_3_sb, psh_3_sbb, psh_3_m, batch_time "
                "FROM iklim_desa_csv ASC WHERE id_desa = '%s'" % str(id_des)
            )
    else:
        if latest:
            query = (
                "SELECT provinsi, id_kabupaten_kota, kabupaten_kota, id_kecamatan, kecamatan, id_desa, desa, month, "
                "ach_1_sbk, ach_1_sb, ach_1_sbb, ach_1_m, "
                "ash_1_sbk, ash_1_sb, ash_1_sbb, ash_1_m, "
                "pch_1_sbk, pch_1_sb, pch_1_sbb, pch_1_m, "
                "psh_1_sbk, psh_1_sb, psh_1_sbb, psh_1_m, "
                "pch_2_sbk, pch_2_sb, pch_2_sbb, pch_2_m, "
                "psh_2_sbk, psh_2_sb, psh_2_sbb, psh_2_m, "
                "pch_3_sbk, pch_3_sb, pch_3_sbb, pch_3_m, "
                "psh_3_sbk, psh_3_sb, psh_3_sbb, psh_3_m, batch_time "
                "FROM iklim_desa_csv ASC WHERE batch_time = (SELECT MAX(batch_time) FROM iklim_desa_csv)"
            )
        else:
            query = (
                "SELECT provinsi, id_kabupaten_kota, kabupaten_kota, id_kecamatan, kecamatan, id_desa, desa, month, "
                "ach_1_sbk, ach_1_sb, ach_1_sbb, ach_1_m, "
                "ash_1_sbk, ash_1_sb, ash_1_sbb, ash_1_m, "
                "pch_1_sbk, pch_1_sb, pch_1_sbb, pch_1_m, "
                "psh_1_sbk, psh_1_sb, psh_1_sbb, psh_1_m, "
                "pch_2_sbk, pch_2_sb, pch_2_sbb, pch_2_m, "
                "psh_2_sbk, psh_2_sb, psh_2_sbb, psh_2_m, "
                "pch_3_sbk, pch_3_sb, pch_3_sbb, pch_3_m, "
                "psh_3_sbk, psh_3_sb, psh_3_sbb, psh_3_m, batch_time "
                "FROM iklim_desa_csv ASC "
            )
    cursor.execute(query)

    # Append Record
    for value in cursor:
        record = {
            'provinsi': value[0],
            'id_kabupaten_kota': value[1],
            'kabupaten_kota': value[2],
            'id_kecamatan': value[3],
            'kecamatan': value[4],
            'id_desa': int(float(value[5])),
            'desa': value[6],
            'month': value[7],
            'ach_1_sbk': value[8],
            'ach_1_sb': value[9],
            'ach_1_sbb': value[10],
            'ach_1_m': value[11],
            'ash_1_sbk': value[12],
            'ash_1_sb': value[13],
            'ash_1_sbb': value[14],
            'ash_1_m': value[15],
            'pch_1_sbk': value[16],
            'pch_1_sb': value[17],
            'pch_1_sbb': value[18],
            'pch_1_m': value[19],
            'psh_1_sbk': value[20],
            'psh_1_sb': value[21],
            'psh_1_sbb': value[22],
            'psh_1_m': value[23],
            'pch_2_sbk': value[24],
            'pch_2_sb': value[25],
            'pch_2_sbb': value[26],
            'pch_2_m': value[27],
            'psh_2_sbk': value[28],
            'psh_2_sb': value[29],
            'psh_2_sbb': value[30],
            'psh_2_m': value[31],
            'pch_3_sbk': value[32],
            'pch_3_sb': value[33],
            'pch_3_sbb': value[34],
            'pch_3_m': value[35],
            'psh_3_sbk': value[36],
            'psh_3_sb': value[37],
            'psh_3_sbb': value[38],
            'psh_3_m': value[39],
            'batch_time': value[40]
        }
        iklim_desa_csv.append(record)
    cursor.close()
    connection.close()
    return render(request, 'iklim_desa_csv.html', {'iklim_desa_csv': iklim_desa_csv})


def iklim_desa_csv_info(request):
    """
    Iklim Desa CSV Info
    """
    iklim_desa_csv_info = []

    # Connect to databases
    SQLITE_DB = settings.DATABASES['bmkg_mqtt']['NAME']
    connection = sqlite3.connect(SQLITE_DB)
    cursor = connection.cursor()
    if settings.SHOW_BPS_ID_DES:
        id_des = settings.SHOW_BPS_ID_DES
        query = (
            "SELECT provinsi, id_desa, desa, month, year, batch_time, "
            "pch_1_sbk, pch_1_sb, pch_1_sbb, pch_1_m, "
            "pch_2_sbk, pch_2_sb, pch_2_sbb, pch_2_m, "
            "pch_3_sbk, pch_3_sb, pch_3_sbb, pch_3_m "
            "FROM iklim_desa_csv WHERE id_desa = '%s' "
            "AND batch_time = (SELECT MAX(batch_time) from iklim_desa_csv) "
            "ORDER BY batch_time DESC" % str(id_des)
        )
    else:
        query = (
            "SELECT provinsi, id_desa, desa, month, year, batch_time, "
            "pch_1_sbk, pch_1_sb, pch_1_sbb, pch_1_m, "
            "pch_2_sbk, pch_2_sb, pch_2_sbb, pch_2_m, "
            "pch_3_sbk, pch_3_sb, pch_3_sbb, pch_3_m "
            "FROM iklim_desa_csv WHERE batch_time = "
            "(SELECT MAX(batch_time) FROM iklim_desa_csv) ORDER BY batch_time DESC "
        )
    cursor.execute(query)

    # Append Record
    for value in cursor:
        pch_1_value = {}
        pch_1_sbk = ast.literal_eval(value[6])
        pch_1_sb = ast.literal_eval(value[7])
        pch_1_sbb = ast.literal_eval(value[8])
        pch_1_m = ast.literal_eval(value[9])
        pch_1_value.update(pch_1_sbk)
        pch_1_value.update(pch_1_sb)
        pch_1_value.update(pch_1_sbb)
        pch_1_value.update(pch_1_m)
        pch_1_value = get_category(pch_1_value)
        pch_2_value = {}
        pch_2_sbk = ast.literal_eval(value[10])
        pch_2_sb = ast.literal_eval(value[11])
        pch_2_sbb = ast.literal_eval(value[12])
        pch_2_m = ast.literal_eval(value[13])
        pch_2_value.update(pch_2_sbk)
        pch_2_value.update(pch_2_sb)
        pch_2_value.update(pch_2_sbb)
        pch_2_value.update(pch_2_m)
        pch_2_value = get_category(pch_2_value)
        pch_3_value = {}
        pch_3_sbk = ast.literal_eval(value[14])
        pch_3_sb = ast.literal_eval(value[15])
        pch_3_sbb = ast.literal_eval(value[16])
        pch_3_m = ast.literal_eval(value[17])
        pch_3_value.update(pch_3_sbk)
        pch_3_value.update(pch_3_sb)
        pch_3_value.update(pch_3_sbb)
        pch_3_value.update(pch_3_m)
        pch_3_value = get_category(pch_3_value)
        if value[5]:
            batch_time = datetime.strptime(value[5], '%Y-%m-%d %H:%M:%S.%f')
            batch_time = get_timestampfull(batch_time)
        else:
            batch_time = None
        record = {
            'provinsi': value[0],
            'id_desa': value[1],
            'desa': value[2],
            'month_year_1': get_month_year(value[3] + 1, value[4]),
            'month_year_2': get_month_year(value[3] + 2, value[4]),
            'month_year_3': get_month_year(value[3] + 3, value[4]),
            'batch_time': batch_time,
            'pch_1_value': sorted(pch_1_value.items(), key=operator.itemgetter(1), reverse=True),
            'pch_2_value': sorted(pch_2_value.items(), key=operator.itemgetter(1), reverse=True),
            'pch_3_value': sorted(pch_3_value.items(), key=operator.itemgetter(1), reverse=True),
        }
        iklim_desa_csv_info.append(record)
    cursor.close()
    connection.close()
    return render(request, 'iklim_desa_csv_info.html', {'iklim_desa_csv_info': iklim_desa_csv_info})
