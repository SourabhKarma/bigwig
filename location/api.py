from encodings import utf_8
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from yaml import serialize
from .models import area,ward
from .serializer import area_serializer,ward_serializer
from rest_framework.permissions import AllowAny
import base64
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView

from broadcast.models import send_notification






from base64 import b64encode



class areab(viewsets.ViewSet):


    def list(self, request):
        queryset =  area.objects.all()
        serializers = area_serializer(queryset,many = True)
        ser = serializers.data
        serializer = base64.b64encode(bytes(str(ser),"utf_8"))
        response = {
            'success': True,
            # 'statusCode': status_code,
            'message': 'area list',

            'data': serializer,

        }   
        # return JsonResponse({"m":serializer})

        return Response(response)














# class areab(APIView):


#     def get(self, request):
#         # data = request.data
#         # serializer = self.serializer_class(data=request.data)

#         # serializer.is_valid(raise_exception=True)
#         # serializer.save()
#         a = "हिन्दी में टाइप करें" 
#         b = b64encode(bytes(str(a),'utf_8'))
#         return Response({'staus' : b ,} )


# try 2


    # def get(self, request, format=None):
    #     """
    #     Return a list of all users.
    #     """
    #     areanames = [area.area_name for area in area.objects.all()]
    #     b = b64encode(bytes(str(areanames),'utf_8'))
    #     return JsonResponse({"m":b})








class area_view(viewsets.ModelViewSet):
    queryset = area.objects.all()
    serializer_class = area_serializer
    permission_classes = (AllowAny,)
    filter_fields = ["area_name",]
    # ordering_fields = '__all__'
    # renderer_classes = (JSONRenderer,)
    # def get(self,request):
    #     items = area.objects.all()
    #     itemss = b64encode(bytes(str(items)))
    #     serializer = area_serializer(itemss, many=True)
    #     return Response(serializer.data)







class ward_view(viewsets.ModelViewSet):

    queryset = ward.objects.all()
    serializer_class = ward_serializer
    permission_classes = (AllowAny,)
    # search_fields = ["area_name"]
    filter_fields = ["area_id",]







