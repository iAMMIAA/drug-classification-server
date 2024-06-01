from rest_framework import serializers
from .models import Informationdrug, UrlImgUser

class Informationdrug_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Informationdrug
        fields = '__all__'

class UrlImgUser_Serializer(serializers.ModelSerializer):
    class Meta:
        model = UrlImgUser
        fields = '__all__'