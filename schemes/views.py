from django.shortcuts import render
from rest_framework import views
from butter_knife.main import get_schemes, get_scheme_data
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

ls = ["agricultre", "cooperation", "education", "civil", "home", "administration", "mines", "labour", "tribal", "urban",
      "women", "child", "ITC", "BSF", "NTPC", "Toy", "innovation", "collector", "DDO", "municipal", "science",
      "technology"]


class SchemeView(views.APIView):

    def get(self, request):
        data = dict()
        schemes = get_schemes()
        test_scheme = list(schemes.values())[0]
        scheme_data = get_scheme_data(test_scheme)
        data["name"] = scheme_data["en"]["name"]
        data["interest_rate"] = scheme_data["en"]["interest_rate"]
        data["income_limit"] = scheme_data["en"]["income_limit"]

        return Response(data, status=status.HTTP_200_OK)

