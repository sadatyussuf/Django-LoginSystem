from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProfileModel(models.Model):
    username = models.CharField(max_length=100)
    desc = models.TextField(max_length=100)
    thumb = models.ImageField(upload_to='thumbnail',null=True, blank=True,default='')
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    # user =  models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.username