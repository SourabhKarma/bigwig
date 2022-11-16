from numpy import source
from rest_framework import serializers
from .models import VideoModel,FeedModel,FeedComments,FeedLikeModel
from drf_extra_fields.fields import Base64FileField
# from django.contrib.auth.models import User
from user.models import User





class VideoSerializer(serializers.ModelSerializer):
    title2 = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = VideoModel
        # fields = "__all__"
        fields = ("video_name","title2")



    def get_title2(self, place):
        data =  self.title2
        return "data:text;base64,%s" % data.encode('base64')


class FeedSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField(read_only = True)
    like_count = serializers.SerializerMethodField(read_only = True)


    class Meta:
        model = FeedModel
        fields = "__all__"

    def get_comment_count(self,obj):
        return obj.feedcomment.count()

    def get_like_count(self,obj):
        return obj.feedlike.count()








class userget(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","email")





class FeedCommentSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()
    # user_ids = serializers.PrimaryKeyRelatedField(read_only=False, queryset=User.objects.all())
    # user_ids = serializers.RelatedField(source='User', read_only=True)
    # user_id = serializers.SlugRelatedField(read_only=True, slug_field='commentuser')
    # user_id = serializers.CharField(source='userget.email', read_only=True)
    # user_id =  serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = FeedComments
        fields = ("id","comment_count","feed_id","user_id","feed_comment",)
        # depth = 1
    
    def get_comment_count(self,obj):
        return obj.feed_id.feedcomment.count()

    def get_user_name(self,obj):
        return obj.feed_id.feedcomment.count()


    # def __init__(self, *args, **kwargs):
    #     super(FeedCommentSerializer, self).__init__(*args, **kwargs)
    #     request = self.context.get('request')
    #     if request and request.method=='POST':
    #         self.Meta.depth = 0
    #     else:
    #         self.Meta.depth = 1



class FeedlikeSerializer(serializers.ModelSerializer):
    # feed_comment = FeedCommentSerializer
    like_count = serializers.SerializerMethodField(read_only = True)
    user_id = serializers.StringRelatedField()


    class Meta:
        model = FeedLikeModel
        fields = ("id","feed_ids","user_id","feed_like","like_count")
    
    def get_like_count(self,obj):
        return obj.feed_ids.feedlike.count()
