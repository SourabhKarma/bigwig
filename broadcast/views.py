from logging import exception
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import FcmSerializer







 



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
    device_token = ["f7rIzMRS-tl75bWr3FzlA6:APA91bEHq2_gsg4iudkRSsqvnFpwGKwOEPQ6XMZ5rSPifn4Zek81BKETe7tnqus2m3qQJwkVjpCxs-gJTNOywRwe_RXyIU11-E3pkfWRH4XrbzEQWptI0ZVPu3Mh50g55TdP3rNyV9qm",
    "chYYTVFRF6gPKWmL1VFuq1:APA91bHhZTeq2FV829-IW0E459H3iHlCgLb4Ewl7twQAunS4GJ8rAVqwb2jW_1tpGY3-nxjmdfis8xd-arq-uqa4jitN44HRjRSw6tdJItTbRx8bxMVf-Q6rFs4PaqFqeKTRDaEKh6z5",
    "c837DoLxIyiPKGSI6MOyp0:APA91bEcLV11wmKcwtW0azMYOXgslPeQ81ww0INEoq4cRNuho0auhtLcTrmi8W-79WXOeUkrC9tB6Npfwmf2vINA2AjigvwqaYJH-JrQoLZHwC8MSrNhQFNUi57tvUhVJh7DZjCPt5tK",
    ]
    send_notification(device_token,"bigwig","added")
    return JsonResponse({"status": "success"}, safe=False)

