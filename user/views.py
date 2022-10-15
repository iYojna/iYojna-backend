import random

from django.shortcuts import render
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response

from .mixins import *
from .models import User
from .serializers import RegisterSerializer


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
        user_name = user_data['email']
        user_name = user_name.split("@")
        
        otp = random.randint(1000,9999)
        user = User.objects.get(email=user_data['email'])
        
        message_handle = MessageHandler(phone_number,otp).send_otp_on_phone()
        user.username= user_name[0]
        user.password = "demopass"
        user.otp= otp
        user.save()
        return Response(user_data, status=status.HTTP_201_CREATED)
