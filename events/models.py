from django.db import models
# from location_field.models.plain import PlainLocationField
from django.core.validators import FileExtensionValidator



# Create your models here.
Yes = 0
No = 1
Maybe = 2

EVENT_CHOICES = [(Yes,"YES"),(No,"NO"),(Maybe,"MAYBE")]


class EventModel(models.Model):

  event_name  = models.CharField(max_length=100,null=True,blank=True)
  event_description = models.TextField(null=True,blank=True)
  event_file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['jpeg','jpg','png'])],null=True,blank=True)
  city = models.CharField(max_length=255, null=True,blank=True)
  start_date  = models.DateTimeField(null=True,blank=True)
  end_date = models.DateTimeField(null=True,blank=True)
  event_start_time = models.TimeField(null=True,blank=True)
  created_by = models.ForeignKey("user.User",null=True,blank=True,on_delete=models.DO_NOTHING)
  envent_video = models.URLField(null=True,blank=True)
  event_latitude = models.DecimalField(max_digits=10, decimal_places=8,null=True,blank=True)
  event_longitude = models.DecimalField(max_digits=10, decimal_places=8,null=True,blank=True)



  # intrested_user = models.ManyToManyField("user.User")
  # event_location = PlainLocationField(based_fields=['city'], zoom=7)



#   image = models.ImageField(null = True,blank= True)
#    status enum('OPEN','CLOSED','CANCELLED') NOT NULL,
#   count_yes 
#   count_no
#   count_maybe 






class EventlikeModel(models.Model):

    userid = models.ForeignKey("user.User",null=True,blank=True,on_delete=models.DO_NOTHING)
    eventid = models.ForeignKey(EventModel,null=True,blank=True,on_delete=models.DO_NOTHING)
    event_choice = models.IntegerField(max_length=10,null=True,blank=True,choices=EVENT_CHOICES)
    # event_yes = models.IntegerField(null=True,blank=True,default=0)
    # event_no = models.IntegerField(null=True,blank=True,default=0)
    # event_maybe = models.IntegerField(null=True,blank=True,default=0)
    # event_char  = models.CharField(max_length=100,null=True,blank=True)
    # event_bool = models.BooleanField(null=True,blank=True,default=True) 
    class Meta:
        unique_together = ("userid", "eventid")
