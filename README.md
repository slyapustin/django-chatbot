# Django Chatbot hosted on Heroku

Django Chatbot application with the background tasks processing and communications via WebSockets.

## Deployment
You can host it on [Heroku](https://www.heroku.com) for free ([account verification required](https://devcenter.heroku.com/articles/account-verification)).

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Technology Stack
 - [Django](https://www.djangoproject.com/) as a mani Web Framwerok
 - [Django Channels](https://github.com/django/channels) as WebSockets framework     
 - [Celery](http://www.celeryproject.org/) as a Asynchronous task queue
 - [Redis](https://redis.io/) as a Message Broker and Cache Backend   
 - [Daphne](https://github.com/django/daphne) as a HTTP and WebSocket protocol server
 - [Heroku](https://www.heroku.com) as a Hosting Platform


## Supported commands
 - `sum <x> <y>` - Calculate sum of two integers
 - `status <url>` - Check website status
