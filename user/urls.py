from . import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('register/',views.RegisterView.as_view(),name="register"),
]