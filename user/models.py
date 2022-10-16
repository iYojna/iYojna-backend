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
        ('Below 10th', 'Below 10th'),
        ('10th', '10th'),
        ('12th', '12th'),
        ('Graduate', 'Graduate'),
        ('Post Graduate', 'Post Graduate'),
        ('Doctorate', 'Doctorate'),
    )

    ED_MAP = {
        'Below 10th': 0,
        '10th': 1,
        '12th': 2,
        'Graduate': 3,
        'Post Graduate': 4,
        'Doctorate': 5,
    }

    first_name = models.CharField(max_length=255, null=True, blank=False)
    last_name = models.CharField(max_length=255, null=True, blank=False)
    otp = models.CharField(max_length=100, null=True, blank=False)
    dob = models.DateField(default=datetime.date.today)
    gender = models.CharField(max_length=9, choices=TYPE, default="Female")
    income = models.IntegerField(blank=True, null=True)
    marital_status = models.CharField(max_length=9, choices=STATUS, default="Unmarried")
    caste = models.CharField(max_length=255, blank=True, null=True)
    education = models.CharField(max_length=20, choices=EDU_TYPES, default="Below 10th")
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

    @property
    def educational_qualifications(self):
        return self.ED_MAP[self.education]

    @property
    def age(self):
        return int((datetime.date.today() - self.dob).days / 365.25)
