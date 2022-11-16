# app/consumers.py
import json
from tokenize import group
from django.http import HttpResponse, JsonResponse
from .models import Message,GroupModel
from user.models import User
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from asgiref.sync import sync_to_async
from channels.generic.websocket import WebsocketConsumer

from urllib.parse import parse_qsl
from django.core.cache import cache



class TextRoomConsumer(AsyncWebsocketConsumer):


    @database_sync_to_async
    def get_userid(self,userid):
        return User.objects.get(id =userid)



    @database_sync_to_async
    def get_groupid(self,groupid):
        return GroupModel.objects.get(id =groupid)
        # return Message.objects.get(groupid = 1)
    # groupInt  groupid

    @database_sync_to_async
    def create_chat(self, sender, text,group,time,user ):
        Message.objects.create(userid = user,sender=sender, message = text ,groupid= group, time = time )

    @database_sync_to_async
    def get_oldchat(self):
        return Message.objects.all()


    async def connect(self):
        try:
            # user = self.scope["user"]
            query_string = self.scope['query_string'].decode('utf-8')
            print(query_string)
            query_params = dict(parse_qsl(query_string))
            print(query_params)
            ticket_uuid = query_params.get('has_ticket')
            print(ticket_uuid)
            print(cache.get("token"))
            self.scope['has_ticket'] = cache.get("token")
            print(self.scope['has_ticket'])
            self.room_name = self.scope['url_route']['kwargs']['room_name']
            self.room_group_name = 'chat_%s' % self.room_name
            # print(self.room_group_name) 

            # Join room group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name,
                # user,
            )

            # if ticket_uuid == cache.get("token"):
            if ticket_uuid == self.scope['has_ticket']:

                print("aaaaaaa")
                await self.accept()
                # await self.get_oldchat(self)
                # print(self.get_oldchat(self))
                cache.delete("token")
                print(cache.get("token"))


            # self.scope['has_ticket'] = cache.get("token")
            # print(self.scope['has_ticket'])
            # if not cache.delete(ticket_uuid): 
            #         raise Exception('ticket not found')
        except:
            print("bbbbbb")
            await self.close()
            return 

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # print(self.room_group_name)

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
            # user,
        )

        # await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):

        # sender1 = self.scope["sender"].first_name
        # name = self.scope['sender'].username
        # print(sender1,name)
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']
        # message = (sender + '(' + name + ')' + ':\n' + message)


        text_data_json = json.loads(text_data)


        userid = text_data_json['userid']
        text = text_data_json['text']
        sender = text_data_json['sender']
        # group = await sync_to_async(GroupModel.objects.get(id='1'))
        groupid =  text_data_json['groupid']


        user = await self.get_userid(userid)
        group  = await self.get_groupid(groupid)
        # print(group)
        time = text_data_json['time']

        await self.create_chat(sender ,text,group,time,user)  


        # Send message to room group
        await (self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': text,
                'sender': sender,
                'userid':userid,
                'time':time,
                'groupid':groupid,
            }
        )


    # Receive message from room group
    async def chat_message(self, event,):

        # print(self.get_oldchat())
        # text_data_json = json.loads(text_data)
        # print(text_data_json)
        # username = self.scope["user"].username
        # message = event['message']
        # name = self.scope["user"].username



        mess = await self.get_oldchat()




                
        text = event['message']
        sender = event['sender']
        # group = event['group']
        time = event['time']
        user  = event['userid']
        group = event['groupid']

        # Send message to WebSocket
        # await self.create_chat(sender ,text)  # It is necessary to await creation of messages


        await self.send(text_data=json.dumps({
            'text': text,
            'sender': sender,
            'userid':user,
            'time':time,
            'groupid':group,
        }))






















# --------------------------- with out uuid -------------------


# class TextRoomConsumer(AsyncWebsocketConsumer):


#     @database_sync_to_async
#     def get_userid(self,userid):
#         return User.objects.get(id =userid)



#     @database_sync_to_async
#     def get_groupid(self,groupid):
#         return GroupModel.objects.get(id =groupid)
#         # return Message.objects.get(groupid = 1)
#     # groupInt  groupid

#     @database_sync_to_async
#     def create_chat(self, sender, text,group,time,user ):
#         Message.objects.create(userid = user,sender=sender, message = text ,groupid= group, time = time )

#     @database_sync_to_async
#     def get_oldchat(self):
#         return Message.objects.all()


#     async def connect(self):
      

#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name
#         # print(self.room_group_name)

#         # Join room group
#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name,
#             # user,
#         )

#         # await self.accept()

#     async def disconnect(self, close_code):
#         # Leave room group
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )

#     # Receive message from WebSocket
#     async def receive(self, text_data):

#         # sender1 = self.scope["sender"].first_name
#         # name = self.scope['sender'].username
#         # print(sender1,name)
#         # text_data_json = json.loads(text_data)
#         # message = text_data_json['message']
#         # message = (sender + '(' + name + ')' + ':\n' + message)


#         text_data_json = json.loads(text_data)


#         userid = text_data_json['user']
#         text = text_data_json['text']
#         sender = text_data_json['sender']
#         # group = await sync_to_async(GroupModel.objects.get(id='1'))
#         groupid =  text_data_json['group']


#         user = await self.get_userid(userid)
#         group  = await self.get_groupid(groupid)
#         # print(group)
#         time = text_data_json['time']

#         await self.create_chat(sender ,text,group,time,user)  


#         # Send message to room group
#         await (self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': text,
#                 'sender': sender,
#                 # 'group':group,
#                 'time':time,
#             }
#         )


#     # Receive message from room group
#     async def chat_message(self, event,):

#         # print(self.get_oldchat())
#         # text_data_json = json.loads(text_data)
#         # print(text_data_json)
#         # username = self.scope["user"].username
#         # message = event['message']
#         # name = self.scope["user"].username



#         mess = await self.get_oldchat()




                
#         text = event['message']
#         sender = event['sender']
#         # group = event['group']
#         time = event['time']

#         # Send message to WebSocket
#         # await self.create_chat(sender ,text)  # It is necessary to await creation of messages


#         await self.send(text_data=json.dumps({
#             'text': text,
#             'sender': sender,
#             # 'group':group,
#             'time':time
#         }))
