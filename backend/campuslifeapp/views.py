from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import viewsets


# ---------- Campus Hero ----------
class CampusHeroListView(viewsets.ReadOnlyModelViewSet):
    queryset = CampusHero.objects.all()
    serializer_class = CampusHeroSerializer

# ---------- Virtual Tour ----------
class VirtualTourListView(viewsets.ReadOnlyModelViewSet):
    queryset = VirtualTour.objects.all()
    serializer_class = VirtualTourSerializer

# ---------- Key Highlights ----------
class KeyHighlightsListView(viewsets.ReadOnlyModelViewSet):
    queryset = key_highlights.objects.all()
    serializer_class = KeyHighlightsSerializer

# ---------- Campus Life Stats ----------
class CampusLifeStatsListView(viewsets.ReadOnlyModelViewSet):
    queryset = campus_life_stats.objects.all()
    serializer_class = CampusLifeStatsSerializer

# ---------- Hostel Life ----------
class HostelLifeSectionListView(viewsets.ReadOnlyModelViewSet):
    queryset = HostelLifeSection.objects.all()
    serializer_class = HostelLifeSectionSerializer

class HostelListView(viewsets.ReadOnlyModelViewSet):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer

class HostelDetailListView(viewsets.ReadOnlyModelViewSet):
    queryset = HostelDetail.objects.all()
    serializer_class = HostelDetailSerializer

class AmenityListView(viewsets.ReadOnlyModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

# ---------- Student Clubs ----------
class StudentClubListView(viewsets.ReadOnlyModelViewSet):
    queryset = Student_club.objects.all()
    serializer_class = StudentClubSerializer

class ActivityListView(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class AchievementListView(viewsets.ReadOnlyModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

# ---------- Library ----------
class LibraryGBUListView(viewsets.ReadOnlyModelViewSet):
    queryset = Library_gbu.objects.all()
    serializer_class = LibraryGBUSerializer

class LibraryStatListView(viewsets.ReadOnlyModelViewSet):
    queryset = LibraryStat.objects.all()
    serializer_class = LibraryStatSerializer

class LibraryFacilityListView(viewsets.ReadOnlyModelViewSet):
    queryset = LibraryFacility.objects.all()
    serializer_class = LibraryFacilitySerializer

class LibraryStatsListView(viewsets.ReadOnlyModelViewSet):
    queryset = LibraryStats.objects.all()
    serializer_class = LibraryStatsSerializer

# ---------- Sports ----------
class SportsFacilityListView(viewsets.ReadOnlyModelViewSet):
    queryset = SportsFacility.objects.all()
    serializer_class = SportsFacilitySerializer


class FacilityFeatureListView(viewsets.ReadOnlyModelViewSet):
    queryset = FacilityFeature.objects.all()
    serializer_class = FacilityFeatureSerializer

# ---------- Food Court ----------
class FoodCourtCategoryListView(viewsets.ReadOnlyModelViewSet):
    queryset = FoodCourtCategory.objects.all()
    serializer_class = FoodCourtCategorySerializer

class FoodCourtItemListView(viewsets.ReadOnlyModelViewSet):
    queryset = FoodCourtItem.objects.all()
    serializer_class = FoodCourtItemSerializer

class FoodOutletListView(viewsets.ReadOnlyModelViewSet):
    queryset = FoodOutlet.objects.all()
    serializer_class = FoodOutletSerializer

class TagListView(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# ---------- Eco Campus ----------
class EcoCampusStatListView(viewsets.ReadOnlyModelViewSet):
    queryset = EcoCampusStat.objects.all()
    serializer_class = EcoCampusStatSerializer

class EcoInitiativeStatsListView(viewsets.ReadOnlyModelViewSet):
    queryset = EcoInitiative_stats.objects.all()
    serializer_class = EcoInitiativeStatsSerializer

class GreenInitiativeListView(viewsets.ReadOnlyModelViewSet):
    queryset = GreenInitiative.objects.all()
    serializer_class = GreenInitiativeSerializer

class ImpactStatListView(viewsets.ReadOnlyModelViewSet):
    queryset = ImpactStat.objects.all()
    serializer_class = ImpactStatSerializer

# ---------- Testimonials ----------
class StudentTestimonialListView(viewsets.ReadOnlyModelViewSet):
    queryset = StudentTestimonial.objects.all()
    serializer_class = StudentTestimonialSerializer

# ---------- Meditation ----------
class MeditationHeroSectionListView(viewsets.ReadOnlyModelViewSet):
    queryset = Meditation_herosection.objects.all()
    serializer_class = MeditationHeroSectionSerializer

class MeditationSessionListView(viewsets.ReadOnlyModelViewSet):
    queryset = MeditationSession.objects.all()
    serializer_class = MeditationSessionSerializer

class MeditationBenefitListView(viewsets.ReadOnlyModelViewSet):
    queryset = MeditationBenefit.objects.all()
    serializer_class = MeditationBenefitSerializer

class MeditationTechniqueListView(viewsets.ReadOnlyModelViewSet):
    queryset = MeditationTechnique.objects.all()
    serializer_class = MeditationTechniqueSerializer

# ---------- NSS / NCC ----------
class OrganizationListView(viewsets.ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class JoinNSSAndNCCListView(viewsets.ReadOnlyModelViewSet):
    queryset = join_nssandncc.objects.all()
    serializer_class = JoinNSSAndNCCSerializer
