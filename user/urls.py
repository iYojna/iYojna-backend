from . import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.LoginAPIView.as_view(), name="login"),
    path('verify-otp/', views.VerifyOTP.as_view(), name='token_refresh'),
    path('verifylogin-otp/', views.VerifyLoginOTP.as_view(), name='token_refresh'),
    path('get-tags/', views.RetUserTags.as_view(), name="get-tags"),
]
