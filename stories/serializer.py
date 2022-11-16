from rest_framework import serializers
from .models import StoriesModel,StoriesComment,StoriesLikeModel,Item




class StoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoriesModel
        fields = '__all__'


class StoriesCommentSerializer(serializers.ModelSerializer):
    stories_comment_count = serializers.SerializerMethodField()

    class Meta:
        model = StoriesComment
        fields = ("id","stories_comment_count","stories_id","user_id","user_name","stories_comment")
    
    def get_stories_comment_count(self,obj):
        return obj.stories_id.storiescomment.count()

    # def get_user_name(self,obj):
    #     return obj.feed_id.feedcomment.count()



class StorieslikeSerializer(serializers.ModelSerializer):
    # feed_comment = FeedCommentSerializer
    stories_like_count = serializers.SerializerMethodField(read_only = True)
    # user_id = serializers.StringRelatedField()


    class Meta:
        model = StoriesLikeModel
        fields = ("id","stories_ids","user_id","stories_like","stories_like_count")
    
    def get_stories_like_count(self,obj):
        return obj.stories_ids.storieslike.count()




class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
