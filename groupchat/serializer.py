from rest_framework import serializers
from .models import GroupModel,GroupChatModel,Message


class GroupChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupChatModel
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    group_message = GroupChatSerializer(many=True, read_only=True)

    class Meta:
        model = GroupModel
        fields = ["id","group_message"]



class GroupListSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupModel
        fields ='__all__'





class MessageSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model = Message
        fields ='__all__'







class GroupRemoveSerializer(serializers.ModelSerializer):
    groupid = serializers.CharField()
    userid = serializers.CharField()