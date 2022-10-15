import random

from django.shortcuts import render
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response

from .mixins import *
from .models import User
from .serializers import RegisterSerializer, LoginSerializer


# Create your views here.
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    
    def get(self,request):
        queryset = User.objects.all()
        serializer = RegisterSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        user=request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        phone_number  =  user_data['phone_no']
        
        otp = random.randint(1000,9999)
        user = User.objects.get(username=user_data['username'])
        
        # message_handle = MessageHandler(phone_number,otp).send_otp_on_phone()
        user.username = user_data['phone_no']
        user.set_password("demopass")
        user.otp= otp
        user.save()
        return Response(user_data, status=status.HTTP_201_CREATED)
    
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class VerifyOTP(views.APIView):
    
    def post(self,request):
        data= request.data
        user = User.objects.get(phone_no=data['phone_no'])
        
        a = user.otp
        b= data['OTP']
        
        if a==b:
           user.is_verified = True
           user.save() 
           return Response({'otp': 'Successfully verified'}, status=status.HTTP_200_OK)
        
        else:
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
