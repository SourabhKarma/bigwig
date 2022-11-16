from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.files import File  # you need this somewhere
import urllib
import os
# Create your models here.


from django.db import models
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from urllib import request
import base64



class StoriesModel(models.Model):

    stories_title = models.TextField(null=True,blank=True)
    stories_discription = models.TextField(null=True,blank=True)
    stories_start = models.DateField(null=True,blank=True)
    stories_end = models.DateField(null=True,blank=True)
    view_count = models.IntegerField(default=0)
    stories_file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['jpeg','jpg','png','mp4','mov','mkv','avi'])],null=True,blank=True)
    stories_files = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['jpeg','jpg','png','mp4','mov','mkv','avi'])],default='giphy.gif')

    url = models.CharField(max_length=255,null=True,blank=True)
    
    # def cache(self):
    #     """Store image locally if we have a URL"""

    #     if self.url and not self.stories_file:
    #         result = urllib.urlretrieve(self.url)
    #         print(self.url)
    #         print(result)
    #         self.stories_file.save(
    #                 os.path.basename(self.url),
    #                 File(open(result[0], 'rb'))
    #                 )
    #         self.save()


    def get_remote_image(self):
        if self.url and not self.stories_files:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.url).read())
            img_temp.flush()
            self.stories_files.save(f"image_{self.pk}", File(img_temp))
        self.save()




class StoriesComment(models.Model):

    stories_id = models.ForeignKey(StoriesModel,null=True,blank=True,on_delete=models.CASCADE,related_name="storiescomment")
    user_id = models.ForeignKey("user.User",null=True,blank=True,on_delete=models.CASCADE, related_name="storiesuser")
    user_name  = models.TextField(null=True,blank=True)
    stories_comment  = models.TextField(null=True,blank=True)



class StoriesLikeModel(models.Model):
    stories_ids = models.ForeignKey(StoriesModel,null=True,blank=True,on_delete=models.CASCADE,related_name="storieslike")
    user_id = models.ForeignKey("user.User",null=True,blank=True,on_delete=models.CASCADE,related_name="storieslikeuser")
    stories_like  = models.BooleanField(null=True,blank=True,default=False)

    class Meta:
        unique_together = ("stories_ids", "user_id")



class Item(models.Model):
    image_file = models.FileField(blank=True,default='1.jpg')
    image_url = models.URLField()
    image_urls = models.URLField()

    image_name = models.CharField(max_length=200,null=True,blank=True)



    # def get_remote_image(self,*args, **kwargs):
    #     if self.image_url and not self.image_file:
    #         result = request.urlretrieve(self.image_url)
    #         self.image_file.save(
    #                 os.path.basename(self.image_url),
    #                 File(open(result[0], 'rb'))
    #                 )
    #         self.save(*args, **kwargs)






    # def save(self, *args, **kwargs):
    #     if self.image_url and not self.image_file:
    #         img_temp = NamedTemporaryFile(delete=True)
    #         img_temp.write(urlopen(self.image_url).read())
    #         img_temp.flush()
    #         self.image_file.save(f"image_{self.pk}", File(img_temp))
    #     super(Item, self).save(*args, **kwargs)


    def save(self, *args, **kwargs):
        if self.image_url and  self.image_file == '1.jpg':
            result = request.urlretrieve(self.image_url)
            self.image_file.save(
                    os.path.basename(self.image_url),
                    File(open(result[0], 'rb')))
        super(Item, self).save(*args, **kwargs)


        image_name_encode = self.image_name
        image_name_encode_str = base64.b64encode(bytes(str(image_name_encode),"utf_8"))
        self.image_name = image_name_encode_str.decode("utf-8")

