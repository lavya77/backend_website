from rest_framework import serializers
from .models import contact_herosection, Contact


class ContactHeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact_herosection
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    initials = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = [
            'id', 'name', 'title', 'email', 'phone',
            'office', 'location', 'image', 'category',
            'is_active', 'created_at', 'updated_at', 'initials'
        ]

    def get_initials(self, obj):
        return obj.get_initials()
