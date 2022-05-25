from django.db import models
from author.models import Author
from user.models import User
#from rack.models import RackNum
# from place.models import Rack
# Create your models here.


class Book(models.Model):

    BOOKS_CHOICES = [
        ("L", "Libro" ),
        ("R", "Revistas"),
    ]
    FORMAT_CHOICES = [
        ("D", "Digital"),
        ("F", "Libro fisico"),
    ]
    owner= models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length=200, blank=False, null=False, default="")
    subject = models.CharField(max_length=200, blank=False, null=False, default="")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.CharField(choices=BOOKS_CHOICES, max_length=200, default="")
    isbn= models.CharField(max_length=10, blank=False, null=False, default="")
    publisher = models.CharField(max_length=200, blank=False, null=False, default="")
    language = models.CharField(max_length=200, blank=False, null=False)
    format = models.CharField(choices=FORMAT_CHOICES, max_length=100, blank=True, null=True)
    rack_item = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.isbn} | {self.title} | {self.author.name}" 
    
    
    #class Author(models.Model):
    #    id= models.AutoField(primary_key= True)
    #first_name= models.CharField(max_length=200, blank=False, null=False)
    #last_name = models.CharField(max_length=200, blank=False, null=False)
    #country = models.CharField(max_length=200, blank=False, null=False)
    #description = models.TextField(blank=False, null=False) 