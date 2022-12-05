from .models import Message
from .serializer import MessageSerializer
from rest_framework import viewsets
import django_filters



class MessageFilter(django_filters.FilterSet):

    groupInt = django_filters.CharFilter(name = "groupInt")

    class Meta:
        model = Message
        fields = ['groupInt',]





class BorrowedViewset(viewsets.ModelViewSet):
   queryset = Message.objects.all()
   serializer_class = MessageSerializer

   def get_queryset(self):
       qs = super().get_queryset()
       only_missing = str(self.request.query_params.get('missing')).lower()
       if only_missing in ['true', '1']:
           return qs.filter(returned__isnull=True)
       return qs 