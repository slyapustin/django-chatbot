release: python manage.py migrate --noinput
web: gunicorn project.wsgi
worker: celery worker --app project.celery.app --loglevel info
