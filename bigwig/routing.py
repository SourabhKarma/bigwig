from channels.routing import ProtocolTypeRouter, URLRouter
# import app.routing
from django.urls import re_path
from groupchat.consumers import TextRoomConsumer
from groupchat.middleware import TokenAuthMiddleware,JwtAuthMiddlewareStack
from django.conf.urls import url







# ------------------------ default ------------------
websocket_urlpatterns = [
    url(r'^ws/(?P<room_name>[^/]+)/$', TextRoomConsumer.as_asgi()),
]
# the websocket will open at 127.0.0.1:8000/ws/<room_name>
application = ProtocolTypeRouter({
    'websocket':
        URLRouter(
            websocket_urlpatterns
        )
    ,
})
# ------------------------ default end ------------------










# # ------------------------ default ------------------
# websocket_urlpatterns = [
#     re_path(r'^ws/(?P<room_name>[^/]+)/$', TextRoomConsumer.as_asgi()),
# ]
# # the websocket will open at 127.0.0.1:8000/ws/<room_name>
# application = ProtocolTypeRouter({
#     'websocket':JwtAuthMiddlewareStack(
#         URLRouter(
#             websocket_urlpatterns
#         )
#     ,)
# })
# # ------------------------ default end ------------------



























# websocket_urlpatterns = [
#     re_path(r'^ws/(?P<room_name>[^/]+)/$', TextRoomConsumer.as_asgi()),
# ]
# # the websocket will open at 127.0.0.1:8000/ws/<room_name>
# application = ProtocolTypeRouter({
#     # "http": get_asgi_application(),
#     'websocket':JwtAuthMiddlewareStack(
#         URLRouter(
#             websocket_urlpatterns
#         )
#     ),
# })







# from django.urls import re_path
# from channels.security.websocket import AllowedHostsOriginValidator
# from channels.routing import ProtocolTypeRouter, URLRouter
# from groupchat.middleware import TokenAuthMiddleware
# from groupchat.consumers import TextRoomConsumer

# websocket_urlpatterns = [
#     re_path(r'^ws/(?P<room_name>[^/]+)/$', TextRoomConsumer.as_asgi()),
# ]
#                         # url(r"^main/$", MainConsumer.as_asgi()),


# application = ProtocolTypeRouter({
#         'websocket':AllowedHostsOriginValidator(
#             TokenAuthMiddleware(
#                 URLRouter(
#                     websocket_urlpatterns
#                 )
            
#         ))
#     })
