from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

# -------- About Us Section --------
router.register(r'aboutus-herosection', views.HeroSectionAboutUsViewSet)
router.register(r'aboutus-stats', views.Aboutus_StatsViewSet)
router.register(r'aboutus-gbu', views.AboutusGBUViewSet)
router.register(r'aboutus-cards', views.AboutUsCardsViewSet)
router.register(r'governance-organizational-highlights', views.GovernanceOrganizationalHighlightsViewSet)
router.register(r'academic-school-programs-stats', views.AcademicSchoolProgramsStatsViewSet)
router.register(r'facilities-infrastructure-highlights', views.FacilitiesInfrastructureHighlightsViewSet)
router.register(r'hostel-residential-life', views.HostelResedentialLifeViewSet)
router.register(r'meditation-wellness-feature', views.WMeditationEllnessFeatureViewSet)
router.register(r'meditation-wellness-center', views.MeditationWellnesCenterViewSet)
router.register(r'green-eco-friendly-campus-highlights', views.GreenEcoFriendlyCampusHighlightsViewSet)
router.register(r'sports-reaction-features', views.SportsReactionFeaturesViewSet)
router.register(r'sports-reaction-highlights', views.SportsReactionHighlightsViewSet)
router.register(r'research-innovation-highlights', views.ResearchInnovationHighlightsViewSet)
router.register(r'student-life-community-highlights', views.StudentLifeCommunityHighlightsViewSet)
router.register(r'aboutus-join-gbu', views.AboutusJoinGBUViewSet)

# -------- Chancellor Section --------
router.register(r'chancellor-hero-section', views.ChancellorHeroSectionViewSet)
router.register(r'chancellor-message', views.ChancellorMessageViewSet)

# -------- Vice Chancellor Section --------
router.register(r'vice-chancellor-hero-section', views.ViceChancellorHeroSectionViewSet)
router.register(r'vice-chancellor-message', views.ViceChancellorMessageViewSet)

# -------- Governance Section --------
router.register(r'governance-committee-highlights', views.GovernanceCommitteeHighlightsViewSet)
router.register(r'governance-hero-section', views.GovernanceHeroSectionViewSet)
router.register(r'governance-organizational-structure', views.GovernanceOrganizationalStructureViewSet)

# -------- Policies Section --------
router.register(r'policies-hero-section', views.PoliciesHeroSectionViewSet)
router.register(r'university-policies', views.UniversityPolicyViewSet)

# -------- Mandatory Disclosure Section --------
router.register(r'mandatory-hero-section', views.MandatoryHeroSectionViewSet)
router.register(r'mandatory-compliance-dashboard', views.MandatoryComplianceDashboardViewSet)
router.register(r'mandatory-compliance-items', views.MandatoryComplianceItemsViewSet)
router.register(r'mandatory-compliance-information-available', views.MandatoryComplianceInformationAvailableViewSet)
router.register(r'regulatory-compliance-highlights', views.RegulatoryComplianceHighlightsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
