from .models import EventModel,EventlikeModel
from rest_framework import serializers





class EventLikeSerializer(serializers.ModelSerializer):

    # total_likes  = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = EventlikeModel
        fields = '__all__'


    # def get_total_likes(self,obj):
    #     return obj.event_char.count()
    




class EventSerializer(serializers.ModelSerializer):
    people = serializers.SerializerMethodField()

    class Meta:
        model = EventModel
        fields = '__all__'




# class EventResultsSerializer(serializers.ModelSerializer):
#     people = EventLikeSerializer(many= True, read_only = True)
#     class Meta:
#         model = EventModel
#         fields = '__all__'