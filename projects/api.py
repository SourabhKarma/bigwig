from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions, exceptions, status
from .models import ProjectModel,ProjectTask
from .serializer import ProjectSerializer,ProjectTaskSerializer,ProjectTaskupdateSerializer
from .permission import AuthorAllStaffAllButEditOrReadOnly,IsobjectUser,IsOwner
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser,IsAuthenticated,SAFE_METHODS
from django.db.models import Q
# Create your views here.



class ProjectView(viewsets.ModelViewSet):


    queryset = ProjectModel.objects.all()

    serializer_class = ProjectSerializer
    # filter_fields  = ["","",]

# ------------ working--------------

# class ProjectTaskView(viewsets.ModelViewSet):

#     queryset = ProjectTask.objects.all()
#     serializer_class = ProjectTaskSerializer
#     filter_fields  = ["projectid"]
#     # permission_classes = [IsOwner,IsAuthenticated]

#     def list(self, request):
#         queryset = ProjectTask.objects.filter(Q(task_role_id = self.request.user)|Q())
#         if not queryset:
#             return JsonResponse({"message":"empty"},status = status.HTTP_400_BAD_REQUEST)
#         # queryset = EventlikeModel.objects.filter()

#         serializer = ProjectTaskSerializer(queryset, many=True)
#         return Response(serializer.data)

#     # def update(self):
#     #     queryset = ProjectTask.objects.filter(task_role_id = self.request.user)
#     #     serializer = ProjectTaskupdateSerializer(queryset, many=True)
#     #     serializer.is_valid(raise_exception=True)
#     #     serializer.save()


#     #     return serializer.data

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         # not permitted check
#         if instance.task_role != self.request.user:
#             print(instance.task_role)
#             print(self.request.user)
#             raise exceptions.PermissionDenied()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)





class IsUser(permissions.BasePermission):
    def has_permission(self, request,view):
        print("Hit IsUser")
        # print( ProjectTask.objects.filter(task_role = request.user))
        return ProjectTask.objects.filter(task_role = request.user)


class ProjectTaskView(viewsets.ModelViewSet):

    queryset = ProjectTask.objects.all()
    serializer_class = ProjectTaskSerializer
    filter_fields  = ["projectid"]
    permission_classes = [IsUser,]

