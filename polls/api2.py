from pyexpat import model
from urllib import response
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.core.exceptions import PermissionDenied
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
import django_filters.rest_framework


from .models import Poll, Choice, Vote
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer,PollSerializerNoVotes,PollSerializerCount

class PollList(mixins.ListModelMixin,GenericViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    filter_fields  = ["vote"]
    search_fields  = ["vote"]



# class PollDetail(generics.RetrieveDestroyAPIView):
#     queryset = Poll.objects.all()
#     serializer_class = PollSerializer


class PollDetail(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializerNoVotes






class ChoiceList(generics.ListCreateAPIView):
    serializer_class = ChoiceSerializer

    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs["pk"])
        return queryset

    def post(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk=self.kwargs["pk"])
        if not request.user == poll.created_by:
            raise PermissionDenied("You can not create choice for this poll.")
        return super().post(request, *args, **kwargs)


class CreateVote(APIView):

    def post(self, request, pk, choice_pk):
        voted_by = request.data.get("voted_by")
        data = {'choice': choice_pk, 'poll': pk, 'voted_by': voted_by}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializerCount

    # def destroy(self, request, *args, **kwargs):
    #     poll = Poll.objects.get(pk=self.kwargs["pk"])
    #     if not request.user == poll.created_by:
    #         raise PermissionDenied("You can not delete this poll.")
    #     return super().destroy(request, *args, **kwargs)





# vote view api
# class VoteViewSet(mixins.ListModelMixin,GenericViewSet):
from django_filters import rest_framework as filters
class AccountTFilter(filters.FilterSet):
    class Meta:
        model = Vote
        fields = ["poll","voted_by"]
        together =["poll","voted_by"]   

class VoteViewSet(viewsets.ModelViewSet):


    queryset = Vote.objects.all()

    serializer_class = VoteSerializer
    filter_fields  = ["poll","voted_by",]

    # search_fields  = ["poll","voted_by",]
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filter_class = AccountTFilter
    # def get_queryset(self):
    #     queryset = Vote.objects.all()

    #     if queryset.exists():
    #         # serializer = VoteSerializer()
    #         # a = [{"a":"a"}]
    #         return queryset
    #     else:
    #         raise Http404

    # def get_queryset(self):
    #     params = VoteSerializer(self.request.query_params)
    #     return params.is_valid(raise_exception=True)

    # if not queryset.exists():
    #     return HttpResponse(status=404)
    # def get_queryset(self):
    #     queryset = self.queryset
    #     if queryset is not None:
    #         queryset = Vote.objects.all()
    #         print(queryset)
    #         return queryset


        # raise Http404
