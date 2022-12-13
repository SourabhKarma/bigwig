from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions, exceptions, status
from .models import ProjectModel,ProjectTask,ProjectInvite
from .serializer import ProjectSerializer,ProjectTaskSerializer,ProjectTaskupdateSerializer,ProjectInviteSerializer
from .permission import AuthorAllStaffAllButEditOrReadOnly,IsobjectUser,IsOwner
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser,IsAuthenticated,SAFE_METHODS
from django.db.models import Q
# Create your views here.
from user.models import User
superuser_list = User.objects.filter(is_superuser = True)
print(superuser_list)






class ProjectView(viewsets.ModelViewSet):


    queryset = ProjectModel.objects.all()

    serializer_class = ProjectSerializer
    # filter_fields  = ["","",]

# ------------ working--------------

class ProjectTaskView(viewsets.ModelViewSet):

    queryset = ProjectTask.objects.all()
    serializer_class = ProjectTaskSerializer
    filter_fields  = ["projectid"]
    # permission_classes = [IsOwner,IsAuthenticated]

    def list(self, request):
        if (self.request.user in superuser_list):
            queryset = ProjectTask.objects.all()
            if not queryset:
                return JsonResponse({"message":"empty"},status = status.HTTP_400_BAD_REQUEST)
            # queryset = EventlikeModel.objects.filter()

            serializer = ProjectTaskSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            queryset = ProjectTask.objects.filter(Q(task_role_id = self.request.user) | Q())
            if not queryset:
                return JsonResponse({"message":"empty"},status = status.HTTP_400_BAD_REQUEST)
            # queryset = EventlikeModel.objects.filter()

            serializer = ProjectTaskSerializer(queryset, many=True)
            return Response(serializer.data)
    # def update(self):
    #     queryset = ProjectTask.objects.filter(task_role_id = self.request.user)
    #     serializer = ProjectTaskupdateSerializer(queryset, many=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()


    #     return serializer.data

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # not permitted check
        if instance.task_role != self.request.user:
            print(instance.task_role)
            print(self.request.user)
            raise exceptions.PermissionDenied()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)





class IsUser(permissions.BasePermission):
    def has_permission(self, request,view):
        print("Hit IsUser")
        superuser_list = User.objects.filter(is_superuser = True)
        if (request.user in superuser_list):
            return ProjectTask.objects.all()
        # print( ProjectTask.objects.filter(task_role = request.user))
        # return ProjectTask.objects.filter(task_role = request.user)


# class ProjectTaskView(viewsets.ModelViewSet):

#     queryset = ProjectTask.objects.all()
#     serializer_class = ProjectTaskSerializer
#     filter_fields  = ["projectid"]
#     permission_classes = [IsUser,]


class ProjectInviteView(viewsets.ModelViewSet):
  
    queryset = ProjectInvite.objects.all()

    serializer_class = ProjectInviteSerializer







# ----------------------- project accept S ------------------

from rest_framework.views import APIView
from django.conf import settings

from .serializer import ProjectAcceptSerialzer
import jwt

class ProjectAddView(APIView):
    permission_classes = (IsAuthenticated,)


    def post(self, request):
        serializer = ProjectAcceptSerialzer
        data  =  request.data
        projectlist = list(ProjectModel.objects.filter(id = data["projectid"]).values_list('project_member',flat =True ))
        print(projectlist)



        # auth_data = request.META["HTTP_AUTHORIZATION"]
        # token = str.replace(str(auth_data), 'Bearer ', '')
        # token_user_id= jwt.decode(token ,settings.SECRET_KEY,algorithms='HS256')
        # print(token_user_id["user_id"])

        # if int(data["userid"]) in grouplist and token_user_id["user_id"] == int(data["userid"]):
        if data["userid"] in projectlist:


            projectlist.append(data["userid"])
            print(projectlist)

            group = ProjectModel.objects.filter(id = data["projectid"])
            print(group)
            group = group.first()
            group.project_member.set(projectlist)

        else:

            return JsonResponse({"message":"user not added in project"},status=status.HTTP_400_BAD_REQUEST)


        # group = GroupModel.objects.filter(id = data["groupid"])
        # print(group)
        # group = group.first()
        # print(group.group_members.set(grouplist))


        return JsonResponse({"message":"user removed from group"}) 



# ------------------------- project accept E -----------------