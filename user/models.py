from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager


from rest_framework import request
import os
from django.db import models
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
import base64
from django.core.files.base import ContentFile
import uuid


# Create your models here.
ADMIN = 1
CITIZEN = 2
PROJECT_MEMBER = 3

ROLE_CHOICES = (
    (ADMIN, 'Admin'),
    (CITIZEN, 'Citizen'),
    (PROJECT_MEMBER, 'Project_member')
)






class User(AbstractUser):


    username = None
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6,null=True,blank=True)

    
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name= models.CharField(max_length=255,null=True,blank=True)
    user_photo = models.FileField(null=True,blank=True,default='index.png')
    gender= models.CharField(max_length=255,null=True,blank=True)
    mobile= models.BigIntegerField(null=True,blank=True)
    email= models.EmailField(unique=False,null=True,blank=True)
    dob= models.DateField(null=True,blank=True)
    status= models.BooleanField(null=True,blank=True,default=1)
    entity_id= models.IntegerField(null=True,blank=True)
    role_id =models.IntegerField(null=True,blank=True,choices=ROLE_CHOICES)
    autopwd= models.CharField(max_length=255,null=True,blank=True)
    profession= models.CharField(max_length=255,null=True,blank=True)
    area= models.CharField(max_length=255,null=True,blank=True)
    ward= models.CharField(max_length=255,null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)
    created_by= models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated = models.DateField(null=True,blank=True)
    updated_by = models.CharField(max_length=255,null=True,blank=True)
    # is_active = models.BooleanField(default=False,)
    image_url = models.TextField(null=True,blank=True)
    # image_urls = models.TextField(null=True,blank=True)

    # notification_tokenss = models.CharField(max_length=200,null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


    # def save(self, *args, **kwargs):
    #     if self.image_url and  self.user_photo == 'index.png':
    #         result = base64.b64decode(self.image_url)
    #         self.user_photo.save(
    #                 os.path.basename(self.image_url),
    #                 File(open(result[0], 'rb')))
    #     super(User, self).save(*args, **kwargs)
    

    def save(self, *args, **kwargs):
        if self.image_url and  self.user_photo == 'index.png':
            name = f'{uuid.uuid4()}'+".jpg"
            data = base64.b64decode(self.image_url)
            self.user_photo = ContentFile(data,name)
        super(User, self).save(*args, **kwargs)










    # def __str__(self):
    #     return self.email



    # def has_perm(self, perm, obj=None):
    #     return True

    # def has_module_perms(self, app_label):
    #     return True


