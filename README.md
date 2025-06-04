# Django Chatbot

The Django Chatbot is a chatbot application that utilizes background task processing and communication via WebSockets.

For more detailed information, please refer to my article titled [Heroku Chatbot with Celery, WebSockets, and Redis](https://itnext.io/heroku-chatbot-with-celery-websockets-and-redis-340fcd160f06).

## Deployment
### Docker

To deploy the application using Docker, follow these steps:
1. Clone the repository: `git clone https://github.com/slyapustin/django-chatbot`
2. Build and run the project: `docker-compose up`
3. Visit `http://localhost:8000/` in your web browser.

### Heroku
Alternatively, you can host the chatbot on [Heroku](https://www.heroku.com). Please note that an [account verification](https://devcenter.heroku.com/articles/account-verification) is required.

Click the button below to deploy the chatbot on Heroku:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Technology Stack
The chatbot utilizes the following technologies:

- [Django](https://www.djangoproject.com/): The main web framework.
- [Django Channels](https://github.com/django/channels): The WebSocket framework.
- [Celery](http://www.celeryproject.org/): An asynchronous task queue.
- [Redis](https://redis.io/): A message broker and cache backend.
- [Daphne](https://github.com/django/daphne): An HTTP and WebSocket protocol server.
- [Heroku](https://www.heroku.com): The hosting platform.

## Supported commands
The chatbot supports the following commands:

- `sum <x> <y>`: Calculates the sum of two integers.
- `status <url>`: Checks the status of a website.

## Need some help?
Join the Slack channel [#django-chatbot](https://join.slack.com/t/lyapustin/shared_invite/enQtNzc0MDQ0NjMxMzY2LTNmOTQ0NWM3YTQxYjM2ZGM3NTZiZWE1Y2E4ZGYyNDc2ODc3NzQ3ZWNlNDk3MGEyMWU0MDFiM2ZlYjYzY2I2Zjk) for assistance.