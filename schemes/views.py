from typing import OrderedDict
from django.shortcuts import render
from rest_framework import views
from butter_knife.main import get_schemes, get_scheme_data
from rest_framework.response import Response
from rest_framework import status
from utils.db.utils import update_schemes, is_eligible
from utils.get_tags.get_tags import getTags

from .models import EnglishSchemeModel, GujSchemeModel
from .serializers import EnglishSchemeModelSerializer

# Create your views here.

ls = ["agricultre", "cooperation", "education", "civil", "home", "administration", "mines", "labour", "tribal", "urban",
      "women", "child", "ITC", "BSF", "NTPC", "Toy", "innovation", "collector", "DDO", "municipal", "science",
      "technology"]


class UpdateSchemeView(views.APIView):
    def get(self, request):
        update_schemes()
        return Response({"message": "Updated Schemes"}, status=status.HTTP_200_OK)


class SchemesView(views.APIView):
    queryset = EnglishSchemeModel.objects.all()

    def get(self, request):
        queryset = EnglishSchemeModel.objects.all()
        serializer = EnglishSchemeModelSerializer(queryset, many=True)
        return Response(serializer.data)


class UpdateSchemeTagsView(views.APIView):
    def get(self, request):
        schemes = EnglishSchemeModel.objects.all()
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
        schemes = EnglishSchemeModel.objects.all()
        resp = {}
        final_resp = {}
        for x in schemes:
            strls = x.tags
            strls = strls.split("'")
            # print(strls)
            for y in strls:
                if y == str(tag):
                    x_scheme = EnglishSchemeModel.objects.get(id=x.id)
                    x_scheme_data = EnglishSchemeModelSerializer(x_scheme).data
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
        query = request.query_params.get('query', None).lower()
        query = query.split("&")
        schemes = EnglishSchemeModel.objects.all()
        resp = OrderedDict()

        for quer in query:
            for x in schemes:
                strls = x.tags
                strls = strls.split("'")
                deno = len(strls)
                num = 0
                for y in strls:
                    if y == str(quer):
                        num = num + 1

                if num > 0:
                    percent = (num / deno) * 100
                    x_scheme = EnglishSchemeModel.objects.get(id=x.id)
                    x_scheme_data = EnglishSchemeModelSerializer(x_scheme).data
                    resp[percent] = x_scheme_data

        return Response(resp, status=status.HTTP_200_OK)
