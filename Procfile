release: python manage.py migrate --noinput
web: daphne project.asgi:application --port $PORT --bind 0.0.0.0
worker: REMAP_SIGTERM=SIGQUIT celery -A project worker --loglevel info
