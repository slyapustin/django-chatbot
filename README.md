# Django Chatbot hosted on Heroku

Django Chatbot with the background tasks processing and communications via WebSockets.

For more details please check my article - [Heroku Chatbot with Celery, WebSockets, and Redis](https://itnext.io/heroku-chatbot-with-celery-websockets-and-redis-340fcd160f06).

## Deployment
You can host it on [Heroku](https://www.heroku.com) for free ([account verification required](https://devcenter.heroku.com/articles/account-verification)).

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Technology Stack
 - [Django](https://www.djangoproject.com/) as a main Web Framework
 - [Django Channels](https://github.com/django/channels) as WebSockets framework     
 - [Celery](http://www.celeryproject.org/) as a Asynchronous task queue
 - [Redis](https://redis.io/) as a Message Broker and Cache Backend   
 - [Daphne](https://github.com/django/daphne) as a HTTP and WebSocket protocol server
 - [Heroku](https://www.heroku.com) as a Hosting Platform


## Supported commands
 - `sum <x> <y>` - Calculate sum of two integers
 - `status <url>` - Check website status

## Need some help?
Here the Slack channel [#django-chatbot](https://join.slack.com/t/lyapustin/shared_invite/enQtNzc0MDQ0NjMxMzY2LTNmOTQ0NWM3YTQxYjM2ZGM3NTZiZWE1Y2E4ZGYyNDc2ODc3NzQ3ZWNlNDk3MGEyMWU0MDFiM2ZlYjYzY2I2Zjk)
