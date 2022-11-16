import base64
from encodings import utf_8
from django.db import models
from pytz import utc

# Create your models here.

class area(models.Model):
    area_name = models.CharField(max_length=255,null=True,blank=True)
    created_by = models.CharField(max_length=255,null=True,blank=True)
    updated_by = models.CharField(max_length=255,null=True,blank=True)
    create_time = models.DateTimeField(auto_created=True,auto_now=True,blank=True,null=True)
    # admin  = models.ForeignKey("user.User",null=True,blank=True,on_delete=models.DO_NOTHING)


    def save(self, *args, **kwargs):
        # a = str(self.area_name).encode('ascii')
        # area_name_encode = base64.b64encode(bytes(str(a),"utf_8"))
        # self.area_name = area_name_encode.decode('ascii')

        # area_name_encode = self.area_name
        # b = base64.b64encode(bytes(str(area_name_encode),"utf_8"))
        # self.area_name = b.decode("utf-8")  
        


        area_name_encode = self.area_name
        self.area_name = base64.b64encode(bytes(str(area_name_encode),"utf_8"))




        # self.area_name = base64.b64encode(str(area_name_encode))

        super(area, self).save(*args, **kwargs)

    def __str__(self):
        a = self.area_name
        b = a.decode("ascii")

        return base64.b64decode(a, 'utf-8')
        # area_name  = str(self.area_name)    
        # return  base64.urlsafe_b64decode(area_name).decode("utf-8","ignore")


    class Meta:
        db_table = "area"



class ward(models.Model):
    area_id = models.ForeignKey("area",null=True,blank=True,on_delete=models.CASCADE)
    ward_name = models.CharField(max_length=255, null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)


    def __str__(self):
        return self.ward_name

    class Meta:
        db_table = "ward"
