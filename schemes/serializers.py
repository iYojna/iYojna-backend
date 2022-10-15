from rest_framework import serializers
from .models import SchemeModel

class PersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model= SchemeModel
        fields = "__all__"