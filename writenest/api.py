from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import generics, viewsets
# Create your views here.









class TeslaModelListCreateAPIView(viewsets.ModelViewSet):
    queryset = TeslaModel1.objects.all()
    serializer_class = TeslaModelSerializer


class CountryNameListCreateAPIView(viewsets.ModelViewSet):
    queryset = CountryName1.objects.all()
    serializer_class = CountryNameSerializer