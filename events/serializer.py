from .models import EVENT_CHOICES, EventModel,EventlikeModel
from rest_framework import serializers
from collections import Counter
# from django.db.models import Count




class EventLikeSerializer(serializers.ModelSerializer):

    # total_likes  = serializers.SerializerMethodField(read_only=True)
    total_yes = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = EventlikeModel
        fields = '__all__'

    def get_total_yes(self,obj):
        print(Counter(str(obj.event_choice)))
        # print(str(obj.event_choice).count("0"))
        # for  x in list(str(obj.event_choice)):
        #     if x == "0":
        #         a = a+1
        #     print(a)

        return obj.eventid




    # def get_total_likes(self,obj):
    #     return obj.event_char.count()
    

  


class EventSerializer(serializers.ModelSerializer):

    event_count = serializers.SerializerMethodField(read_only=True,required =False)
    # event_choice = serializers.SerializerMethodField(read_only=True,required =False)
    # event_choice = serializers.IntegerField()

    questions =serializers.SerializerMethodField()
    class Meta:
        model = EventModel
        fields = ['id','event_count','event_name','questions']


    def get_event_count(self, obj):
        return obj.event_count.count()

    def get_questions(self,obj):
        print (EventlikeModel.objects.filter(event_choice = 0).count(),"dddddddddddd",obj.id)
        # print (EventlikeModel.objects.filter(event_choice = 0).all(),"aaaaa")

        # return EventlikeModel.objects.filter(event_choice=0)













# class EventResultsSerializer(serializers.ModelSerializer):
#     people = EventLikeSerializer(many= True, read_only = True)
#     class Meta:
#         model = EventModel
#         fields = '__all__'