from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import generics, viewsets

from rest_framework import generics, status  
from rest_framework.response import Response  

# Create your views here.





class CountryView(generics.ListCreateAPIView):  
    queryset = CountryName1.objects.all()  
    serializer_class = CountryNameSerializer  
    
    def create(self, request, *args, **kwargs):  
        serializer = self.get_serializer(data=request.data, many=True)  
        serializer.is_valid(raise_exception=True)  
    
        try:  
            self.perform_create(serializer)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        except:  
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  








class TeslaModelListCreateAPIView(viewsets.ModelViewSet):
    queryset = TeslaModel1.objects.all()
    serializer_class = TeslaModelSerializer


class CountryNameListCreateAPIView(viewsets.ModelViewSet):
    queryset = CountryName1.objects.all()
    serializer_class = CountryNameSerializer