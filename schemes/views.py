from django.shortcuts import render
from rest_framework import views
from butter_knife.main import get_schemes, get_scheme_data
from rest_framework.response import Response
from rest_framework import status
from utils.db.update_schemes import main

from .models import EnglishSchemeModel, GujSchemeModel

# Create your views here.

ls = ["agricultre", "cooperation", "education", "civil", "home", "administration", "mines", "labour", "tribal", "urban",
      "women", "child", "ITC", "BSF", "NTPC", "Toy", "innovation", "collector", "DDO", "municipal", "science",
      "technology"]


class UpdateSchemeView(views.APIView):
    def get(self, request):
        main()
        return Response({"message": "Updated Schemes"}, status=status.HTTP_200_OK)
    

class SchemesView(views.APIView):
    def get(self, request):
        en_schemes = EnglishSchemeModel.objects.all()
        gu_schemes = GujSchemeModel.objects.all()
        
        return Response({"en": en_schemes, "gu": gu_schemes})
