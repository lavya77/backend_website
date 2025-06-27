from rest_framework import serializers
from .models import BookingHeroSection, UserRole, BookingFacility

class BookingHeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingHeroSection
        fields = '__all__'

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'

class BookingFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingFacility
        fields = '__all__'
