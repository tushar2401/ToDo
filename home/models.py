from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)  
    taskTitle = models.CharField( max_length=30)
    taskDesc = models.TextField()
    assignto = models.CharField(max_length=20,null=True)

    #def __str__(self):
        #return self.taskTitle,self.user.username

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    contact_no = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username
    

    