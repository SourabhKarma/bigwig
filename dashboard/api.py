from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets

from .models import VideoModel,FeedModel,FeedComments,FeedLikeModel
from .serializer import VideoSerializer,FeedSerializer,FeedCommentSerializer,FeedlikeSerializer
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
import base64
# base64.b64encode(b'your name')

'''(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet'''
# Create your views here.

class VideoView (mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.ListModelMixin,GenericViewSet):

    queryset = VideoModel.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (AllowAny,)
    # filter_fields = ["area_name",]   


class FeedView (mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.ListModelMixin,GenericViewSet):

    queryset = FeedModel.objects.all()
    serializer_class = FeedSerializer
    permission_classes = (AllowAny,) 
    


class FeedCommentView(viewsets.ModelViewSet):
    queryset = FeedComments.objects.all()
    serializer_class = FeedCommentSerializer
    filter_fields = ["feed_id",]   

    # def list(self, request):
    #     queryset = FeedComments.objects.all()
    #     filter_fields = ["feed_id",]   

    #     if not queryset:
    #         return JsonResponse({"message":"empty"},status = status.HTTP_400_BAD_REQUEST)
    #     # queryset = EventlikeModel.objects.filter()

    #     serializer = FeedCommentSerializer(queryset, many=True)

    #     return Response(serializer.data)


class FeedlikeView(viewsets.ModelViewSet):
    queryset = FeedLikeModel.objects.all()
    serializer_class = FeedlikeSerializer
    filter_fields = ["feed_ids",]  