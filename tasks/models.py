from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=30)
    description=models.TextField()
    dueDate=models.DateTimeField(null=True,blank=True)
    isComplete=models.BooleanField()
    createdAt=models.DateTimeField(default=timezone.localtime)
    updatedAt=models.DateTimeField(default=timezone.localtime)
    PRIORITY_CHOICE={
    "LOW":"low",
    "MEDIUM":"medium",
    "HIGH":"high"
    }
    priority=models.CharField(max_length=6,choices=PRIORITY_CHOICE)
    taskImage=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    # description,dueDate,priority,isComplete,createdAt,updatedAt,

    
