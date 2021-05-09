#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "waiting for postgres..."
    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done
    echo "postgresql started"
fi

conda run -n env python manage.py makemigrations
conda run -n env python manage.py migrate

exec "$@"