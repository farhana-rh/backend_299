from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Meeting

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ("id", "title", "datetime", "link", "google_drive_folder_id", "author", "email")
        extra_kwargs = {
            "author": {"read_only": True}
        }
    
    # def create(self, validated_data):
    #     return Meeting.objects.create(**validated_data)