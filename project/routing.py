from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': URLRouter(
        chat.routing.websocket_urlpatterns
        ),
})
