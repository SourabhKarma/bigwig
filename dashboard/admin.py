from django.contrib import admin
from .models import VideoModel,FeedModel,FeedComments,FeedLikeModel
# Register your models here.

admin.site.register(VideoModel)
admin.site.register(FeedModel)
admin.site.register(FeedComments)
admin.site.register(FeedLikeModel)