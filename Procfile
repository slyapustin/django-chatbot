release: python manage.py migrate --noinput
web: gunicorn project.wsgi
worker: REMAP_SIGTERM=SIGQUIT celery worker --app project.celery.app --loglevel info
