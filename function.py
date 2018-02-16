"""
Function for http://webdata.bmkg.go.id/ xml parsing.
"""

import urllib2
import datetime
import mysql.connector

from mysql.connector import errorcode, connect

from settings import CONFIG


def databases_connect():
    """ Function to connect databases. """
    try:
        cnx = connect(**CONFIG)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print "Something is wrong with your user name or password"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print "Database does not exist"
        else:
            print err
        cnx = False
    return cnx

def read_xml(url):
    """ Function to read xml from webdata. """
    try:
        xml = urllib2.urlopen(url)
        xml_string = xml.read()
        xml.close()
    except Exception as err:
        print err
        print "This could be wrong url or internet connection problem"
        xml_string = False
    return xml_string

def read_html(url):
    """ Function to read html from webpage. """
    try:
        html = urllib2.urlopen(url)
        html_string = html.read()
        html.close()
    except Exception as err:
        print err
        print "This could be wrong url or internet connection problem"
        html_string = False
    return html_string

def read_csv(url):
    """ Function to read csv from webdata. """
    try:
        csv = urllib2.urlopen(url)
        csv_string = csv.read()
        csv.close()
    except Exception as err:
        print err
        print "This could be wrong url or internet connection problem"
        csv_string = False
    return csv_string

def datetime_converter(date):
    """
        Function to handle datetime is not json serializable error.
        https://code-maven.com/serialize-datetime-object-as-json-in-python
    """
    if isinstance(date, datetime.datetime):
        return date.__str__()

def get_month_name(index):
    """
        Function to get month name in bahasa based on month number
    """
    if index == 13:
        index = 1
    elif index == 14:
        index = 2
    elif index == 15:
        index = 3
    elif index == 0:
        index = 12
    if index == 1:
        monthname = 'Januari'
    elif index == 2:
        monthname = 'Februari'
    elif index == 3:
        monthname = 'Maret'
    elif index == 4:
        monthname = 'April'
    elif index == 5:
        monthname = 'Mei'
    elif index == 6:
        monthname = 'Juni'
    elif index == 7:
        monthname = 'Juli'
    elif index == 8:
        monthname = 'Agustus'
    elif index == 9:
        monthname = 'September'
    elif index == 10:
        monthname = 'Oktober'
    elif index == 11:
        monthname = 'November'
    else:
        monthname = 'Desember'
    return monthname

def sqlite_insert_command(table):
    if table == 'gempa_dirasakan':
        insert_command = (
            "INSERT INTO " + table +
            "(batch_time, tanggal, bujur, lintang, "
            "coordinate, magnitude, magnitude_unit, kedalaman, "
            "kedalaman_unit, symbol, dirasakan, keterangan) "
            "VALUES (:batch_time, :tanggal, :bujur, :lintang, "
            ":coordinate, :magnitude, :magnitude_unit, :kedalaman, "
            ":kedalaman_unit, :symbol, :dirasakan, :keterangan)"
        )
    elif table == 'gempa_terkini':
        insert_command = (
            "INSERT INTO " + table +
            "(batch_time, tanggal, bujur, lintang, "
            "coordinate, magnitude, magnitude_unit, kedalaman, "
            "kedalaman_unit, symbol, wilayah) "
            "VALUES (:batch_time, :tanggal, :bujur, :lintang, "
            ":coordinate, :magnitude, :magnitude_unit, :kedalaman, "
            ":kedalaman_unit, :symbol, :wilayah)"
        )
    elif table == 'gempa_terkini_csv':
        insert_command = (
            "INSERT INTO " + table +
            "(batch_time, src, eqid, datetime, "
            "longitude, latitude, coordinate, magnitude, "
            "depth, region) "
            "VALUES (:batch_time, :src, :eqid, :datetime, "
            ":longitude, :latitude, :coordinate, :magnitude, "
            ":depth, :region)"
        )
    elif table == 'satelit_himawari_8_ir_enhanced':
        insert_command = (
            "INSERT INTO " + table +
            "(batch_time, judul, narasi, lokasi, file) "
            "VALUES (:batch_time, :judul, :narasi, :lokasi, :file)"
        )
    elif table == 'satelit_himawari_8_natural_color' or table == 'satelit_himawari_8_natural_color' or table == 'satelit_hotspot_modis':
        insert_command = (
            "INSERT INTO " + table +
            "(batch_time, judul, narasi, lokasi, file) "
            "VALUES (:batch_time, :judul, :narasi, :lokasi, :file)"
        )
    elif table == 'maritim_cuaca_pelayanan':
        insert_command = (
            "INSERT INTO " + table +
            "(batch_time, domain, station_id, shortname, "
            "timestamp, phone_number, phone_id, email, "
            "address, area_id, area_name, area_description, "
            "area_domain, type, datetime, validfrom, "
            "validto, timezone, weather_id, weather_description, "
            "weather_icon_id_unit, weather_icon_id, "
            "weather_icon_en_unit, weather_icon_en, "
            "wd_from_id, wd_from_description, wd_from_icon_id_unit, "
            "wd_from_icon_en_unit, wd_from_card_unit, "
            "wd_from_icon_id, wd_from_icon_en, wd_from_card, "
            "wd_to_id, wd_to_description, wd_to_icon_en_unit, "
            "wd_to_icon_id_unit, wd_to_card_unit, "
            "wd_to_icon_en, wd_to_icon_id, wd_to_card, "
            "ws_min_id, ws_min_description, ws_min_unit, "
            "ws_min, ws_max_id, ws_max_description, ws_max_unit, "
            "ws_max, wave_min_id, wave_min_description, wave_min_unit, "
            "wave_min, wave_max_id, wave_max_description, wave_max_unit, "
            "wave_max, status_warning_id, status_warning_description, "
            "status_warning_unit, status_warning, "
            "hari, peringatan_dini, kondisi_synoptik)"
            "VALUES (:batch_time, :domain, :station_id, :shortname, "
            ":timestamp, :phone_number, :phone_id, :email, "
            ":address, :area_id, :area_name, :area_description, "
            ":area_domain, :type, :datetime, :validfrom, "
            ":validto, :timezone, :weather_id, :weather_description, "
            ":weather_icon_id_unit, :weather_icon_id, "
            ":weather_icon_en_unit, :weather_icon_en, "
            ":wd_from_id, :wd_from_description, :wd_from_icon_id_unit, "
            ":wd_from_icon_en_unit, :wd_from_card_unit, "
            ":wd_from_icon_id, :wd_from_icon_en , :wd_from_card, "
            ":wd_to_id, :wd_to_description , :wd_to_icon_en_unit, "
            ":wd_to_icon_id_unit, :wd_to_card_unit, "
            ":wd_to_icon_en, :wd_to_icon_id, :wd_to_card, "
            ":ws_min_id, :ws_min_description, :ws_min_unit, "
            ":ws_min, :ws_max_id, :ws_max_description, :ws_max_unit, "
            ":ws_max, :wave_min_id, :wave_min_description, :wave_min_unit, "
            ":wave_min, :wave_max_id, :wave_max_description, :wave_max_unit, "
            ":wave_max, :status_warning_id, :status_warning_description, "
            ":status_warning_unit, :status_warning, "
            ":hari, :peringatan_dini, :kondisi_synoptik)"
        )
    elif table == 'maritim_cuaca_pelabuhan':
        insert_command = (
            "INSERT INTO " + table +
            "(batch_time, domain, station_id, shortname, "
            "timestamp, phone_number, phone_id, email, "
            "address, port_id, port_name, port_description, "
            "port_domain, port_longitude, port_latitude, "
            "port_coordinate, type, datetime, validfrom, "
            "validto, timezone, weather_id, weather_description, "
            "weather_icon_unit, weather_icon, wd_from_id, "
            "wd_from_description, wd_from_icon_id_unit, "
            "wd_from_icon_en_unit, wd_from_icon_card_unit, "
            "wd_from_icon_id, wd_from_icon_en, wd_from_icon_card, "
            "wd_to_id, wd_to_description, wd_to_icon_en_unit, "
            "wd_to_icon_id_unit, wd_to_icon_card_unit, "
            "wd_to_icon_en, wd_to_icon_id, wd_to_icon_card, "
            "ws_min_id, ws_min_description, ws_min_unit, "
            "ws_min, ws_max_id, ws_max_description, ws_max_unit, "
            "ws_max, wave_min_id, wave_min_description, wave_min_unit, "
            "wave_min, wave_max_id, wave_max_description, wave_max_unit, "
            "wave_max, visibility_id, visibility_description, "
            "visibility_unit, visibility, tmin_id, tmin_description, "
            "tmin_unit, tmin, tmax_id, tmax_description, tmax_unit, "
            "tmax, humin_id, humin_description, humin_unit, humin, "
            "humax_id, humax_description, humax_unit, humax, pdf_id, "
            "pdf_description, pdf_unit, pdf, pasang_min_datemin, "
            "pasang_min_datemax, pasang_min_unit, pasang_min_description, "
            "pasang_min_zona, pasang_min, pasang_max_datemin, "
            "pasang_max_datemax, pasang_max_unit, pasang_max_description, "
            "pasang_max_zona, pasang_max, remarks) "
            "VALUES (:batch_time, :domain, :station_id, :shortname, "
            ":timestamp, :phone_number, :phone_id, :email, "
            ":address, :port_id, :port_name, :port_description, "
            ":port_domain, :port_longitude, :port_latitude, "
            ":port_coordinate, :type, :datetime, :validfrom, "
            ":validto, :timezone, :weather_id, :weather_description, "
            ":weather_icon_unit, :weather_icon, :wd_from_id, "
            ":wd_from_description, :wd_from_icon_id_unit, "
            ":wd_from_icon_en_unit, :wd_from_icon_card_unit, "
            ":wd_from_icon_id, :wd_from_icon_en , :wd_from_icon_card, "
            ":wd_to_id, :wd_to_description , :wd_to_icon_en_unit, "
            ":wd_to_icon_id_unit, :wd_to_icon_card_unit, "
            ":wd_to_icon_en, :wd_to_icon_id, :wd_to_icon_card, "
            ":ws_min_id, :ws_min_description, :ws_min_unit, "
            ":ws_min, :ws_max_id, :ws_max_description, :ws_max_unit, "
            ":ws_max, :wave_min_id, :wave_min_description, :wave_min_unit, "
            ":wave_min, :wave_max_id, :wave_max_description, :wave_max_unit, "
            ":wave_max, :visibility_id, :visibility_description, "
            ":visibility_unit, :visibility, :tmin_id, :tmin_description, "
            ":tmin_unit, :tmin, :tmax_id, :tmax_description, :tmax_unit, "
            ":tmax, :humin_id, :humin_description, :humin_unit, :humin, "
            ":humax_id, :humax_description, :humax_unit, :humax, :pdf_id, "
            ":pdf_description, :pdf_unit, :pdf, :pasang_min_datemin, "
            ":pasang_min_datemax, :pasang_min_unit, :pasang_min_description, "
            ":pasang_min_zona, :pasang_min, :pasang_max_datemin, "
            ":pasang_max_datemax, :pasang_max_unit, :pasang_max_description, "
            ":pasang_max_zona, :pasang_max, :remarks)"
        )
    elif table == 'maritim_cuaca_penyebrangan':
        insert_command = (
            "INSERT INTO " + table +
            "(batch_time, domain, station_id, shortname, "
            "timestamp, phone_number, phone_id, email, "
            "address, area_id, area_name_id, area_name_en, "
            "area_description, area_domain, area_habor_from, "
            "area_habor_to, type, datetime, validfrom, "
            "validto, timezone, weather_id, weather_description, "
            "weather_icon_unit, weather_icon, wd_from_id, "
            "wd_from_description, wd_from_icon_id_unit, "
            "wd_from_icon_en_unit, wd_from_icon_card_unit, "
            "wd_from_icon_id, wd_from_icon_en, wd_from_icon_card, "
            "wd_to_id, wd_to_description, wd_to_icon_en_unit, "
            "wd_to_icon_id_unit, wd_to_icon_card_unit, "
            "wd_to_icon_en, wd_to_icon_id, wd_to_icon_card, "
            "ws_min_id, ws_min_description, ws_min_unit, "
            "ws_min, ws_max_id, ws_max_description, ws_max_unit, "
            "ws_max, wave_min_id, wave_min_description, wave_min_unit, "
            "wave_min, wave_max_id, wave_max_description, wave_max_unit, "
            "wave_max) "
            "VALUES (:batch_time, :domain, :station_id, :shortname, "
            ":timestamp, :phone_number, :phone_id, :email, "
            ":address, :area_id, :area_name_id, :area_name_en, "
            ":area_description, :area_domain, :area_habor_from, "
            ":area_habor_to, :type, :datetime, :validfrom, "
            ":validto, :timezone, :weather_id, :weather_description, "
            ":weather_icon_unit, :weather_icon, :wd_from_id, "
            ":wd_from_description, :wd_from_icon_id_unit, "
            ":wd_from_icon_en_unit, :wd_from_icon_card_unit, "
            ":wd_from_icon_id, :wd_from_icon_en , :wd_from_icon_card, "
            ":wd_to_id, :wd_to_description , :wd_to_icon_en_unit, "
            ":wd_to_icon_id_unit, :wd_to_icon_card_unit, "
            ":wd_to_icon_en, :wd_to_icon_id, :wd_to_icon_card, "
            ":ws_min_id, :ws_min_description, :ws_min_unit, "
            ":ws_min, :ws_max_id, :ws_max_description, :ws_max_unit, "
            ":ws_max, :wave_min_id, :wave_min_description, :wave_min_unit, "
            ":wave_min, :wave_max_id, :wave_max_description, :wave_max_unit, "
            ":wave_max)"
        )
    elif table == 'maritim_wisata_bahari':
        insert_command = (
            "INSERT INTO " + table +
            "(batch_time, domain, station_id, shortname, "
            "timestamp, phone_number, phone_id, email, "
            "address, beach_id, beach_name, beach_description, "
            "beach_domain, beach_longitude, beach_latitude, "
            "beach_coordinate, type, datetime, hour, "
            "wave_id, wave_description, wave_direction_unit, "
            "wave_deg_unit, wave_direction, wave_deg, wave_height_id, "
            "wave_height_description, wave_height_meter_unit, "
            "wave_height_feet_unit, wave_height_meter, wave_height_feet, "
            "weather_id, weather_description, weather_unit, weather, "
            "wd_id, wd_description, wd_deg_unit, wd_card_unit, "
            "wd_sexa_unit, wd_deg, wd_card, wd_sexa, ws_id, "
            "ws_description, ws_kt_unit, ws_mph_unit, ws_kt, ws_mph)"
            "VALUES (:batch_time, :domain, :station_id, :shortname, "
            ":timestamp, :phone_number, :phone_id, :email, "
            ":address, :beach_id, :beach_name, :beach_description, "
            ":beach_domain, :beach_longitude, :beach_latitude, "
            ":beach_coordinate, :type, :datetime, :hour, "
            ":wave_id, :wave_description, :wave_direction_unit, "
            ":wave_deg_unit, :wave_direction, :wave_deg, :wave_height_id, "
            ":wave_height_description, :wave_height_meter_unit, "
            ":wave_height_feet_unit, :wave_height_meter, :wave_height_feet, "
            ":weather_id, :weather_description, :weather_unit, :weather, "
            ":wd_id, :wd_description, :wd_deg_unit, :wd_card_unit, "
            ":wd_sexa_unit, :wd_deg, :wd_card, :wd_sexa, :ws_id, "
            ":ws_description, :ws_kt_unit, :ws_mph_unit, :ws_kt, :ws_mph)"
        )
    elif table == 'digital_forecast':
        insert_command = ( 
            "INSERT INTO " + table +
            "(batch_time, domain, timestamp, area_id, area_latitude, "
            "area_longitude, area_coordinate, area_type, area_level, "
            "area_name_id, area_name_en, area_description, area_domain, "
            "area_tags, bps_id, hu_id, hu_description, hu_type, "
            "hu_00_hour, hu_00_unit, hu_00, hu_06_hour, "
            "hu_06_unit, hu_06, hu_12_hour, hu_12_unit, "
            "hu_12, hu_18_hour, hu_18_unit, hu_18, "
            "hu_24_unit, hu_24_hour, hu_24, hu_30_unit, "
            "hu_30_hour, hu_30, hu_36_unit, hu_36_hour, "
            "hu_36, hu_42_unit, hu_42_hour, hu_42, "
            "hu_48_unit, hu_48_hour, hu_48, hu_54_unit, "
            "hu_54_hour, hu_54, hu_60_unit, hu_60_hour, "
            "hu_60, hu_66_hour, hu_66_unit, hu_66, "
            "hu_72_unit, hu_72_hour, hu_72, hu_78_unit, "
            "hu_78_hour, hu_78, humax_id, humax_description, "
            "humax_type, humax_unit, humax_1_day, humax_1, "
            "humax_2_day, humax_2, humax_3_day, humax_3, "
            "tmax_id, tmax_description, tmax_type, tmax_c_unit, "
            "tmax_f_unit, tmax_1_day, tmax_1_c, tmax_1_f, "
            "tmax_2_day, tmax_2_c, tmax_2_f, tmax_3_day, "
            "tmax_3_c, tmax_3_f, humin_id, humin_description, "
            "humin_type, humin_unit, humin_1_day, humin_1, "
            "humin_2_day, humin_2, humin_3_day, humin_3, "
            "tmin_id, tmin_description, tmin_type, tmin_c_unit, "
            "tmin_f_unit, tmin_1_day, tmin_1_c, tmin_1_f, "
            "tmin_2_day, tmin_2_c, tmin_2_f, tmin_3_day, "
            "tmin_3_c, tmin_3_f, t_id, t_description, "
            "t_type, t_00_hour, t_00_c_unit, t_00_f_unit, "
            "t_00_c, t_00_f, t_06_hour, t_06_c_unit, "
            "t_06_f_unit, t_06_c, t_06_f, t_12_hour, "
            "t_12_c_unit, t_12_f_unit, t_12_c, t_12_f, "
            "t_18_hour, t_18_c_unit, t_18_f_unit, t_18_c, "
            "t_18_f, t_24_hour, t_24_c_unit, t_24_f_unit, "
            "t_24_c, t_24_f, t_30_hour, t_30_c_unit, "
            "t_30_f_unit, t_30_c, t_30_f, t_36_hour, "
            "t_36_c_unit, t_36_f_unit, t_36_c, t_36_f, "
            "t_42_hour, t_42_c_unit, t_42_f_unit, t_42_c, "
            "t_42_f, t_48_hour, t_48_c_unit, t_48_f_unit, "
            "t_48_c, t_48_f, t_54_hour, t_54_c_unit, "
            "t_54_f_unit, t_54_c, t_54_f, t_60_hour, "
            "t_60_c_unit, t_60_f_unit, t_60_c, t_60_f, "
            "t_66_hour, t_66_c_unit, t_66_f_unit, t_66_c, "
            "t_66_f, t_72_hour, t_72_c_unit, t_72_f_unit, "
            "t_72_c, t_72_f, t_78_hour, t_78_c_unit, "
            "t_78_f_unit, t_78_c, t_78_f, weather_id, "
            "weather_description, weather_type, weather_00, weather_00_unit, "
            "weather_00_hour, weather_06, weather_06_unit, weather_06_hour, "
            "weather_12, weather_12_unit, weather_12_hour, weather_18, "
            "weather_18_unit, weather_18_hour, weather_24, weather_24_unit, "
            "weather_24_hour, weather_30, weather_30_unit, weather_30_hour, "
            "weather_36, weather_36_unit, weather_36_hour, weather_42, "
            "weather_42_unit, weather_42_hour, weather_48, weather_48_unit, "
            "weather_48_hour, weather_54, weather_54_unit, weather_54_hour, "
            "weather_60, weather_60_unit, weather_60_hour, weather_72, "
            "weather_72_unit, weather_72_hour, weather_78, weather_78_unit, "
            "weather_78_hour, wd_id, wd_description, wd_type, "
            "wd_00_deg_unit, wd_00_card_unit, wd_00_sexa_unit, wd_00_deg, "
            "wd_00_card, wd_00_sexa, wd_06_hour, wd_06_deg_unit, "
            "wd_06_card_unit, wd_06_sexa_unit, wd_06_deg, wd_06_card, "
            "wd_06_sexa, wd_12_hour, wd_12_deg_unit, wd_12_card_unit, "
            "wd_12_sexa_unit, wd_12_deg, wd_12_card, wd_12_sexa, "
            "wd_18_hour, wd_18_deg_unit, wd_18_card_unit, wd_18_sexa_unit, "
            "wd_18_deg, wd_18_card, wd_18_sexa, wd_24_hour, "
            "wd_24_deg_unit, wd_24_card_unit, wd_24_sexa_unit, wd_24_deg, "
            "wd_24_card, wd_24_sexa, wd_30_hour, wd_30_deg_unit, "
            "wd_30_card_unit, wd_30_sexa_unit, wd_30_deg, wd_30_card, "
            "wd_30_sexa, wd_36_hour, wd_36_deg_unit, wd_36_card_unit, "
            "wd_36_sexa_unit, wd_36_deg, wd_36_card, wd_36_sexa, "
            "wd_42_hour, wd_42_deg_unit, wd_42_card_unit, wd_42_sexa_unit, "
            "wd_42_deg, wd_42_card, wd_42_sexa, wd_48_hour, "
            "wd_48_deg_unit, wd_48_card_unit, wd_48_sexa_unit, wd_48_deg, "
            "wd_48_card, wd_48_sexa, wd_54_hour, wd_54_deg_unit, "
            "wd_54_card_unit, wd_54_sexa_unit, wd_54_deg, wd_54_card, "
            "wd_54_sexa, wd_60_hour, wd_60_deg_unit, wd_60_card_unit, "
            "wd_60_sexa_unit, wd_60_deg, wd_60_card, wd_60_sexa, "
            "wd_66_hour, wd_66_deg_unit, wd_66_card_unit, wd_66_sexa_unit, "
            "wd_66_deg, wd_66_card, wd_66_sexa, wd_72_hour, "
            "wd_72_deg_unit, wd_72_card_unit, wd_72_sexa_unit, wd_72_deg, "
            "wd_72_card, wd_72_sexa, wd_78_hour, wd_78_deg_unit, "
            "wd_78_card_unit, wd_78_sexa_unit, wd_78_deg, wd_78_card, "
            "wd_78_sexa, ws_id, ws_description, ws_type, "
            "ws_00_hour, ws_00_mph_unit, ws_00_kph_unit, ws_00_ms_unit, "
            "ws_00_kt_unit, ws_00_mph, ws_00_kph, ws_00_ms, "
            "ws_00_kt, ws_06_hour, ws_06_mph_unit, ws_06_kph_unit, "
            "ws_06_ms_unit, ws_06_kt_unit, ws_06_kt, ws_06_mph, "
            "ws_06_kph, ws_06_ms, ws_12_hour, ws_12_mph_unit, "
            "ws_12_kph_unit, ws_12_ms_unit, ws_12_kt_unit, ws_12_kt, "
            "ws_12_mph, ws_12_kph, ws_12_ms, ws_18_hour, "
            "ws_18_mph_unit, ws_18_kph_unit, ws_18_ms_unit, ws_18_kt_unit, "
            "ws_18_kt, ws_18_mph, ws_18_kph, ws_18_ms, "
            "ws_24_hour, ws_24_mph_unit, ws_24_kph_unit, ws_24_ms_unit, "
            "ws_24_kt_unit, ws_24_kt, ws_24_mph, ws_24_kph, "
            "ws_24_ms, ws_30_hour, ws_30_mph_unit, ws_30_kph_unit, "
            "ws_30_ms_unit, ws_30_kt_unit, ws_30_kt, ws_30_mph, "
            "ws_30_kph, ws_30_ms, ws_36_hour, ws_36_mph_unit, "
            "ws_36_kph_unit, ws_36_ms_unit, ws_36_kt_unit, ws_36_kt, "
            "ws_36_mph, ws_36_kph, ws_36_ms, ws_42_hour, "
            "ws_42_mph_unit, ws_42_kph_unit, ws_42_ms_unit, ws_42_kt_unit, "
            "ws_42_kt, ws_42_mph, ws_42_kph, ws_42_ms, "
            "ws_48_hour, ws_48_mph_unit, ws_48_kph_unit, ws_48_ms_unit, "
            "ws_48_kt_unit, ws_48_kt, ws_48_mph, ws_48_kph, "
            "ws_48_ms, ws_54_hour, ws_54_mph_unit, ws_54_kph_unit, "
            "ws_54_ms_unit, ws_54_kt_unit, ws_54_kt, ws_54_mph, "
            "ws_54_kph, ws_54_ms, ws_60_hour, ws_60_mph_unit, "
            "ws_60_kph_unit, ws_60_ms_unit, ws_60_kt_unit, ws_60_kt, "
            "ws_60_mph, ws_60_kph, ws_60_ms, ws_66_hour, "
            "ws_66_mph_unit, ws_66_kph_unit, ws_66_ms_unit, ws_66_kt_unit, "
            "ws_66_kt, ws_66_mph, ws_66_kph, ws_66_ms, "
            "ws_72_hour, ws_72_mph_unit, ws_72_kph_unit, ws_72_ms_unit, "
            "ws_72_kt_unit, ws_72_kt, ws_72_mph, ws_72_kph, "
            "ws_72_ms, ws_78_hour, ws_78_mph_unit, ws_78_kph_unit, "
            "ws_78_ms_unit, ws_78_kt_unit, ws_78_kt, ws_78_mph, "
            "heatindex_id, heatindex_description, heatindex_type, "
            "heatindex_00_hour, heatindex_00, heatindex_06_hour, "
            "heatindex_06, heatindex_12_hour, "
            "heatindex_12, heatindex_18_hour, heatindex_18, "
            "heatindex_24_hour, heatindex_24, "
            "heatindex_30_hour, heatindex_30, heatindex_36_hour, "
            "heatindex_36, heatindex_42_hour, heatindex_42, "
            "heatindex_48_hour, heatindex_48, "
            "heatindex_54_hour, heatindex_54, heatindex_60_hour, "
            "heatindex_60, heatindex_66_hour, heatindex_66, "
            "heatindex_72_hour, heatindex_72, heatindex_78_hour, heatindex_78)"
            "VALUES (:batch_time, :domain, :timestamp, :area_id, :area_latitude, "
            ":area_longitude, :area_coordinate, :area_type, :area_level, "
            ":area_name_id, :area_name_en, :area_description, :area_domain, "
            ":area_tags, :bps_id, :hu_id, :hu_description, :hu_type, "
            ":hu_00_hour, :hu_00_unit, :hu_00, :hu_06_hour, "
            ":hu_06_unit, :hu_06, :hu_12_hour, :hu_12_unit, "
            ":hu_12, :hu_18_hour, :hu_18_unit, :hu_18, "
            ":hu_24_unit, :hu_24_hour, :hu_24, :hu_30_unit, "
            ":hu_30_hour, :hu_30, :hu_36_unit, :hu_36_hour, "
            ":hu_36, :hu_42_unit, :hu_42_hour, :hu_42, "
            ":hu_48_unit, :hu_48_hour, :hu_48, :hu_54_unit, "
            ":hu_54_hour, :hu_54, :hu_60_unit, :hu_60_hour, "
            ":hu_60, :hu_66_hour, :hu_66_unit, :hu_66, "
            ":hu_72_unit, :hu_72_hour, :hu_72, :hu_78_unit, "
            ":hu_78_hour, :hu_78, :humax_id, :humax_description, "
            ":humax_type, :humax_unit, :humax_1_day, :humax_1, "
            ":humax_2_day, :humax_2, :humax_3_day, :humax_3, "
            ":tmax_id, :tmax_description, :tmax_type, :tmax_c_unit, "
            ":tmax_f_unit, :tmax_1_day, :tmax_1_c, :tmax_1_f, "
            ":tmax_2_day, :tmax_2_c, :tmax_2_f, :tmax_3_day, "
            ":tmax_3_c, :tmax_3_f, :humin_id, :humin_description, "
            ":humin_type, :humin_unit, :humin_1_day, :humin_1, "
            ":humin_2_day, :humin_2, :humin_3_day, :humin_3, "
            ":tmin_id, :tmin_description, :tmin_type, :tmin_c_unit, "
            ":tmin_f_unit, :tmin_1_day, :tmin_1_c, :tmin_1_f, "
            ":tmin_2_day, :tmin_2_c, :tmin_2_f, :tmin_3_day, "
            ":tmin_3_c, :tmin_3_f, :t_id, :t_description, "
            ":t_type, :t_00_hour, :t_00_c_unit, :t_00_f_unit, "
            ":t_00_c, :t_00_f, :t_06_hour, :t_06_c_unit, "
            ":t_06_f_unit, :t_06_c, :t_06_f, :t_12_hour, "
            ":t_12_c_unit, :t_12_f_unit, :t_12_c, :t_12_f, "
            ":t_18_hour, :t_18_c_unit, :t_18_f_unit, :t_18_c, "
            ":t_18_f, :t_24_hour, :t_24_c_unit, :t_24_f_unit, "
            ":t_24_c, :t_24_f, :t_30_hour, :t_30_c_unit, "
            ":t_30_f_unit, :t_30_c, :t_30_f, :t_36_hour, "
            ":t_36_c_unit, :t_36_f_unit, :t_36_c, :t_36_f, "
            ":t_42_hour, :t_42_c_unit, :t_42_f_unit, :t_42_c, "
            ":t_42_f, :t_48_hour, :t_48_c_unit, :t_48_f_unit, "
            ":t_48_c, :t_48_f, :t_54_hour, :t_54_c_unit, "
            ":t_54_f_unit, :t_54_c, :t_54_f, :t_60_hour, "
            ":t_60_c_unit, :t_60_f_unit, :t_60_c, :t_60_f, "
            ":t_66_hour, :t_66_c_unit, :t_66_f_unit, :t_66_c, "
            ":t_66_f, :t_72_hour, :t_72_c_unit, :t_72_f_unit, "
            ":t_72_c, :t_72_f, :t_78_hour, :t_78_c_unit, "
            ":t_78_f_unit, :t_78_c, :t_78_f, :weather_id, "
            ":weather_description, :weather_type, :weather_00, :weather_00_unit, "
            ":weather_00_hour, :weather_06, :weather_06_unit, :weather_06_hour, "
            ":weather_12, :weather_12_unit, :weather_12_hour, :weather_18, "
            ":weather_18_unit, :weather_18_hour, :weather_24, :weather_24_unit, "
            ":weather_24_hour, :weather_30, :weather_30_unit, :weather_30_hour, "
            ":weather_36, :weather_36_unit, :weather_36_hour, :weather_42, "
            ":weather_42_unit, :weather_42_hour, :weather_48, :weather_48_unit, "
            ":weather_48_hour, :weather_54, :weather_54_unit, :weather_54_hour, "
            ":weather_60, :weather_60_unit, :weather_60_hour, :weather_72, "
            ":weather_72_unit, :weather_72_hour, :weather_78, :weather_78_unit, "
            ":weather_78_hour, :wd_id, :wd_description, :wd_type, "
            ":wd_00_deg_unit, :wd_00_card_unit, :wd_00_sexa_unit, :wd_00_deg, "
            ":wd_00_card, :wd_00_sexa, :wd_06_hour, :wd_06_deg_unit, "
            ":wd_06_card_unit, :wd_06_sexa_unit, :wd_06_deg, :wd_06_card, "
            ":wd_06_sexa, :wd_12_hour, :wd_12_deg_unit, :wd_12_card_unit, "
            ":wd_12_sexa_unit, :wd_12_deg, :wd_12_card, :wd_12_sexa, "
            ":wd_18_hour, :wd_18_deg_unit, :wd_18_card_unit, :wd_18_sexa_unit, "
            ":wd_18_deg, :wd_18_card, :wd_18_sexa, :wd_24_hour, "
            ":wd_24_deg_unit, :wd_24_card_unit, :wd_24_sexa_unit, :wd_24_deg, "
            ":wd_24_card, :wd_24_sexa, :wd_30_hour, :wd_30_deg_unit, "
            ":wd_30_card_unit, :wd_30_sexa_unit, :wd_30_deg, :wd_30_card, "
            ":wd_30_sexa, :wd_36_hour, :wd_36_deg_unit, :wd_36_card_unit, "
            ":wd_36_sexa_unit, :wd_36_deg, :wd_36_card, :wd_36_sexa, "
            ":wd_42_hour, :wd_42_deg_unit, :wd_42_card_unit, :wd_42_sexa_unit, "
            ":wd_42_deg, :wd_42_card, :wd_42_sexa, :wd_48_hour, "
            ":wd_48_deg_unit, :wd_48_card_unit, :wd_48_sexa_unit, :wd_48_deg, "
            ":wd_48_card, :wd_48_sexa, :wd_54_hour, :wd_54_deg_unit, "
            ":wd_54_card_unit, :wd_54_sexa_unit, :wd_54_deg, :wd_54_card, "
            ":wd_54_sexa, :wd_60_hour, :wd_60_deg_unit, :wd_60_card_unit, "
            ":wd_60_sexa_unit, :wd_60_deg, :wd_60_card, :wd_60_sexa, "
            ":wd_66_hour, :wd_66_deg_unit, :wd_66_card_unit, :wd_66_sexa_unit, "
            ":wd_66_deg, :wd_66_card, :wd_66_sexa, :wd_72_hour, "
            ":wd_72_deg_unit, :wd_72_card_unit, :wd_72_sexa_unit, :wd_72_deg, "
            ":wd_72_card, :wd_72_sexa, :wd_78_hour, :wd_78_deg_unit, "
            ":wd_78_card_unit, :wd_78_sexa_unit, :wd_78_deg, :wd_78_card, "
            ":wd_78_sexa, :ws_id, :ws_description, :ws_type, "
            ":ws_00_hour, :ws_00_mph_unit, :ws_00_kph_unit, :ws_00_ms_unit, "
            ":ws_00_kt_unit, :ws_00_mph, :ws_00_kph, :ws_00_ms, "
            ":ws_00_kt, :ws_06_hour, :ws_06_mph_unit, :ws_06_kph_unit, "
            ":ws_06_ms_unit, :ws_06_kt_unit, :ws_06_kt, :ws_06_mph, "
            ":ws_06_kph, :ws_06_ms, :ws_12_hour, :ws_12_mph_unit, "
            ":ws_12_kph_unit, :ws_12_ms_unit, :ws_12_kt_unit, :ws_12_kt, "
            ":ws_12_mph, :ws_12_kph, :ws_12_ms, :ws_18_hour, "
            ":ws_18_mph_unit, :ws_18_kph_unit, :ws_18_ms_unit, :ws_18_kt_unit, "
            ":ws_18_kt, :ws_18_mph, :ws_18_kph, :ws_18_ms, "
            ":ws_24_hour, :ws_24_mph_unit, :ws_24_kph_unit, :ws_24_ms_unit, "
            ":ws_24_kt_unit, :ws_24_kt, :ws_24_mph, :ws_24_kph, "
            ":ws_24_ms, :ws_30_hour, :ws_30_mph_unit, :ws_30_kph_unit, "
            ":ws_30_ms_unit, :ws_30_kt_unit, :ws_30_kt, :ws_30_mph, "
            ":ws_30_kph, :ws_30_ms, :ws_36_hour, :ws_36_mph_unit, "
            ":ws_36_kph_unit, :ws_36_ms_unit, :ws_36_kt_unit, :ws_36_kt, "
            ":ws_36_mph, :ws_36_kph, :ws_36_ms, :ws_42_hour, "
            ":ws_42_mph_unit, :ws_42_kph_unit, :ws_42_ms_unit, :ws_42_kt_unit, "
            ":ws_42_kt, :ws_42_mph, :ws_42_kph, :ws_42_ms, "
            ":ws_48_hour, :ws_48_mph_unit, :ws_48_kph_unit, :ws_48_ms_unit, "
            ":ws_48_kt_unit, :ws_48_kt, :ws_48_mph, :ws_48_kph, "
            ":ws_48_ms, :ws_54_hour, :ws_54_mph_unit, :ws_54_kph_unit, "
            ":ws_54_ms_unit, :ws_54_kt_unit, :ws_54_kt, :ws_54_mph, "
            ":ws_54_kph, :ws_54_ms, :ws_60_hour, :ws_60_mph_unit, "
            ":ws_60_kph_unit, :ws_60_ms_unit, :ws_60_kt_unit, :ws_60_kt, "
            ":ws_60_mph, :ws_60_kph, :ws_60_ms, :ws_66_hour, "
            ":ws_66_mph_unit, :ws_66_kph_unit, :ws_66_ms_unit, :ws_66_kt_unit, "
            ":ws_66_kt, :ws_66_mph, :ws_66_kph, :ws_66_ms, "
            ":ws_72_hour, :ws_72_mph_unit, :ws_72_kph_unit, :ws_72_ms_unit, "
            ":ws_72_kt_unit, :ws_72_kt, :ws_72_mph, :ws_72_kph, "
            ":ws_72_ms, :ws_78_hour, :ws_78_mph_unit, :ws_78_kph_unit, "
            ":ws_78_ms_unit, :ws_78_kt_unit, :ws_78_kt, :ws_78_mph, "
            ":heatindex_id, :heatindex_description, :heatindex_type, "
            ":heatindex_00_hour, :heatindex_00, :heatindex_06_hour, "
            ":heatindex_06, :heatindex_12_hour, "
            ":heatindex_12, :heatindex_18_hour, :heatindex_18, "
            ":heatindex_24_hour, :heatindex_24, "
            ":heatindex_30_hour, :heatindex_30, :heatindex_36_hour, "
            ":heatindex_36, :heatindex_42_hour, :heatindex_42, "
            ":heatindex_48_hour, :heatindex_48, "
            ":heatindex_54_hour, :heatindex_54, :heatindex_60_hour, "
            ":heatindex_60, :heatindex_66_hour, :heatindex_66, "
            ":heatindex_72_hour, :heatindex_72, :heatindex_78_hour, :heatindex_78)"
        )
    elif table == 'iklim_kabupaten_csv':
        insert_command = (
            "INSERT INTO " + table +
            "(batch_time, provinsi, id_kabupaten_kota, kabupaten_kota, month, year, "
            "ach_1_sbk, ach_1_sb, ach_1_sbb, ach_1_m, "
            "ash_1_sbk, ash_1_sb, ash_1_sbb, ash_1_m, "
            "pch_1_sbk, pch_1_sb, pch_1_sbb, pch_1_m, "
            "psh_1_sbk, psh_1_sb, psh_1_sbb, psh_1_m, "
            "pch_2_sbk, pch_2_sb, pch_2_sbb, pch_2_m, "
            "psh_2_sbk, psh_2_sb, psh_2_sbb, psh_2_m, "
            "pch_3_sbk, pch_3_sb, pch_3_sbb, pch_3_m, "
            "psh_3_sbk, psh_3_sb, psh_3_sbb, psh_3_m) "
            "VALUES (:batch_time, :provinsi, :id_kabupaten_kota, :kabupaten_kota, :month, :year, "
            ":ach_1_sbk, :ach_1_sb, :ach_1_sbb, :ach_1_m, "
            ":ash_1_sbk, :ash_1_sb, :ash_1_sbb, :ash_1_m, "
            ":pch_1_sbk, :pch_1_sb, :pch_1_sbb, :pch_1_m, "
            ":psh_1_sbk, :psh_1_sb, :psh_1_sbb, :psh_1_m, "
            ":pch_2_sbk, :pch_2_sb, :pch_2_sbb, :pch_2_m, "
            ":psh_2_sbk, :psh_2_sb, :psh_2_sbb, :psh_2_m, "
            ":pch_3_sbk, :pch_3_sb, :pch_3_sbb, :pch_3_m, "
            ":psh_3_sbk, :psh_3_sb, :psh_3_sbb, :psh_3_m) "
        )
    elif table == 'iklim_kecamatan_csv':
        insert_command = (
            "INSERT INTO " + table +
            "(batch_time, provinsi, id_kabupaten_kota, kabupaten_kota, id_kecamatan, kecamatan, month, year, "
            "ach_1_sbk, ach_1_sb, ach_1_sbb, ach_1_m, "
            "ash_1_sbk, ash_1_sb, ash_1_sbb, ash_1_m, "
            "pch_1_sbk, pch_1_sb, pch_1_sbb, pch_1_m, "
            "psh_1_sbk, psh_1_sb, psh_1_sbb, psh_1_m, "
            "pch_2_sbk, pch_2_sb, pch_2_sbb, pch_2_m, "
            "psh_2_sbk, psh_2_sb, psh_2_sbb, psh_2_m, "
            "pch_3_sbk, pch_3_sb, pch_3_sbb, pch_3_m, "
            "psh_3_sbk, psh_3_sb, psh_3_sbb, psh_3_m) "
            "VALUES (:batch_time, :provinsi, :id_kabupaten_kota, :kabupaten_kota, :id_kecamatan, :kecamatan, :month, :year, "
            ":ach_1_sbk, :ach_1_sb, :ach_1_sbb, :ach_1_m, "
            ":ash_1_sbk, :ash_1_sb, :ash_1_sbb, :ash_1_m, "
            ":pch_1_sbk, :pch_1_sb, :pch_1_sbb, :pch_1_m, "
            ":psh_1_sbk, :psh_1_sb, :psh_1_sbb, :psh_1_m, "
            ":pch_2_sbk, :pch_2_sb, :pch_2_sbb, :pch_2_m, "
            ":psh_2_sbk, :psh_2_sb, :psh_2_sbb, :psh_2_m, "
            ":pch_3_sbk, :pch_3_sb, :pch_3_sbb, :pch_3_m, "
            ":psh_3_sbk, :psh_3_sb, :psh_3_sbb, :psh_3_m) "
        )
    elif table == 'iklim_desa_csv':
        insert_command = (
            "INSERT INTO " + table +
            "(batch_time, provinsi, id_kabupaten_kota, kabupaten_kota, id_kecamatan, kecamatan, id_desa, desa, month, year, "
            "ach_1_sbk, ach_1_sb, ach_1_sbb, ach_1_m, "
            "ash_1_sbk, ash_1_sb, ash_1_sbb, ash_1_m, "
            "pch_1_sbk, pch_1_sb, pch_1_sbb, pch_1_m, "
            "psh_1_sbk, psh_1_sb, psh_1_sbb, psh_1_m, "
            "pch_2_sbk, pch_2_sb, pch_2_sbb, pch_2_m, "
            "psh_2_sbk, psh_2_sb, psh_2_sbb, psh_2_m, "
            "pch_3_sbk, pch_3_sb, pch_3_sbb, pch_3_m, "
            "psh_3_sbk, psh_3_sb, psh_3_sbb, psh_3_m) "
            "VALUES (:batch_time, :provinsi, :id_kabupaten_kota, :kabupaten_kota, :id_kecamatan, :kecamatan, :id_desa, :desa, :month, :year, "
            ":ach_1_sbk, :ach_1_sb, :ach_1_sbb, :ach_1_m, "
            ":ash_1_sbk, :ash_1_sb, :ash_1_sbb, :ash_1_m, "
            ":pch_1_sbk, :pch_1_sb, :pch_1_sbb, :pch_1_m, "
            ":psh_1_sbk, :psh_1_sb, :psh_1_sbb, :psh_1_m, "
            ":pch_2_sbk, :pch_2_sb, :pch_2_sbb, :pch_2_m, "
            ":psh_2_sbk, :psh_2_sb, :psh_2_sbb, :psh_2_m, "
            ":pch_3_sbk, :pch_3_sb, :pch_3_sbb, :pch_3_m, "
            ":psh_3_sbk, :psh_3_sb, :psh_3_sbb, :psh_3_m) "
        )
    else:
        insert_command = None
    return insert_command
