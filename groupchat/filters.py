from .models import Message
from .serializer import MessageSerializer
import django_filters



class MessageFilter(django_filters.FilterSet):

    groupInt = django_filters.CharFilter(name = "groupInt")

    class Meta:
        model = Message
        fields = ['groupInt',]