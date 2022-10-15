from rest_framework import serializers
from .models import EnglishSchemeModel, GujSchemeModel


class EnglishSchemeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnglishSchemeModel
        fields = "__all__"


class GujSchemeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GujSchemeModel
        fields = "__all__"
