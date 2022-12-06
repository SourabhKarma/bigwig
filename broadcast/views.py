from logging import exception
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import FcmSerializer

from .models import NotiModel





 



from rest_framework.views import APIView

class FCMDevicesListAPIView(APIView):

    permission_classes = (IsAuthenticated,)


from pyfcm import FCMNotification
from bigwig.settings import FCM_DJANGO_SETTINGS
from django.http import Http404, JsonResponse

def send_notification(registration_id,message_title, message_body):
   try:
      push_service = FCMNotification(api_key=FCM_DJANGO_SETTINGS['FCM_SERVER_KEY'])
    #   registration_id = []
      result=push_service.notify_multiple_devices(registration_id, message_title=message_title,
                                        message_body=message_body)
      return result
   except:
      raise exception

def send_noti(request):
   queryset =list(NotiModel.objects.values_list('device_key', flat=True))
   single_user = list(NotiModel.objects.filter(name = 'device2').values_list('device_key',flat=True))
   print(single_user)
   #index of 0 of user list is passing in group list index to remove that particular user id notification
   single_user.remove(single_user[0])

   # single_user.remove('chYYTVFRF6gPKWmL1VFuq1:APA91bHhZTeq2FV829-IW0E459H3iHlCgLb4Ewl7twQAunS4GJ8rAVqwb2jW_1tpGY3-nxjmdfis8xd-arq-uqa4jitN44HRjRSw6tdJItTbRx8bxMVf-Q6rFs4PaqFqeKTRDaEKh6z5')
   print(single_user)

   # print(queryset)



   #  a = list(queryset)
   #  print(a)
   #  device_token = ["tl75bWr3FzlA6:APA91bEHq2_gsg4iudkRSsqvnFpwGKwOEPQ6XMZ5rSPifn4Zek81BKETe7tnqus2m3qQJwkVjpCxs-gJTNOywRwe_RXyIU11-E3pkfWRH4XrbzEQWptI0ZVPu3Mh50g55TdP3rNyV9qm"
   #  ]
   device_token = queryset
   send_notification(device_token,"bigwig","added")
   return JsonResponse({"status": "success"}, safe=False)

