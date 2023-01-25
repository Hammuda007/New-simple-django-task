from django.db import models
from taggit.managers import TaggableManager
# Create your models here.


class Cours(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=100)
    suptitle=models.CharField(max_length=100)
    Description=models.TextField(max_length=10000)
    Requirment=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='Courses/', default='default.png')
    tags = TaggableManager()
   

    def __str__(self):
      return self.title