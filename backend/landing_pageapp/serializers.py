from rest_framework import serializers
from .models import (
    NewsandEvents, QuickAccess, About, Leadership, Banner, GlanceStat,
    Campus_gallery, Excellence_in_Education, Campus_life, Companies_hiring, VirtualExperience
)

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class QuickAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuickAccess
        fields = '__all__'

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class LeadershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leadership
        fields = '__all__'

class GlanceStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlanceStat
        fields = '__all__'

class CampusGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus_gallery
        fields = '__all__'

class ExcellenceInEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excellence_in_Education
        fields = '__all__'

class CampusLifeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus_life
        fields = '__all__'

class CompaniesHiringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies_hiring
        fields = '__all__'

class VirtualExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualExperience
        fields = '__all__'

class NewsAndEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsandEvents
        fields = '__all__'
