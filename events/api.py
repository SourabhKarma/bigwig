from base64 import b64encode
from django.shortcuts import render
from rest_framework import viewsets
from .models import EventModel,EventlikeModel
from .serializer import EventSerializer,EventLikeSerializer
from rest_framework.response import Response
# from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework import filters
# Create your views here.


class EventView(viewsets.ModelViewSet):
    queryset = EventModel.objects.all()
    serializer_class = EventSerializer
    # filter_fields = ["intrested_user"]
    # search_filter = ["intrested_user"]

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = EventSerializer(instance=instance)

    #     return Response(serializer.data)

class EventLikeView(viewsets.ModelViewSet):
    queryset = EventlikeModel.objects.filter()
    serializer_class = EventLikeSerializer
    filter_fields = ["event_choice"]
    # search_filter = ["intrested_user"]    

    def list(self, request):
        queryset = EventlikeModel.objects.filter(userid = self.request.user)
        # queryset = EventlikeModel.objects.filter()

        serializer = EventLikeSerializer(queryset, many=True)
        return Response(serializer.data)



# class eventdoubleview(ObjectMultipleModelAPIView):
#         querylist = [
#         {'queryset': EventModel.objects.all(), 'serializer_class': EventSerializer},
#         {'queryset': EventlikeModel.objects.all(), 'serializer_class': EventLikeSerializer},
        
#     ]
#         filter_backends = (filters.SearchFilter,)
#         search_fields = ('event_name','event_choice')