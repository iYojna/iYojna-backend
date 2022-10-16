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
        ('Graduate', 3),
        ('Under Graduate', 2),
        ('Schooling', 1),
        ('Not Applicable', 0),
    )

    first_name = models.CharField(max_length=255, null=True, blank=False)
    last_name = models.CharField(max_length=255, null=True, blank=False)
    otp = models.CharField(max_length=100, null=True, blank=False)
    dob = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=9, choices=TYPE, default="Female")
    income = models.IntegerField(blank=True, null=True)
    marital_status = models.CharField(max_length=9, choices=STATUS, default="Unmarried")
    caste = models.CharField(max_length=255, blank=True, null=True)
    educational_qualifications = models.CharField(max_length=15, choices=EDU_TYPES, default="Graduate")
    district = models.CharField(max_length=255, blank=True, null=True)
    phone_no = models.CharField(max_length=15, blank=True)
    tags = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
