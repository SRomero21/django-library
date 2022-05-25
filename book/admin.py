from django.contrib import admin
from .models import Book
# Register your models here.

#admin.site.register(Book)

class ListBook(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Book, ListBook) 
