#!/bin/sh


python manage.py migrate --run-syncdb
#python manage.py collectstatic --no-input

gunicorn GLOCS.wsgi:application --bind 0.0.0.0:8080 --reload  -w 4
