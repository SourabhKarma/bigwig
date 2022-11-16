import base64
from encodings import utf_8
from django.contrib import admin

# Register your models here.
from .models import area,ward

# class areaAdmin(admin.ModelAdmin):
#     fields = ['area_name']

#     def save_model(self, request, obj, form, change):
#         obj.username = request.user
#         obj.area_name = base64.encode(str(obj.area_name),None)

#         print("yes")
#         return super(areaAdmin, self).save_model(request, obj, form, change)



admin.site.register(area)
admin.site.register(ward)