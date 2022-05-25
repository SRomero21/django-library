from .models import Author
from rest_framework import serializers
#from author.serializers import AuthorSerializer

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
