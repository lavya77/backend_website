from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'placement-brochures', PlacementBrochureViewSet)
router.register(r'stats', StatsViewSet)
router.register(r'what-inside', WhatInsideViewSet)
router.register(r'brochure-section', BrochureSectionItemViewSet)
router.register(r'internship-opportunities', InternshipOpportunityViewSet)
router.register(r'companies', CompaniesViewSet)
router.register(r'internship-cards', InternshipCardViewSet)
router.register(r'internship-providers', InternshipProvidersViewSet)
router.register(r'application-process', ApplicationProcessViewSet)
router.register(r'journey-cards', JourneyCardViewSet)
router.register(r'placement-statistics', PlacementStatisticViewSet)
router.register(r'department-stats', DepartmentStatsViewSet)
router.register(r'package-distributions', PackageDistributionViewSet)
router.register(r'ugpg-placement-stats', UGPGPlacementStatsViewSet)
router.register(r'placement-offer-types', PlacementOfferTypeViewSet)
router.register(r'reports', ReportViewSet)
router.register(r'training-careers', TrainingCareerViewSet)
router.register(r'career-support-stats', CareerSupportStatViewSet)
router.register(r'key-topics-training', KeyTopicsTrainingViewSet)
router.register(r'training-programs', TrainingProgramViewSet)
router.register(r'career-services', CareerServicesViewSet)
router.register(r'upcoming-workshops', UpcomingWorkshopsViewSet)
router.register(r'ready-enhance-skills', ReadyEnhanceSkillsViewSet)
router.register(r'esteemed-campus', EsteemedCampusViewSet)
router.register(r'recruitment-highlights', RecruitmentHighlightsViewSet)
router.register(r'recruiter-companies', RecruiterCompanyViewSet)
router.register(r'what-recruiters-say', WhatRecruitersSayViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
