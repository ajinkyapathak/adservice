#!/bin/sh
sleep 1s

echo "############# Running adservice using unicorn ################"
gunicorn -c gunicorn.py service_app:app
