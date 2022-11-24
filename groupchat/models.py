from django.db import models
import base64
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

    def save(self, *args, **kwargs):
        # event_name_encode = self.event_name
        # event_name_encode_str = base64.b64encode(bytes(str(event_name_encode),"utf_8"))
        # self.event_name = event_name_encode_str.decode("utf-8")

        # event_name_encode = self.message
        # event_name_encode_str = base64.b64encode(bytes(str(self.message),"utf_8"))
        self.message = base64.b64encode(bytes(str(self.message),"utf_8")).decode("utf-8")
        self

        super(Message, self).save(*args,**kwargs)








    # def last_message(self):
    #     return Message.objects.order_by('time').all()[:20]

    class Meta:
        ordering = ['time']


    