from email.mime import image
from telnetlib import Telnet
from django.db import models
from django.core.validators import FileExtensionValidator
import base64

# Create your models here.
from base64 import b64encode
# from base64.fields import Base64ImageField
# from drf_extra_fields.fields import Base64ImageField

from django.utils.translation import gettext_lazy as _




class VideoModel(models.Model):
     

    video_name  = models.CharField(max_length=200, null=True,blank=True)
    video_desc = models.CharField(max_length=200, null=True,blank=True)
    video_name_m = models.CharField(max_length=200, null=True,blank=True)
    video_desc_m  = models.CharField(max_length=200, null=True,blank=True)
    video_link = models.FileField(null=True,blank=True)
    viewed  = models.IntegerField(null=True,blank=True,default=0)
    liked  =models.IntegerField(null=True,blank=True,default=0)
    title  = models.BinaryField(null=True,blank=True)
    title2  = models.TextField(null=True,blank=True,help_text=_('title2'), verbose_name=_('title2'))
#    entity_id  
#    created_by 
#    updated 
#    updated_by  



    def __str__(self):
        return self.video_name

    class Meta:
        db_table = "video"








class FeedModel(models.Model):

    feed_title = models.TextField(null=True,blank=True)
    feed_discription = models.TextField(null=True,blank=True)
    feed_image = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['jpeg','jpg','png'])],null=True,blank=True)


    def save(self, *args, **kwargs):

        # area_name_encode = self.area_name
        # b = base64.b64encode(bytes(str(area_name_encode),"utf_8"))
        # self.area_name = b.decode("utf-8")  
        


        feed_title_encode = self.feed_title
        feed_discription_encode = self.feed_discription

        self.area_name = base64.b64encode(bytes(str(feed_title_encode),"utf_8"))
        self.feed_discription = base64.b64encode(bytes(str(feed_discription_encode),"utf_8"))






        super(FeedModel, self).save(*args, **kwargs)

    class Meta:
        db_table = "feeds"



#---------------------------------------

class FeedComments(models.Model):
    feed_id = models.ForeignKey(FeedModel,null=True,blank=True,on_delete=models.CASCADE,related_name="feedcomment")
    user_id = models.ForeignKey("user.User",null=True,blank=True,on_delete=models.CASCADE, related_name="commentuser")
    user_name  = models.TextField(null=True,blank=True)
    feed_comment  = models.TextField(null=True,blank=True)

#-------------------------------- Yes ------------------------- 

class FeedLikeModel(models.Model):
    feed_ids = models.ForeignKey(FeedModel,null=True,blank=True,on_delete=models.CASCADE,related_name="feedlike")
    user_id = models.ForeignKey("user.User",null=True,blank=True,on_delete=models.CASCADE)
    feed_like  = models.BooleanField(null=True,blank=True,default=False)

    class Meta:
        unique_together = ("feed_ids", "user_id")











