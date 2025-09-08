#!/bin/bash

while ! nc -z db 5432; do
  sleep 2
  echo "Waiting postgress...."
done

while ! nc -z redis 6379; do
  sleep 2
  echo "Waiting redis...."
done

python3 manage.py collectstatic --noinput
python3 manage.py migrate --noinput

gunicorn config.wsgi:application -b 0.0.0.0:8000 --workers 6



exit $?


