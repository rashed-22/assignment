from django.db import models

# Create your models here.

class TaskModel(models.Model):
    id = models.IntegerField(primary_key=True)
    taskTitle = models.CharField(max_length=20)
    taskDescription = models.TextField(max_length=50)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"ID: {self.id} Task: {self.taskTitle} Desc: {self.taskDescription} Status: {self.is_completed}"
    
        