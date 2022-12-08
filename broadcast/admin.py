from django.contrib import admin
from .models import NotiModel,BroadCastModel
# Register your models here.



# admin.site.register(CustomFCMDevice)
admin .site.register(NotiModel)
admin.site.register(BroadCastModel)