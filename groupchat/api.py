from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated
from django_filters import filterset
from rest_framework import generics
from user.models import User
from .filters import MessageFilter
from .models import GroupModel,GroupChatModel, Message
from .serializer import GroupSerializer,GroupChatSerializer,GroupListSerializer,MessageSerializer
from .permissions import IsInGroup
from django_filters import rest_framework as filters
from rest_framework.exceptions import ValidationError
# Create your views here.


class GroupView(viewsets.ModelViewSet):

    queryset = GroupModel.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
    filter_fields = ["id"]




class GroupChatView(viewsets.ModelViewSet):

    queryset = GroupChatModel.objects.all()
    serializer_class = GroupChatSerializer
    filter_fields = ["group_id"]
        # permission_classes = [IsInGroup]



class GroupListView(viewsets.ModelViewSet):

    queryset = GroupModel.objects.all()
    serializer_class = GroupListSerializer
    # permission_classes = [IsInGroup]
    # filter_fields = ["id"]

    # def list(self, request):
    #     queryset = GroupModel.objects.filter(group_members = self.request.user)
    #     if not queryset:
    #         return JsonResponse({"message":"empty"},status = status.HTTP_400_BAD_REQUEST)
    #     # queryset = EventlikeModel.objects.filter()

    #     serializer = GroupListSerializer(queryset, many=True)
    #     return Response(serializer.data)







class MessageView(viewsets.ModelViewSet):


    queryset = Message.objects.all().exclude(groupInt__iexact=None)
    serializer_class = MessageSerializer
    filter_fields = ["groupid"]
    # def get_queryset(self):
    #     # queryset = Message.objects.filter(groupInt__isnull=False)
    #     queryset = Message.objects.all().exclude(groupInt__iexact=None)

    #     print(queryset)

    #     if  queryset.exists():
    #         print(queryset)
    #         return queryset

    #         # raise Response(status=status.HTTP_204_NO_CONTENT)
    #         # raise ValidationError({"error": ["You don't have enough permission."]})
    #     else:
    #         # return queryset
    #         raise ValidationError({"error": ["You don't have enough permission."]})








#--------------- channels jwt uuid -------------------------------------------

from django.core.cache import cache
from django.core.cache import caches  
from uuid import uuid4
from rest_framework.views import APIView
from user.serializer import UserListSerializer
# from django.contrib.auth import 
class RegisterFilterAPIView(viewsets.ModelViewSet):
    """
        get:
            API view for retrieving ticket uuid.
    """
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    # authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    # def list(self, request, *args, **kwargs):
    #     ticket_uuid = str(uuid4())

    #     if request.user.is_au:
    #         return HttpResponse({"as":"as"})
    #     else:
    #         # You can set any condition based on logged in user here
    #         cache.set(ticket_uuid)

    # request.user.is_authenticated
    #     return Response({'ticket_uuid': ticket_uuid})

    def list(self, request):

        ticket_uuid = str(uuid4())
        queryset = GroupModel.objects.filter(group_members = self.request.user)
        print(queryset)
        # queryset = User.objects.filter(id = self.request.user.id)
        if not queryset:
            return JsonResponse({"message":"empty"},status = status.HTTP_400_BAD_REQUEST)
        # queryset = EventlikeModel.objects.filter()
        # m_cache = caches.all()[0]
        cache.set("token",ticket_uuid)
        print(cache.get("token"))

        return Response({'ticket_uuid': ticket_uuid})