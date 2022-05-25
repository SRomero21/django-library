from django.contrib import admin
from .models import User
#, CustomUserManager
# Register your models here.
class ListUser(admin.ModelAdmin):
    search_fields = ['email']

#admin.site.register(User) 
admin.site.register(User, ListUser) 


