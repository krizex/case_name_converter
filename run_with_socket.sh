#!/bin/env bash

source venv/flask/bin/activate
cd src

exec uwsgi wsgi_socket_config.ini
