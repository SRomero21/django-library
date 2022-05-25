from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password", "first_name",
                  "last_name", "id", "date_joined", "last_login"
                  )
        
        extra_kwargs = {
            "password": {"write_only": True},
            "id": {"read_only": True},
            "date_joined": {"read_only": True},
            "last_login": {"read_only": True},
        }
    
    def create(self, validated_data):
        user = User(
            **validated_data
        )
        user.set_password(validated_data["password"])
        user.save()
        return user