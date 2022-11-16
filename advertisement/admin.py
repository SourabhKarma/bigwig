from django.contrib import admin
from .models import Advertisement,AdvertisementSubCategory,AdvertismentCategory
# Register your models here.



admin.site.register(Advertisement)
admin.site.register(AdvertisementSubCategory)
admin.site.register(AdvertismentCategory)