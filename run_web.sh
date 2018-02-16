#!/usr/bin/env bash

source ~/.virtualenvs/bmkgmqtt/bin/activate
cd $(dirname $0)/web
python manage.py runserver 0.0.0.0:8000
