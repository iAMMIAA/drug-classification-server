from rest_framework import serializers
from .models import Informationdrug

class Informationdrug_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Informationdrug
        fields = '__all__'