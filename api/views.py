from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, MeetingSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Meeting 
import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
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


#for google auth


class GoogleLogin(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        token_id = request.data.get("token")

        if not token_id:
            return Response({"error": "Token not provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Verify token with Google
        google_url = f"https://oauth2.googleapis.com/tokeninfo?id_token={token_id}"
        response = requests.get(google_url)

        if response.status_code != 200:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

        data = response.json()

        email = data.get("email")
        first_name = data.get("given_name", "")
        last_name = data.get("family_name", "")

        if not email:
            return Response({"error": "Email not found in token"}, status=status.HTTP_400_BAD_REQUEST)

        # Get or create user
        user, created = User.objects.get_or_create(email=email, defaults={
            "username": email,
            "first_name": first_name,
            "last_name": last_name,
        })

        # Issue JWT tokens
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })

