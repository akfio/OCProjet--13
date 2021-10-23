web: gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT --log-file - --log-level debug
python manage.py collectstatic --noinput
python manage.py migrate

