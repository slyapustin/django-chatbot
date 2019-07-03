release: python manage.py migrate --noinput
web: gunicorn project.wsgi
worker: celery worker --app=app.tasks.app
