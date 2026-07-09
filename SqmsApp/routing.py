from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/queue/global/", consumers.QueueConsumer.as_asgi()),
    path("ws/queue/<int:ticket_number>/", consumers.QueueConsumer.as_asgi()),
]