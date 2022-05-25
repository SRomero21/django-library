from .models import Book
from rest_framework import serializers
from user.serializers import UserSerializer

class BookSerializer(serializers.ModelSerializer):
    book = serializers.CharField(source="get_book_display")
    format = serializers.CharField(source="get_format_display")
    owner = UserSerializer()
    class Meta:
        model = Book
        fields = '__all__'
        depth = 1
        #fields = ["title", "id"]
        #fields = ["title"]
        
class UserSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Book
        fields = "__all__" 
