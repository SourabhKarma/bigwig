from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import JsonResponse
from grpc import Status, StatusCode
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status

from .models import Poll,Vote
from .serializers import votevalidateser

# def polls_list(request):
#     MAX_OBJECTS = 20
#     polls = Poll.objects.all()[:20]
#     data = {"results": list(polls.values(
#         "question", "created_by__username", "pub_date"))}
#     return JsonResponse(data)


# def polls_detail(request, pk):
#     poll = get_object_or_404(Poll, pk=pk)
#     data = {"results": {
#         "question": poll.question,
#         "created_by": poll.created_by.username,
#         "pub_date": poll.pub_date
#     }}
#     return JsonResponse(data)



class votevalidateview(APIView):

    def post(self, request):

        data = request.data
        serializer = votevalidateser(data=data)

        if serializer.is_valid():
            voted_by = serializer.data['voted_by'] 
            poll = serializer.data['poll'] 

            # otp = serializer.data['otp'] 
            

            vote = Vote.objects.filter(voted_by = voted_by)
            polls = Vote.objects.filter(poll = poll)


            if  vote.exists() and polls.exists():
                response = {
                    'success': True,
                    'statusCode':200,
                    'message': 'already voted',
                    'data':'voted',
                }
                return Response(response)
            # user = user.first()
        # return HttpResponse("no")
        # print(self.request.user)
        data = {"data":"not voted","status":status.HTTP_200_OK}
        return JsonResponse(data)