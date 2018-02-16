#!/usr/bin/env bash

source ~/.virtualenvs/bmkgmqtt/bin/activate
cd $(dirname $0)
supervisord -n -c supervisord.conf
