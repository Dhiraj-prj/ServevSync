# ServeSync/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import HOME.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ServeSync.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            HOME.routing.websocket_urlpatterns  # Points to the websocket patterns
        )
    ),
})
