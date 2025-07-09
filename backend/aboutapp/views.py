
from rest_framework import viewsets
from .models import *

from .serializers import *
# ---------------- About Us Section ----------------
class HeroSectionAboutUsViewSet(viewsets.ModelViewSet):
    queryset = HeroSectionAboutUs.objects.all()
    serializer_class = HeroSectionAboutUsSerializer

class Aboutus_StatsViewSet(viewsets.ModelViewSet):
    queryset = Aboutus_Stats.objects.all()
    serializer_class = Aboutus_StatsSerializer

class AboutusGBUViewSet(viewsets.ModelViewSet):
    queryset = aboutus_gbu.objects.all()
    serializer_class = AboutusGBUSerializer

class AboutUsCardsViewSet(viewsets.ModelViewSet):
    queryset = about_us_cards.objects.all()
    serializer_class = AboutUsCardsSerializer

class GovernanceOrganizationalHighlightsViewSet(viewsets.ModelViewSet):
    queryset = Governance_organizatonal_highlights.objects.all()
    serializer_class = GovernanceOrganizationalHighlightsSerializer

class AcademicSchoolProgramsStatsViewSet(viewsets.ModelViewSet):
    queryset = Academic_school_programs_stats.objects.all()
    serializer_class = AcademicSchoolProgramsStatsSerializer

class FacilitiesInfrastructureHighlightsViewSet(viewsets.ModelViewSet):
    queryset = facilities_infrastructure_highlights.objects.all()
    serializer_class = FacilitiesInfrastructureHighlightsSerializer

class HostelResedentialLifeViewSet(viewsets.ModelViewSet):
    queryset = Hostel_resedential_life.objects.all()
    serializer_class = HostelResedentialLifeSerializer

class WMeditationEllnessFeatureViewSet(viewsets.ModelViewSet):
    queryset = WMeditation_ellness_Feature.objects.all()
    serializer_class = WMeditationEllnessFeatureSerializer

class MeditationWellnesCenterViewSet(viewsets.ModelViewSet):
    queryset = Meditation_wellnes_center.objects.all()
    serializer_class = MeditationWellnesCenterSerializer

class GreenEcoFriendlyCampusHighlightsViewSet(viewsets.ModelViewSet):
    queryset = Green_eco_friendly_campus_highlights.objects.all()
    serializer_class = GreenEcoFriendlyCampusHighlightsSerializer

class SportsReactionFeaturesViewSet(viewsets.ModelViewSet):
    queryset = sports_reaction_features.objects.all()
    serializer_class = SportsReactionFeaturesSerializer

class SportsReactionHighlightsViewSet(viewsets.ModelViewSet):
    queryset = Sports_Reaction_highlights.objects.all()
    serializer_class = SportsReactionHighlightsSerializer

class ResearchInnovationHighlightsViewSet(viewsets.ModelViewSet):
    queryset = Research_innovation_highlights.objects.all()
    serializer_class = ResearchInnovationHighlightsSerializer

class StudentLifeCommunityHighlightsViewSet(viewsets.ModelViewSet):
    queryset = student_life_community_highlights.objects.all()
    serializer_class = StudentLifeCommunityHighlightsSerializer

class AboutusJoinGBUViewSet(viewsets.ModelViewSet):
    queryset = aboutus_joingbu.objects.all()
    serializer_class = AboutusJoinGBUSerializer

# ---------------- Chancellor Section ----------------
class ChancellorHeroSectionViewSet(viewsets.ModelViewSet):
    queryset = ChancellorHeroSection.objects.all()
    serializer_class = ChancellorHeroSectionSerializer

class ChancellorMessageViewSet(viewsets.ModelViewSet):
    queryset = ChancellorMessage.objects.all()
    serializer_class = ChancellorMessageSerializer

# ---------------- Vice Chancellor Section ----------------
class ViceChancellorHeroSectionViewSet(viewsets.ModelViewSet):
    queryset = ViceChancellorHeroSection.objects.all()
    serializer_class = ViceChancellorHeroSectionSerializer

class ViceChancellorMessageViewSet(viewsets.ModelViewSet):
    queryset = ViceChancellorMessage.objects.all()
    serializer_class = ViceChancellorMessageSerializer

# ---------------- Governance Section ----------------
class GovernanceCommitteeHighlightsViewSet(viewsets.ModelViewSet):
    queryset = Governance_committee_highlights.objects.all()
    serializer_class = GovernanceCommitteeHighlightsSerializer

class GovernanceHeroSectionViewSet(viewsets.ModelViewSet):
    queryset = GovernanceHeroSection.objects.all()
    serializer_class = GovernanceHeroSectionSerializer

class GovernanceOrganizationalStructureViewSet(viewsets.ModelViewSet):
    queryset = Governance_organizational_structure.objects.all()
    serializer_class = GovernanceOrganizationalStructureSerializer

# ---------------- Policies Section ----------------
class PoliciesHeroSectionViewSet(viewsets.ModelViewSet):
    queryset = PoliciesHeroSection.objects.all()
    serializer_class = PoliciesHeroSectionSerializer

class UniversityPolicyViewSet(viewsets.ModelViewSet):
    queryset = UniversityPolicy.objects.all()
    serializer_class = UniversityPolicySerializer

# ---------------- Mandatory Disclosure Section ----------------
class MandatoryHeroSectionViewSet(viewsets.ModelViewSet):
    queryset = MandatoryHeroSection.objects.all()
    serializer_class = MandatoryHeroSectionSerializer

class MandatoryComplianceDashboardViewSet(viewsets.ModelViewSet):
    queryset = Mandatory_compliance_dashboard.objects.all()
    serializer_class = MandatoryComplianceDashboardSerializer

class MandatoryComplianceItemsViewSet(viewsets.ModelViewSet):
    queryset = Mandatory_compliance_items.objects.all()
    serializer_class = MandatoryComplianceItemsSerializer

class MandatoryComplianceInformationAvailableViewSet(viewsets.ModelViewSet):
    queryset = Mandatory_compliance_information_available.objects.all()
    serializer_class = MandatoryComplianceInformationAvailableSerializer

class RegulatoryComplianceHighlightsViewSet(viewsets.ModelViewSet):
    queryset = Regulatory_compliance_highlights.objects.all()
    serializer_class = RegulatoryComplianceHighlightsSerializer
