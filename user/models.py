# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
import datetime


# Create your models here.

class User(AbstractUser):
    
    TYPE = (
        ('Female', 'Female'),
        ('Male', 'Male'),
    )
    
    STATUS = (
        ('Unmarried', 'Unmarried'),
        ('Married', 'Married'),
        ('Widow', 'Widow'),
    )
    
    EDU_TYPES = (
        ('Graduate', 'Graduate'),
        ('Not Applicable', 'Uneducated'),
        ('Under Graduate', 'Under Graduate'),
        ('Schooling', 'In School'),
    )
    
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=255, null=True, blank= False)
    last_name = models.CharField(max_length=255, null=True, blank= False)
    otp = models.CharField(max_length=100, null= True, blank= False)
    dob = models.DateField(default=datetime.date.today)
    gender = models.CharField(max_length=9,choices=TYPE,default="Female")
    income = models.IntegerField(blank=True, null=True)
    marital_status = models.CharField(max_length=9,choices=STATUS,default="Unmarried")
    caste = models.CharField(max_length=255, blank=True, null=True)
    educational_qualifications = models.CharField(max_length=15,choices= EDU_TYPES,default="Graduate")
    district = models.CharField(max_length=255, blank=True, null=True)
    phone_no = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return self.username

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }
