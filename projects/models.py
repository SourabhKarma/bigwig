from django.db import models

# Create your models here.


active = 0
inactive = 1
completed = 2
cancelled = 3


PROJECT_CHOICES = [(active,"ACTIVE"),(inactive,"INACTIVE"),(completed,"COMPLETED"),(cancelled,"CANCELLED")]

active = 0
inactive = 1
completed = 2


PROJECT_TASK_CHOICES = [(active,"ACTIVE"),(inactive,"INACTIVE"),(completed,"COMPLETED")]








class ProjectModel(models.Model):
       project_name  = models.CharField(max_length=200,null=True,blank=True) 
       project_description  = models.TextField(null=True,blank=True)
       project_file = models.FileField(null=True,blank=True)
       start_date  = models.DateTimeField(null=True,blank=True)
       end_date  = models.DateTimeField(null=True,blank=True)
       project_leader = models.ForeignKey("user.User",null=True,blank=True,on_delete=models.DO_NOTHING)
       completion  = models.IntegerField(null=True,blank=True,default=0)
       status = models.IntegerField(null=True,blank=True,choices=PROJECT_CHOICES,default=0)
       created  = models.DateTimeField(auto_created=True,auto_now=True)
       created_by = models.ForeignKey("user.User",null=True,blank=True,on_delete=models.DO_NOTHING,related_name="projectowner")
       project_member = models.ManyToManyField("user.User",related_name="project_members")


       def __str__(self):
              return self.project_name




class ProjectInvite(models.Model):
    projectid = models.ForeignKey(ProjectModel,null=True,blank=True,on_delete=models.DO_NOTHING)
    userinvite = models.ForeignKey("user.User",null=True,blank=True,on_delete=models.DO_NOTHING)
    invite_status = models.BooleanField(null=True,blank=True,default=0)
    class Meta:
        unique_together = ("projectid", "invite_status")





class ProjectTask(models.Model):
    projectid = models.ForeignKey(ProjectModel,null=True,blank=True,on_delete=models.DO_NOTHING)
    task_name  = models.CharField(max_length=200,null=True,blank=True)
    task_discription = models.TextField(null=True,blank=True)
    task_status = models.IntegerField(null=True,blank=True,choices=PROJECT_TASK_CHOICES,default=0)
    task_role = models.ForeignKey("user.User",null=True,blank=True,on_delete=models.DO_NOTHING)
