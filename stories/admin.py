from django.contrib import admin
from .models import StoriesModel,StoriesLikeModel,StoriesComment,Item

# Register your models here.

admin.site.register(StoriesModel)
admin.site.register(StoriesLikeModel)
admin.site.register(StoriesComment)
admin.site.register(Item)
