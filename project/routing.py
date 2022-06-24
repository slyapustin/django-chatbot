import chat.routing
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket': URLRouter(
        chat.routing.websocket_urlpatterns
        ),
})
