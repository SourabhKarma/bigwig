from rest_framework import serializers
from .models import ProjectModel,ProjectTask,ProjectInvite




class ProjectTaskSerializer(serializers.ModelSerializer):
    projectid = serializers.StringRelatedField()
    task_role = serializers.StringRelatedField()
    class Meta:
        model = ProjectTask
        fields = '__all__'


# update


class ProjectTaskupdateSerializer(serializers.ModelSerializer):
    task_status =  serializers.IntegerField()






class ProjectInviteSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectInvite
        fields = '__all__'












class ProjectTaskUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTask
        fields = '__all__'






class ProjectSerializer(serializers.ModelSerializer):
    # alluser  = serializers.SerializerMethodField(read_only = True)
    # created_by   = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = ProjectModel
        fields = '__all__'



