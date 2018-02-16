#!/usr/bin/env bash

source ~/.virtualenvs/bmkgmqtt/bin/activate
cd $(dirname $0)
python sqlite_clear_databases.py
