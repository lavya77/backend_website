from rest_framework import serializers
from .models import *

class HeroSectionAboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSectionAboutUs
        fields = '__all__'

class Aboutus_StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aboutus_Stats
        fields = '__all__'

class AboutusGBUSerializer(serializers.ModelSerializer):
    class Meta:
        model = aboutus_gbu
        fields = '__all__'

class AboutUsCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = about_us_cards
        fields = '__all__'

class GovernanceOrganizationalHighlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Governance_organizatonal_highlights
        fields = '__all__'

class AcademicSchoolProgramsStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic_school_programs_stats
        fields = '__all__'

class FacilitiesInfrastructureHighlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = facilities_infrastructure_highlights
        fields = '__all__'

class HostelResedentialLifeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel_resedential_life
        fields = '__all__'

class WMeditationEllnessFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = WMeditation_ellness_Feature
        fields = '__all__'

class MeditationWellnesCenterSerializer(serializers.ModelSerializer):
    features = WMeditationEllnessFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = Meditation_wellnes_center
        fields = '__all__'

class GreenEcoFriendlyCampusHighlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Green_eco_friendly_campus_highlights
        fields = '__all__'

class SportsReactionFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = sports_reaction_features
        fields = '__all__'

class SportsReactionHighlightsSerializer(serializers.ModelSerializer):
    feature = SportsReactionFeaturesSerializer(many=True, read_only=True)

    class Meta:
        model = Sports_Reaction_highlights
        fields = '__all__'

class ResearchInnovationHighlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research_innovation_highlights
        fields = '__all__'

class StudentLifeCommunityHighlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = student_life_community_highlights
        fields = '__all__'

class AboutusJoinGBUSerializer(serializers.ModelSerializer):
    class Meta:
        model = aboutus_joingbu
        fields = '__all__'

class ChancellorHeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChancellorHeroSection
        fields = '__all__'

class ChancellorMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChancellorMessage
        fields = '__all__'

class ViceChancellorHeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViceChancellorHeroSection
        fields = '__all__'

class ViceChancellorMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViceChancellorMessage
        fields = '__all__'

class GovernanceCommitteeHighlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Governance_committee_highlights
        fields = '__all__'

class GovernanceHeroSectionSerializer(serializers.ModelSerializer):
    highlights = GovernanceCommitteeHighlightsSerializer(many=True, read_only=True)

    class Meta:
        model = GovernanceHeroSection
        fields = '__all__'

class GovernanceOrganizationalStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Governance_organizational_structure
        fields = '__all__'

class PoliciesHeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliciesHeroSection
        fields = '__all__'

class UniversityPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityPolicy
        fields = '__all__'

class MandatoryHeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MandatoryHeroSection
        fields = '__all__'

class MandatoryComplianceDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mandatory_compliance_dashboard
        fields = '__all__'

class MandatoryComplianceItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mandatory_compliance_items
        fields = '__all__'

class MandatoryComplianceInformationAvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mandatory_compliance_information_available
        fields = '__all__'

class RegulatoryComplianceHighlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regulatory_compliance_highlights
        fields = '__all__'
