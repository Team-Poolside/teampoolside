#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "waiting for postgres..."
    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done
    echo "postgresql started"
fi

# conda run -p /home/app/web/env python manage.py makemigrations --noinput
conda run -p /home/app/web/env python manage.py migrate --noinput
conda run -p /home/app/web/env python manage.py collectstatic -c --noinput

exec "$@"