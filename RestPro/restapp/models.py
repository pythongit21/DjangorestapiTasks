from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=250)
    task_desc = models.CharField(max_length=250)
    date_add = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', default='images/None/Noimage.jpg')