release: python manage.py migrate --noinput
web: daphne project.asgi:application
worker: REMAP_SIGTERM=SIGQUIT celery worker --app project.celery.app --loglevel info
