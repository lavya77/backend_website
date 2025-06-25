from rest_framework import serializers
from .models import (
    CampusHero, VirtualTour, key_highlights, campus_life_stats,
    HostelLifeSection, Hostel, HostelDetail, Amenity,
    Student_club, Activity, Achievement,
    Library_gbu, LibraryStat, LibraryFacility, LibraryStats,
    SportsFacility,  FacilityFeature,
    FoodCourtCategory, FoodCourtItem, FoodOutlet, Tag, 
    EcoCampusStat, EcoInitiative_stats, GreenInitiative, ImpactStat,
    StudentTestimonial, Meditation_herosection, MeditationSession,
    MeditationBenefit, MeditationTechnique,
    Organization, join_nssandncc
)

class CampusHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampusHero
        fields = '__all__'

class VirtualTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualTour
        fields = '__all__'

class KeyHighlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = key_highlights
        fields = '__all__'

class CampusLifeStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = campus_life_stats
        fields = '__all__'

class HostelLifeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostelLifeSection
        fields = '__all__'

class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = '__all__'

class HostelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostelDetail
        fields = '__all__'

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'

class StudentClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_club
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

class LibraryGBUSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library_gbu
        fields = '__all__'

class LibraryStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryStat
        fields = '__all__'

class LibraryFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryFacility
        fields = '__all__'

class LibraryStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryStats
        fields = '__all__'

class SportsFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsFacility
        fields = '__all__'

class FacilityFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityFeature
        fields = '__all__'

class FoodCourtCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCourtCategory
        fields = '__all__'

class FoodCourtItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCourtItem
        fields = '__all__'

class FoodOutletSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodOutlet
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class EcoCampusStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcoCampusStat
        fields = '__all__'

class EcoInitiativeStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcoInitiative_stats
        fields = '__all__'

class GreenInitiativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GreenInitiative
        fields = '__all__'

class ImpactStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpactStat
        fields = '__all__'

class StudentTestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTestimonial
        fields = '__all__'

class MeditationHeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meditation_herosection
        fields = '__all__'

class MeditationSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeditationSession
        fields = '__all__'

class MeditationBenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeditationBenefit
        fields = '__all__'

class MeditationTechniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeditationTechnique
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class JoinNSSAndNCCSerializer(serializers.ModelSerializer):
    class Meta:
        model = join_nssandncc
        fields = '__all__'
