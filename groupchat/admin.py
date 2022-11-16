from django.contrib import admin
from .models import GroupModel,GroupChatModel,Message
# Register your models here.


class time(admin.ModelAdmin):
    readonly_fields = ('time',)




admin.site.register(Message,time)

admin.site.register(GroupModel)
admin.site.register(GroupChatModel)