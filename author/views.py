from django.shortcuts import render
from rest_framework import viewsets
from .models import Author
from .serializers import AuthorSerializer


# Create your views here.
class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


#from .permissions import IsOwnerOrReadOnlyBook
#from rest_framework.permissions import  IsAdminUser
#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework import filters 
