from django.db import models



class Task(models.Model):
 task = models.CharField(max_length=100,unique=True)
 completed = models.BooleanField(default=True)
 description = models.TextField()
 created_date =models.DateField(auto_now=True)

 def __str__(self):
  return self.task