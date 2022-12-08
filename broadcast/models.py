from django.db import models
from django.db.models import signals
from django.dispatch import receiver 

# from fcm_django.models import FCMDevice

# from firebase_admin.messaging import Message
# device = FCMDevice.objects.all().first()
# device.send_message(Message(data={"a":"a"}))
# # Create your models here.
# def send_notification(user_ids,title, message, data):
#    try:
#       device = FCMDevice.objects.filter(user__in=user_ids).first()
#       result = device.send_message(title=title,body=message,
#                           data=data,sound=True)
#       return result
#    except:
#       pass



# data = {
#          "name": "HORN OK PLEASE!",
#          "days": 3,
#          "country": "United States"
#        }



# send_notification(user_ids=["1","2","3"],
#                   title="It's now or never: Horn Ok is back!",
#                   message="Book now to get 50% off!",
#                   data=data)


# from fcm_django.models import FCMDevice,AbstractFCMDevice




# class CustomFCMDevice(AbstractFCMDevice):
#     language = models.CharField(max_length=35, blank=False)
#     position = models.CharField(max_length=35, blank=False)
#     app_version = models.CharField(max_length=35, blank=False)















# def send_notification(user_id, title, message, data):
#     try:
#         device = FCMDevice.objects.filter(user=user_id).last()
#         result = device.send_message(title=title, body=message, data=data, 
#            sound=True)
#         return result
#     except:
#         pass



# send_notification(user_id=1, title="Order Return", message="yourmessage", data=None)













class NotiModel(models.Model):
    device_key = models.CharField(max_length=255, null=True,blank=True)
    name = models.CharField(max_length=255, null=True,blank=True)





from .views import send_notification    




class BroadCastModel(models.Model):
    title = models.CharField(max_length=255, null=True,blank=True)
    message = models.CharField(max_length=255, null=True,blank=True)

@receiver(signals.post_save, sender=BroadCastModel) 
def noti(sender, instance, created, **kwargs):

    queryset =list( NotiModel.objects.values_list('device_key', flat=True))
    print(queryset)
    device_token = queryset
    send_notification(device_token,instance.title,instance.message)
    # return JsonResponse({"status": "success"}, safe=False)