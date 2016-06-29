#!/bin/env bash

source venv/flask/bin/activate
echo ${PATH}
echo `which python`
cd src

exec uwsgi wsgi_socket_config.ini
