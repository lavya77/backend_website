from rest_framework import serializers
from .models import QuickAccess , Banner , About

class Bannerserializer(serializers.ModelSerializer):
    class Meta:
        model= Banner
        fields='__all__'

class QuickAccessserializer(serializers.ModelSerializer):
    class Meta:
        model = QuickAccess
        fields= '__all__'
class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields='__all__'