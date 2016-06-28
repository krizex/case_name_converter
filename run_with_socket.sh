#!/bin/env bash

source venv/falsk/bin/activate

cd src

exec uwsgi wsgi_socket_config.ini