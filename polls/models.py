from django.db import models

# Create your models here.
# polls   
#     entity_id     
#     poll_text    
#     created  
#     end_date  
#     status   
#     option1    
#     option2    
#     option3    
#     option4    
#     option5    
#     option6    
#     created_by     
#     updated  
#     updated_by     
#     poll_text_m    
#     option1_m    
#     option2_m    
#     option3_m    
#     option4_m    
#     option5_m    
#     option6_m  


# poll_result   
#     poll_id     
#     user_id     
#     option_selected     
#     created   
#     language  


# questions model & user foreign key



# class Choice(models.Model):
#     name = models.CharField(max_length=20)


#     def __str__(self):
#         return self.name




# class PollModel(models.Model):
#     user_id  = models.ForeignKey("user.User",null=True,blank=True,on_delete=models.DO_NOTHING)
#     poll_title = models.TextField(null=True,blank=True)
#     poll_discription = models.TextField(null=True,blank=True)
#     choices = models.ManyToManyField(Choice, related_name='related_polls', blank=True)




class Poll(models.Model):
    question = models.CharField(max_length=100,null=True,blank=True)
    created_by = models.ForeignKey("user.User",null=True,blank=True, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices',null=True,blank=True,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    choice = models.ForeignKey(Choice, related_name='votes',null=False,blank=False, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll,null=True,blank=True, on_delete=models.CASCADE)
    voted_by = models.ForeignKey("user.User",null=False,blank=False, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("poll", "voted_by")
    
    
    # @property
    # def choice_count(self):
    #     return self.choice_set.count










