from . import views
from django.urls import path



urlpatterns = [
    path('update-schemes/',views.UpdateSchemeView.as_view(),name="update-schemes"),
    path('get-schemes/',views.SchemesView.as_view(),name="get-schemes"),
    path('update-tags/', views.UpdateSchemeTagsView.as_view(), name="update-tags"),
    path('retrieve-schemes/', views.RetTagSchemeView.as_view(), name = "retrieve-schemes"),
    path('retrieve-query-schemes/', views.RetQuerySchemeView.as_view(), name = "retrieve-schemes"),
]