from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30,null=False,blank=False)
    last_name = models.CharField(max_length=30,null=True,blank=True)
    phone_number = models.CharField(max_length=13,null=False,blank=False)
    image = models.ImageField(upload_to='',null=True,blank=True)

    def __str__(self):
        return self.user
