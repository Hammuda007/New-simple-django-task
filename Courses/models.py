from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
# Create your models here.


class Cours(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=100)
    suptitle=models.CharField(max_length=100)
    Description=models.TextField(max_length=10000)
    Requirment=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='Courses/', default='default.png')
    author=models.ForeignKey(User,related_name='post_author',on_delete=models.CASCADE)
    tags = TaggableManager()
   

    def __str__(self):
      return self.title