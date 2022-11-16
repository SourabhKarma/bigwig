from django.db import models

# Create your models here.




class GroupModel(models.Model):
    group_members = models.ManyToManyField("user.User")
    group_name = models.CharField(max_length=100,null=True,blank=True)




class GroupChatModel(models.Model):

    group_member = models.ForeignKey("user.User",on_delete=models.DO_NOTHING,null=True,blank=True)
    group_id = models.ForeignKey(GroupModel,on_delete=models.DO_NOTHING,null=True,blank=True,related_name="group_message")
    group_member_text = models.CharField(null=True,blank=True,max_length=200)
    text_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-text_time']



class Message(models.Model):
    # context = models.TextField(null=True,blank=True,)
    sender = models.TextField(null=True,blank=True,)
    message = models.TextField(null=True,blank=True,)
    timestamp = models.DateTimeField(auto_now=True)
    # group = models.TextField(null=True,blank=True,)
    time = models.DateTimeField(auto_now=True)


    groupid = models.ForeignKey(GroupModel , null=True,blank=True,on_delete=models.DO_NOTHING)
    userid =  models.ForeignKey("user.User",on_delete=models.DO_NOTHING,null=True,blank=True)
    groupInt= models.IntegerField(null=True,blank=True,)

    def last_message(self):
        return Message.objects.order_by('time').all()[:20]

    class Meta:
        ordering = ['time']


    