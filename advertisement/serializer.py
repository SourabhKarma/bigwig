
from rest_framework import serializers
from .models import Advertisement, AdvertisementSubCategory, AdvertismentCategory




class AdvertismentCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = AdvertismentCategory
        fields = "__all__"



class AdvertisementSubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = AdvertisementSubCategory
        fields = "__all__"




class AdvertisementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertisement
        fields = "__all__"
