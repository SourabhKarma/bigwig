

# from .models import BroadCastModel,NotiModel
# from .views import send_notification    
# from django.db.models import signals
# from django.dispatch import receiver 









# @receiver(signals.post_save, sender=BroadCastModel) 
# def noti(sender, instance, created, **kwargs):

#     queryset =list( NotiModel.objects.values_list('device_key', flat=True))
#     print(queryset)
#     device_token = queryset
#     send_notification(device_token,instance.title,instance.message)
#     # return JsonResponse({"status": "success"}, safe=False)