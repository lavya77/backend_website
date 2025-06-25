from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

# Campus
router.register(r'campus-hero', CampusHeroListView)
router.register(r'virtual-tours', VirtualTourListView)
router.register(r'key-highlights', KeyHighlightsListView)
router.register(r'campus-life-stats', CampusLifeStatsListView)

# Hostel
router.register(r'hostel-life-section', HostelLifeSectionListView)
router.register(r'hostels', HostelListView)
router.register(r'hostel-details', HostelDetailListView)
router.register(r'amenities', AmenityListView)

# Student Clubs
router.register(r'student-clubs', StudentClubListView)
router.register(r'activities', ActivityListView)
router.register(r'achievements', AchievementListView)

# Library
router.register(r'library-info', LibraryGBUListView)
router.register(r'library-stats', LibraryStatListView)
router.register(r'library-facilities', LibraryFacilityListView)
router.register(r'library-stats-new', LibraryStatsListView)

# Sports
router.register(r'sport-facilities', SportsFacilityListView)
router.register(r'features', FacilityFeatureListView)


# Food
router.register(r'food-court-categories', FoodCourtCategoryListView)
router.register(r'food-court-items', FoodCourtItemListView)
router.register(r'food-outlets', FoodOutletListView)
router.register(r'tags', TagListView)

# Green Campus
router.register(r'eco-campus-stats', EcoCampusStatListView)
router.register(r'eco-initiative-stats', EcoInitiativeStatsListView)
router.register(r'green-initiatives', GreenInitiativeListView)
router.register(r'impact-stats', ImpactStatListView)

# Testimonials
router.register(r'student-testimonials', StudentTestimonialListView)

# Meditation
router.register(r'meditation-hero', MeditationHeroSectionListView)
router.register(r'meditation-sessions', MeditationSessionListView)
router.register(r'meditation-benefits', MeditationBenefitListView)
router.register(r'meditation-techniques', MeditationTechniqueListView)

# NSS / NCC
router.register(r'organizations', OrganizationListView)
router.register(r'join-nss-ncc', JoinNSSAndNCCListView)

urlpatterns = [
    path('', include(router.urls)),
]
