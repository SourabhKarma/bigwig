from django.shortcuts import render
from rest_framework import viewsets
from .models import Advertisement,AdvertisementSubCategory,AdvertismentCategory
from .serializer import AdvertisementSerializer,AdvertisementSubCategorySerializer,AdvertismentCategorySerializer




# Create your views here.


class AdvertismentCategoryView(viewsets.ModelViewSet):
    queryset = AdvertismentCategory.objects.all()
    serializer_class = AdvertismentCategorySerializer



class AdvertisementSubCategoryView(viewsets.ModelViewSet):

    queryset = AdvertisementSubCategory.objects.all()
    serializer_class = AdvertisementSubCategorySerializer
    filter_fields = ["ads_category_id",]   



class AdvertisementView(viewsets.ModelViewSet):

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_fields = ["ads_category_id","ads_subcategory_id"]   

