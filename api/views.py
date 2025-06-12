from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, MeetingSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Meeting 
# Create your views here.


class MeetingListCreate(generics.ListCreateAPIView):
    serializer_class = MeetingSerializer
    permission_classes = [IsAuthenticated] # Ensure user is authenticated

    def get_queryset(self):
        return Meeting.objects.filter(author=self.request.user)  # Only show user's meetings
    

    def perform_create(self, serializer):
         serializer.save(author=self.request.user)  # Auto-assign user
        
           
        
           


class MeetingDelete(generics.DestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Meeting.objects.filter(author=self.request.user)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]