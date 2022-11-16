from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
# Create your views here.
from .models import FeedBack
from .serializer import FeedBackSerializer
from rest_framework import pagination,generics

class FeedBackPage(pagination.PageNumberPagination):
    page_size = 1


class FeedBackView(viewsets.ModelViewSet):

    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer
    permission_classes = (AllowAny,)
    filter_fields = ["userid","pollsid"]
    pagination_class = FeedBackPage