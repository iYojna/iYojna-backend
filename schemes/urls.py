from . import views
from django.urls import path



urlpatterns = [
    path('get-schemes/',views.SchemeView.as_view(),name="get-schemes"),
]