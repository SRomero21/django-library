from django.db import models

# Create your models here.
class Author(models.Model):
    name= models.CharField(max_length=200, blank=False, null=False, default="")
    description= models.TextField(max_length=200, blank=False, null=False, default="")
    
    def __str__(self):
        return self.name

# class RackNum(models.Model):
#     name= models.CharField(max_length=200, blank=False, null=False, default="")
#     description= models.TextField(max_length=200, blank=False, null=False, default="")
    
#     def __str__(self):
#         return self.name