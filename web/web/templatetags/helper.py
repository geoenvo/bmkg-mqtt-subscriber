"""
Function for BMKG MQTT Django UI.
"""
import os

from datetime import datetime
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    """
        Strip html class
    """
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    """
        Strip html function
    """
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def weather_image(icon_number, forecast_time):
    """
    Function for determine weather icon filename
    """
    if forecast_time == "am":
        if icon_number == "5":
            icon_filename = "udara kabur-am.png"
        elif icon_number == "45":
            icon_filename = "kabut-am.png"
        elif icon_number == "60":
            icon_filename = "hujan ringan-am.png"
        elif icon_number == "61":
            icon_filename = "hujan sedang-am.png"
        elif icon_number == "63":
            icon_filename = "hujan lebat-am.png"
        elif icon_number == "80":
            icon_filename = "hujan sedang-am.png"
        elif icon_number == "95":
            icon_filename = "hujan lokal-am.png"
        elif icon_number == "97":
            icon_filename = "hujan petir-am.png"
        elif icon_number == "100":
            icon_filename = "cerah-am.png"
        elif icon_number == "101":
            icon_filename = "cerah berawan-am.png"
        elif icon_number == "102":
            icon_filename = "cerah berawan-am.png"
        elif icon_number == "103":
            icon_filename = "berawan-am.png"
        elif icon_number == "104":
            icon_filename = "berawan tebal-am.png"
        else:
            icon_filename = None
    else:
        if icon_number == "5":
            icon_filename = "udara kabur-pm.png"
        elif icon_number == "45":
            icon_filename = "kabut-pm.png"
        elif icon_number == "60":
            icon_filename = "hujan ringan-pm.png"
        elif icon_number == "61":
            icon_filename = "hujan sedang-pm.png"
        elif icon_number == "63":
            icon_filename = "hujan lebat-pm.png"
        elif icon_number == "80":
            icon_filename = "hujan sedang-pm.png"
        elif icon_number == "95":
            icon_filename = "hujan lokal-pm.png"
        elif icon_number == "97":
            icon_filename = "hujan petir-pm.png"
        elif icon_number == "100":
            icon_filename = "cerah-pm.png"
        elif icon_number == "101":
            icon_filename = "cerah berawan-pm.png"
        elif icon_number == "102":
            icon_filename = "cerah berawan-pm.png"
        elif icon_number == "103":
            icon_filename = "berawan-pm.png"
        elif icon_number == "104":
            icon_filename = "berawan tebal-pm.png"
        else:
            icon_filename = None
    return icon_filename


def get_timestamp(timestamp):
    """
    Return timestamp in Bahasa from datetime format
    """
    year = timestamp.year
    month = timestamp.month
    day = timestamp.day
    day_name = datetime.strftime(timestamp, "%A")
    if month == 1:
        monthname = 'Januari'
    elif month == 2:
        monthname = 'Februari'
    elif month == 3:
        monthname = 'Maret'
    elif month == 4:
        monthname = 'April'
    elif month == 5:
        monthname = 'Mei'
    elif month == 6:
        monthname = 'Juni'
    elif month == 7:
        monthname = 'Juli'
    elif month == 8:
        monthname = 'Agustus'
    elif month == 9:
        monthname = 'September'
    elif month == 10:
        monthname = 'Oktober'
    elif month == 11:
        monthname = 'November'
    else:
        monthname = 'Desember'
    if day_name == 'Monday':
        day_name = 'Senin'
    elif day_name == 'Tuesday':
        day_name = 'Selasa'
    elif day_name == 'Wednesday':
        day_name = 'Rabu'
    elif day_name == 'Thursday':
        day_name = 'Kamis'
    elif day_name == 'Friday':
        day_name = 'Jumat'
    elif day_name == 'Saturday':
        day_name = 'Sabtu'
    else:
        day_name = 'Minggu'
    return "%s, %s %s %s" % (day_name, str(day), monthname, str(year))


def get_timestampfull(timestamp):
    """
    Return timestamp full until time in Bahasa from datetime format
    """
    year = timestamp.year
    month = timestamp.month
    day = timestamp.day
    hour = timestamp.hour
    if hour < 10:
        hour = "0%s" % str(hour)
    minute = timestamp.minute
    if minute < 10:
        minute = "0%s" % str(minute)
    second = timestamp.second
    if second < 10:
        second = "0%s" % str(second)
    microsecond = timestamp.microsecond
    day_name = datetime.strftime(timestamp, "%A")
    if month == 1:
        monthname = 'Januari'
    elif month == 2:
        monthname = 'Februari'
    elif month == 3:
        monthname = 'Maret'
    elif month == 4:
        monthname = 'April'
    elif month == 5:
        monthname = 'Mei'
    elif month == 6:
        monthname = 'Juni'
    elif month == 7:
        monthname = 'Juli'
    elif month == 8:
        monthname = 'Agustus'
    elif month == 9:
        monthname = 'September'
    elif month == 10:
        monthname = 'Oktober'
    elif month == 11:
        monthname = 'November'
    else:
        monthname = 'Desember'
    if day_name == 'Monday':
        day_name = 'Senin'
    elif day_name == 'Tuesday':
        day_name = 'Selasa'
    elif day_name == 'Wednesday':
        day_name = 'Rabu'
    elif day_name == 'Thursday':
        day_name = 'Kamis'
    elif day_name == 'Friday':
        day_name = 'Jumat'
    elif day_name == 'Saturday':
        day_name = 'Sabtu'
    else:
        day_name = 'Minggu'
    return "%s, %s %s %s %s:%s:%s.%s" % (day_name, str(day), monthname, str(year), str(hour), str(minute), str(second), str(microsecond))


def wind_direction(card):
    """
        Return Wind Girection in Bahasa from CARD
    """
    if card == "N":
        direction = "Utara"
    elif card == "NNE":
        direction = "Utara Timur Laut"
    elif card == "NE":
        direction = "Timur Laut"
    elif card == "ENE":
        direction = "Timur Timur Laut"
    elif card == "E":
        direction = "Timur"
    elif card == "ESE":
        direction = "Timur Menenggara"
    elif card == "SE":
        direction = "Tenggara"
    elif card == "SSE":
        direction = "Selatan Menenggara"
    elif card == "S":
        direction = "Selatan"
    elif card == "SSW":
        direction = "Selatan Barat Daya"
    elif card == "SW":
        direction = "Barat Daya"
    elif card == "WSW":
        direction = "Barat Barat Daya"
    elif card == "W":
        direction = "Barat"
    elif card == "WNW":
        direction = "Barat Barat Laut"
    elif card == "NW":
        direction = "Barat Laut"
    elif card == "NNW":
        direction = "Utara Barat Laut"
    else:
        direction = "Variable"
    return direction


def get_category(cat_dict):
    """
        Get category note based on key
    """
    for key, value in zip(cat_dict.keys(), cat_dict.values()):
        if key == "0 - 20" or key == "20 - 50" or key == "50 - 100":
            cat_dict[key] = [value, "Rendah"]
        elif key == "100 - 150" or key == "150 - 200" or key == "200 - 300":
            cat_dict[key] = [value, "Menengah"]
        elif key == "300 - 400":
            cat_dict[key] = [value, "Tinggi"]
        else:
            cat_dict[key] = [value, "Sangat Tinggi"]
    return cat_dict


def get_month_year(month_index, year):
    """
        Function to get month name in bahasa based on month number and year
    """
    if month_index == 13:
        month_index = 1
        year = year + 1
    elif month_index == 14:
        month_index = 2
        year = year + 1
    elif month_index == 15:
        month_index = 3
        year = year + 1
    elif month_index == 0:
        month_index = 12
        year = year - 1
    if month_index == 1:
        monthname = 'Januari'
    elif month_index == 2:
        monthname = 'Februari'
    elif month_index == 3:
        monthname = 'Maret'
    elif month_index == 4:
        monthname = 'April'
    elif month_index == 5:
        monthname = 'Mei'
    elif month_index == 6:
        monthname = 'Juni'
    elif month_index == 7:
        monthname = 'Juli'
    elif month_index == 8:
        monthname = 'Agustus'
    elif month_index == 9:
        monthname = 'September'
    elif month_index == 10:
        monthname = 'Oktober'
    elif month_index == 11:
        monthname = 'November'
    else:
        monthname = 'Desember'
    return monthname, year
