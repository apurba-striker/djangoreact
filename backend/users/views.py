from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import UserResgisterSerializer, UserLoginSerializer, UserProfileSerializer, UserUpdateSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = UserResgisterSerializer
    permission_classes = [AllowAny]
    
    def post(self,request):
        serializer = UserLoginSerializer(data=request.data)
        user = authenticate(username=serializer.validate_data['email'],password=serializer.validate_data['password'])
        if user is None:
            return Response({"error":"Invalid Credentials"},status = status.HTTP_401_UNAUTHORIZED)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh':str(refresh),
            'access':str(refresh.access_token),
        },status=status.HTTP_200_OK)
        
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]
    def get_object(self):
        return self.request.user
    
class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [AllowAny]
    def get_object(self):
        return self.request.user         


# Create your views here.
