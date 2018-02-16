"""
BMKG MQTT subscriber
"""

import time
import datetime
import paho.mqtt.client as mqtt
import sqlite3
import json
import os

from settings import (
    TOPIC,
    SQLITE_DB,
    BROKER_ADDRESS,
    BROKER_KEEPALIVE,
    CLIENT_ID_SUB,
    MOSQUITTO_USER,
    MOSQUITTO_PASSWORD,
    CLEAR_MESSAGE_RETAIN
)
from function import sqlite_insert_command


def on_connect(client, userdata, flags, rc):
    """ Callback function when connecting to broker
    """
    print "CONNACK received with code %d." % (rc)
    client.subscribe(topics_list, qos=1)

def on_disconnect(client, userdata, rc):
    """ Callback function when disconnecting to broker
    """
    if rc != 0:
        print "Unexpected disconnection with code %d." % (rc)

def on_subscribe(client, userdata, mid, granted_qos):
    """ Callback function when subscribing to a topic
    """
    print "Subscribed %s %s." % (str(mid), str(granted_qos))

def on_message(client, userdata, message):
    """ Callback function when receiving topic message
    """
    # print("message received=%s" % str(message.payload.decode("utf-8")))
    if str(message.retain) == '0':
        print "=" * 60
        print 'START : %s' % str(datetime.datetime.now())
        print "message topic=%s" % str(message.topic)
        print "message qos=%s" % str(message.qos)
        print "message retain flag=%s" % str(message.retain)
        # Integrate topic with sqlite table
        if str(message.topic) == 'gempa/dirasakan':
            table = 'gempa_dirasakan'
        elif str(message.topic) == 'gempa/terkini':
            table = 'gempa_terkini'
        elif str(message.topic) == 'gempa/terkinicsv':
            table = 'gempa_terkini_csv'
        elif str(message.topic) == 'cuaca/citrasatelit/himawari/irenhanced':
            table = 'satelit_himawari_8_ir_enhanced'
        elif str(message.topic) == 'cuaca/citrasatelit/himawari/naturalcolor':
            table = 'satelit_himawari_8_natural_color'
        elif str(message.topic) == 'cuaca/citrasatelit/hotspotmodis':
            table = 'satelit_hotspot_modis'
        elif 'cuaca/maritim/wisata_bahari' in str(message.topic):
            table = 'maritim_wisata_bahari'
        elif 'cuaca/maritim/penyebrangan' in str(message.topic):
            table = 'maritim_cuaca_penyebrangan'
        elif 'cuaca/maritim/pelabuhan' in str(message.topic):
            table = 'maritim_cuaca_pelabuhan'
        elif 'cuaca/maritim/pelayanan' in str(message.topic):
            table = 'maritim_cuaca_pelayanan'
        elif 'cuaca/digitalforecast' in str(message.topic):
            table = 'digital_forecast'
        elif 'iklim/kabupaten' in str(message.topic):
            table = 'iklim_kabupaten_csv'
        elif 'iklim/kecamatan' in str(message.topic):
            table = 'iklim_kecamatan_csv'
        elif 'iklim/desa' in str(message.topic):
            table = 'iklim_desa_csv'
        else:
            table = None
        # Save to sqlite
        print "Received Message Size = %s bytes " % str(len(message.payload.encode('utf-8')))
        save_to_sqlite(table, message.payload, message.topic)
    else:
        if CLEAR_MESSAGE_RETAIN:
            print "Sending empty payload for topic: %s" %  str(message.topic)
            client.publish(message.topic, None, qos=1, retain=True)

def save_to_sqlite(table, messages, topic):
    """
    Save message to bmkg_msqtt sqlite databases
    """
    print "Sqlite DB location: %s" % SQLITE_DB
    print "Save to Table : %s" % table
    print "Save for Topic : %s" % topic
    try:
        connection = sqlite3.connect(SQLITE_DB)
        cursor = connection.cursor()
        insert_command = sqlite_insert_command(table)
        if insert_command:
            records = json.loads(messages)
            for record in records:
                insert_value = record
                print "Insert for batchtime record: %s" % record['batch_time']
                cursor.execute(insert_command, insert_value)
                connection.commit()
            cursor.close()
            connection.close()
            print 'FINISH : %s ' % str(datetime.datetime.now())
            print "=" * 60
    except Exception as e:
        print e


if __name__ == '__main__':
    # Topic listing
    topics_list = []
    for value in TOPIC.values():
        if isinstance(value, list):
            for v in value:
                topics_list.append((v, 1))
        else:
            topics_list.append((value, 1))

    print "creating new instance"
    # Create new instance
    client = mqtt.Client(CLIENT_ID_SUB, protocol=mqtt.MQTTv31, clean_session=False)
    if MOSQUITTO_USER and MOSQUITTO_PASSWORD:
        client.username_pw_set(MOSQUITTO_USER, MOSQUITTO_PASSWORD)

    # Attach function to callback
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe
    client.on_message = on_message

    print "client id sub : %s" % CLIENT_ID_SUB
    print "connecting to broker : %s" % str(BROKER_ADDRESS)
    print "Topic List: "
    for topic in topics_list:
        print "- %s" % str(topic[0])
    # Connect to broker
    client.connect(BROKER_ADDRESS, keepalive=BROKER_KEEPALIVE)

    ##client.loop_start() # start the loop
    #print("Subscribing to topics %s" % topics_list)
    ##client.subscribe(topics_list) # do this on connect callback
    ##time.sleep(10) # wait
    ##client.disconnect()
    ##client.loop_stop() # stop the loop
    client.loop_forever()
