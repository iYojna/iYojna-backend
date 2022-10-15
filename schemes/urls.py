from . import views
from django.urls import path



urlpatterns = [
    path('update-schemes/',views.UpdateSchemeView.as_view(),name="update-schemes"),
    path('get-schemes/',views.SchemesView.as_view(),name="get-schemes"),
]