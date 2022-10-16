from typing import OrderedDict
from django.shortcuts import render
from rest_framework import views
from butter_knife.main import get_schemes, get_scheme_data
from rest_framework.response import Response
from rest_framework import status
from utils.db.utils import update_schemes, is_eligible
from utils.get_tags.get_tags import getTags

from .models import EnglishSchemeModel, GujSchemeModel
from .serializers import EnglishSchemeModelSerializer, GujSchemeModelSerializer

# Create your views here.

ls = ["agricultre", "cooperation", "education", "civil", "home", "administration", "mines", "labour", "tribal", "urban",
      "women", "child", "ITC", "BSF", "NTPC", "Toy", "innovation", "collector", "DDO", "municipal", "science",
      "technology"]


def get_model_by_request(request):
    if request.GET.get("lang") == "gu":
        return GujSchemeModel
    else:
        return EnglishSchemeModel


def get_serializer_by_request(request):
    if request.GET.get("lang") == "gu":
        return GujSchemeModelSerializer
    else:
        return EnglishSchemeModelSerializer


class UpdateSchemeView(views.APIView):
    def get(self, request):
        update_schemes()
        return Response({"message": "Updated Schemes"}, status=status.HTTP_200_OK)


class SchemesView(views.APIView):
    queryset = EnglishSchemeModel.objects.all()

    def get(self, request):
        queryset = get_model_by_request(request).objects.all()
        serializer = get_serializer_by_request(request)(queryset, many=True)
        return Response(serializer.data)


class UpdateSchemeTagsView(views.APIView):
    def get(self, request):
        schemes = get_model_by_request(request).objects.all()
        for x in schemes:
            name = x.name
            desc = x.desc

            ls = getTags(name)
            if desc:
                ps = getTags(desc)
            else:
                ps = []

            js = ls + ps
            x.tags = str(js)
            x.save()

            print(x.name)

        return Response({"message": "Updated Tags"}, status=status.HTTP_200_OK)


class RetTagSchemeView(views.APIView):
    def get(self, request):
        tag = request.query_params.get("tag", None)
        if tag is None:
            return Response({"message": "Please provide a tag"}, status=status.HTTP_400_BAD_REQUEST)
        tag = request.query_params.get('tag', None).lower()
        schemes = get_model_by_request(request).objects.all()
        resp = {}
        final_resp = {}
        for x in schemes:
            strls = x.tags
            strls = strls.split("'")
            # print(strls)
            for y in strls:
                if y == str(tag):
                    x_scheme = get_model_by_request(request).objects.get(id=x.id)
                    x_scheme_data = get_serializer_by_request(request)(x_scheme).data
                    resp[x.id] = x_scheme_data

        for scheme_id, scheme_data in resp.items():
            if is_eligible(scheme_data, request.user):
                scheme_data["eligible"] = True
            else:
                scheme_data["eligible"] = False
            final_resp[scheme_id] = scheme_data

        return Response(final_resp, status=status.HTTP_200_OK)


class RetQuerySchemeView(views.APIView):
    def get(self, request):
        query = request.query_params.get('query', None)
        if query is None:
            return Response({"message": "Please provide a query"}, status=status.HTTP_400_BAD_REQUEST)
        query = query.lower().split(",")
        schemes = get_model_by_request(request).objects.all()
        resp = OrderedDict()

        for x in schemes:
            strls = x.tags
            strls = strls.split("'")
            strls = list(map(str.lower, strls))

            num = 0
            for quer in query:
                if quer in strls:
                    num += 1
            if num != 0:
                x_scheme_data = get_serializer_by_request(request)(x).data
                if resp.get(num / len(query)):
                    resp[num / len(query)].append(x_scheme_data)
                else:
                    resp[num / len(query)] = [x_scheme_data]

        return Response(resp, status=status.HTTP_200_OK)
