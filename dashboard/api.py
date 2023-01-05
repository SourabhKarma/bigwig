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

# total news
# total projects 
# total events
# total group






# -------------- dashboard api  S---------------------

from events.models import EventModel
from projects.models import ProjectModel
from dashboard.models import FeedModel
from groupchat.models import GroupModel
from user.models import User
from location.models import area,ward
from rest_framework.views import APIView
import base64



class DashboardView(APIView):



    def get(self,request):

        news= FeedModel.objects.count()
        projects =  ProjectModel.objects.count()
        events = EventModel.objects.count()
        group =   GroupModel.objects.count()
        user = User.objects.count()
        userk =  User.objects.filter(role_id = 1).count()
        areac = area.objects.count()
        areap = list(area.objects.all().values_list("id",flat=True))
        areaname = list(area.objects.all().values_list("area_name",flat=True))

        print(areaname)
        print(areap)
        a= []
        for x in areap:     
            usercount = User.objects.filter(area = x).count()
            a.append(usercount)
        print(a)
        res = dict(map(lambda i,j : (i,j) , areaname,a))
        print(res)
        wardc = ward.objects.count()
        # if Exception is True:
        #     return(JsonResponse({"a":"a"}))
        return JsonResponse({"news":news,"projects":projects,"events":events,"group":group,"users":user,"userk":userk,"areac":areac,"wardc":wardc,"area":res,"areaname":areaname,"areacount":a},status= status.HTTP_200_OK)


# ---------------- dashboard api E -------------------------



# api for user activity

class UserActivity(APIView):


    def post(self,request):
        data = request.data
        userid =  data["userid"]
        userlike = list(FeedLikeModel.objects.filter(user_id = userid).values())
        print(userlike)
        # projects =  ProjectModel.objects.filter(userid= )
        events = EventModel.objects.filter()
        group =   GroupModel.objects.filter()
        return JsonResponse({"a":userlike},status= status.HTTP_200_OK)

