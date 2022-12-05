from django.db import models
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


from fcm_django.models import FCMDevice,AbstractFCMDevice




class CustomFCMDevice(AbstractFCMDevice):
    language = models.CharField(max_length=35, blank=False)
    position = models.CharField(max_length=35, blank=False)
    app_version = models.CharField(max_length=35, blank=False)















def send_notification(user_id, title, message, data):
    try:
        device = FCMDevice.objects.filter(user=user_id).last()
        result = device.send_message(title=title, body=message, data=data, 
           sound=True)
        return result
    except:
        pass



send_notification(user_id=1, title="Order Return", message="yourmessage", data=None)