#!/usr/bin/env bash

source ~/.virtualenvs/bmkgmqtt/bin/activate
cd $(dirname $0)
python bmkg_mqtt_subscriber.py
