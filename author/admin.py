from django.contrib import admin
from .models import *


class ListAuthor(admin.ModelAdmin):
    search_fields = ['name']

# Register your models here.
admin.site.register(Author, ListAuthor)