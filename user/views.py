from django.contrib import admin
from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .serializers import UserSerializer
from .models import User
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny #, IsAuthenticated,
from rest_framework.decorators import action
from book.models import Book
from book.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
#from place.models import RackItem
#from place.serializers import RackSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset =  User.objects.all()
    #permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes] 
    
    @action(detail=True)
    def my_book(self, request,  pk=None):
        queryset = Book.objects.filter( owner__id=pk )
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True)
    def by_author(self, request,  pk=None):
        queryset = Book.objects.filter( author__id=pk )
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True)
    def by_rack(self, request,  pk=None):
        queryset = Book.objects.filter( rack_item=pk )
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
      
    #@action(detail=True)
    #def my_book_on_rack(self, request,  pk=None):
    #    queryset = RackItem.objects.filter(
    #        book__owner__id = pk
    #    ).values_list("book__id", flat=True)
    #    #print(queryset)
    #    #print(pk)
    #    books = Book.objects.filter(
    #        id__in=queryset
    #    )
    #    serializer = BookSerializer(books, many=True)
    #    return Response(serializer.data, status=status.HTTP_200_OK) 
    
    ##@action(detail=True)
    #def by_authors(self, request,  pk=None):
    #    queryset = RackItem.objects.filter(
    #        book__owner__id = pk
    #    ).values_list("book__id", flat=True)
    #    #print(queryset)
    #    #print(pk)
    #    books = Book.objects.filter(
    #        id__in=queryset
    #    )
    #    serializer = BookSerializer(books, many=True)
    #    return Response(serializer.data, status=status.HTTP_200_OK) 
    
#class AuthorViewset(viewsets.ModelViewSet):

    
    
    
    
    
    
    
    
    