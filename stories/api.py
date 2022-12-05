from django.shortcuts import render
from base64 import b64encode
from rest_framework.response import Response
from .models import StoriesModel,StoriesComment,StoriesLikeModel,Item
from .serializer import StoriesSerializer,StoriesCommentSerializer,StorieslikeSerializer,ItemSerializer
from rest_framework import viewsets
from rest_framework import filters
from django_filters import FilterSet
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser , FormParser
from rest_framework.permissions import IsAdminUser , IsAuthenticated

from rest_framework.throttling import ScopedRateThrottle
from django.db.models import Q
# Create your views here.


class StoriesView(viewsets.ModelViewSet):

    queryset = StoriesModel.objects.all()
    serializer_class = StoriesSerializer
    filter_fields = ["stories_start"]
    parser_classes = (FormParser, MultiPartParser)

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.view_count = obj.view_count + 1
        obj.save(update_fields=("view_count", ))
        return super().retrieve(request, *args, **kwargs)


    # def patch(self, request, pk):
    #     testmodel_object = self.get_object(pk)
    #     serializer = StoriesSerializer(testmodel_object, data=request.data, partial=True) # set partial=True to update a data partially
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(code=201, data=serializer.data)
    #     return JsonResponse(code=400, data="wrong parameters")


    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = StoriesSerializer(instance=instance)
    #     a = [serializer.data]
    #     b64encode(bytes(a))
    #     return Response(a)


class StoriesCommentView(viewsets.ModelViewSet):

    queryset = StoriesComment.objects.all()
    serializer_class = StoriesCommentSerializer





class StoriesLikeView(viewsets.ModelViewSet):
    queryset = StoriesLikeModel.objects.all()
    serializer_class = StorieslikeSerializer
    filter_fields = ["stories_ids",]  



#---------------------- user list view ------------------------








#-----------------------user list view end --------------------



from rest_framework.throttling import ScopedRateThrottle

class ScopeTenPerTenMinutesThrottle(ScopedRateThrottle):
    

    rate = '1/s' # <<<<< This line is very important
    # You just can enter any rate you want it will directly be overwritten by parse_rate
    

    def parse_rate(self, rate):
        """
        Given the request rate string, return a two tuple of:
        <allowed number of requests>, <period of time in seconds>

        So we always return a rate for 10 request per 10 minutes.

        Args:
            string: rate to be parsed, which we ignore.

        Returns:
            tuple:  <allowed number of requests>, <period of time in seconds>
        """
        return (3, 120) # 10 Requests per 600 seconds (10 minutes)







from rest_framework.exceptions import Throttled
from rest_framework import status


class Throttl(Throttled):
    status_code = status.HTTP_429_TOO_MANY_REQUESTS
    pass


class ItemView(viewsets.ModelViewSet):
    throttle_scope = 'robots'
    throttle_classes = (ScopeTenPerTenMinutesThrottle,)
      
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = [IsAuthenticated,]


    # def get_permissions(self):
    #     if self.request.method in ['GET']:
    #         return [IsAdminUser()]
    #     return [IsAuthenticated()]

    def throttled(self, request, wait):
        # status_code = status.HTTP_403_FORBIDDEN
        a= round(float(wait/60),2)
        raise Throttl(detail={
              "message":"request limit exceeded",
              "availableIn":f"{a} minutes",
            #   "throttleType":"type",
            #   "statuscode": status.HTTP_400_BAD_REQUEST
        })


