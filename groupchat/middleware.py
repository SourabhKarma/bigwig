
from django.db import close_old_connections
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from jwt import decode as jwt_decode
from django.conf import settings
from django.contrib.auth import get_user_model
from urllib.parse import parse_qs
from user.models import User

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from asgiref.sync import sync_to_async












from django.contrib.auth.models import AnonymousUser
from channels.middleware import BaseMiddleware
from channels.auth import AuthMiddlewareStack


@database_sync_to_async
def get_user(validated_token):
    try:
        user = get_user_model().objects.get(id=validated_token["user_id"])
        # return get_user_model().objects.get(id=toke_id)
        print(f"{user}")
        return user

    except User.DoesNotExist:
        return AnonymousUser()



class JwtAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
       # Close old database connections to prevent usage of timed out connections
        close_old_connections()

        # Get the token
        token = parse_qs(scope["query_string"].decode("utf8"))["token"][0]

        # Try to authenticate the user
        try:
            # This will automatically validate the token and raise an error if token is invalid
            UntypedToken(token)
        except (InvalidToken, TokenError) as e:
            # Token is invalid
            print(e)
            return None
        else:
            #  Then token is valid, decode it
            decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            print(decoded_data)
            # Will return a dictionary like -
            # {
            #     "token_type": "access",
            #     "exp": 1568770772,
            #     "jti": "5c15e80d65b04c20ad34d77b6703251b",
            #     "user_id": 6
            # }

            # Get the user using ID
            scope["user"] = await get_user(validated_token=decoded_data)
        return await super().__call__(scope, receive, send)


def JwtAuthMiddlewareStack(inner):
    return JwtAuthMiddleware(AuthMiddlewareStack(inner))








































class TokenAuthMiddleware:
    """
    Custom token auth middleware
    """
 
    def __init__(self, inner):
        # Store the ASGI application we were passed
        self.inner = inner
 
    def __call__(self, scope):
 
        # Close old database connections to prevent usage of timed out connections
        close_old_connections()
 
        # Get the token
        token = parse_qs(scope["query_string"].decode("utf8"))["token"][0]
        print(token)
        # Try to authenticate the user
        try:
            # This will automatically validate the token and raise an error if token is invalid
            UntypedToken(token)
        except (InvalidToken, TokenError) as e:
            # Token is invalid
            return None
        else:
            #  Then token is valid, decode it
            decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            print(decoded_data)
            # Will return a dictionary like -
            # {
            #     "token_type": "access",
            #     "exp": 1568770772,
            #     "jti": "5c15e80d65b04c20ad34d77b6703251b",
            #     "user_id": 6
            # }
 
            # Get the user using ID
            # user = get_user_model().objects.get(id=decoded_data["user_id"])
            user = get_user_model().objects.get(id=decoded_data["user_id"])

 
        # Return the inner application directly and let it run everything else
        return self.inner(dict(scope, user=user))































































































































































# ------------------------------------------ 11/11 ----------------------------------------





# from django.contrib.auth.models import AnonymousUser
# from rest_framework.authtoken.models import Token
# from channels.db import database_sync_to_async
# from channels.middleware import BaseMiddleware

# @database_sync_to_async
# def get_user(token_key):
#     try:
#         token = Token.objects.get(key=token_key)
#         return token.user
#     except Token.DoesNotExist:
#         return AnonymousUser()


# class TokenAuthMiddleware(BaseMiddleware):
#     def __init__(self, inner):
#         super().__init__(inner)

#     async def __call__(self, scope, receive, send):
#         try:
#             token_key = dict(scope['headers'])[b'sec-websocket-protocol'].decode('utf-8')
#         except ValueError:
#             token_key = None
#         scope['user'] = AnonymousUser() if token_key is None else await get_user(token_key)
#         return await super().__call__(scope, receive, send)



# # from django.contrib.auth.models import AnonymousUser
# # from rest_framework.authtoken.models import Token
# # from channels.db import database_sync_to_async
# # from channels.middleware import BaseMiddleware

# # @database_sync_to_async
# # def get_user(token_key):
# #     try:
# #         token = Token.objects.get(key=token_key)
# #         return token.user
# #     except Token.DoesNotExist:
# #         return AnonymousUser()

# # class TokenAuthMiddleware(BaseMiddleware):
# #     def __init__(self, inner):
# #         super().__init__(inner)

# #     async def __call__(self, scope, receive, send):
# #         try:
# #             token_key = (dict((x.split('=') for x in scope['query_string'].decode().split("&")))).get('token', None)
# #         except ValueError:
# #             token_key = None
# #         scope['user'] = AnonymousUser() if token_key is None else await get_user(token_key)
# #         return await super().__call__(scope, receive, send)




# import traceback
# from urllib.parse import parse_qs

# from channels.auth import AuthMiddlewareStack
# from channels.db import database_sync_to_async
# from django.conf import settings
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import AnonymousUser
# from django.db import close_old_connections
# from jwt import decode as jwt_decode
# from jwt import InvalidSignatureError, ExpiredSignatureError, DecodeError


# User = get_user_model()


# class JWTAuthMiddleware:
#     def __init__(self, app):
#         self.app = app

#     async def __call__(self, scope, receive, send):
#         close_old_connections()
#         try:
#             jwt_token_list = ""
#             if(jwt_token_list == parse_qs(scope["query_string"].decode("utf8")).get('token', None)):
#                 jwt_token = jwt_token_list[0]
#                 jwt_payload = self.get_payload(jwt_token)
#                 user_credentials = self.get_user_credentials(jwt_payload)
#                 user = await self.get_logged_in_user(user_credentials)
#                 scope['user'] = user
#             else:
#                 scope['user'] = AnonymousUser()
#         except (InvalidSignatureError, KeyError, ExpiredSignatureError, DecodeError):
#             traceback.print_exc()
#         except:
#             scope['user'] = AnonymousUser()
#         return await self.app(scope, receive, send)

#     def get_payload(self, jwt_token):
#         payload = jwt_decode(
#             jwt_token, settings.SECRET_KEY, algorithms=["HS256"])
#         return payload

#     def get_user_credentials(self, payload):
#         """
#         method to get user credentials from jwt token payload.
#         defaults to user id.
#         """
#         user_id = payload['user_id']
#         return user_id

#     async def get_logged_in_user(self, user_id):
#         user = await self.get_user(user_id)
#         return user

#     @database_sync_to_async
#     def get_user(self, user_id):
#         try:
#             return User.objects.get(id=user_id)
#         except User.DoesNotExist:
#             return AnonymousUser()


# def JWTAuthMiddlewareStack(app):
#     return JWTAuthMiddleware(AuthMiddlewareStack(app))




