from django.db import models

# Create your models here.



class FeedBack(models.Model):
    
    userid = models.ForeignKey("user.User",null=False,blank=False,on_delete=models.CASCADE)
    pollsid = models.ForeignKey("polls.Poll",null=False,blank=False,on_delete=models.DO_NOTHING)
    feedback_text = models.TextField(null=True,blank=True)

    class Meta:
        unique_together = ("userid", "pollsid")
        db_table = "feedback"
