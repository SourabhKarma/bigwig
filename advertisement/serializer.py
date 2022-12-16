
from rest_framework import serializers
from .models import Advertisement, AdvertisementSubCategory, AdvertismentCategory




class AdvertismentCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = AdvertismentCategory
        fields = "__all__"



class AdvertisementSubCategorySerializer(serializers.ModelSerializer):
    # ads_category_id = serializers.PrimaryKeyRelatedField(queryset=AdvertismentCategory.objects.all(), many=False)
    class Meta:
        model = AdvertisementSubCategory
        fields = "__all__"

    # def to_representation(self, instance):
    #     print(instance)
    #     response = super().to_representation(instance)
    #     print(response)
    #     response['ads_category_id'] = instance.ads_category_id.ads_category
    #     # response['item'] = instance.item.name
    #     # response['price'] = instance.item.price
    
    #     return response


class AdvertisementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertisement
        fields = "__all__"


    def to_representation(self, instance):
        print(instance)
        response = super().to_representation(instance)
        print(response)
        response['ads_category_id'] = instance.ads_category_id.ads_category
        response['ads_subcategory_id'] = instance.ads_subcategory_id.ads_subcategory
        # response['price'] = instance.item.price
    
        return response