from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

# ----------------- Academic Section -----------------
router.register(r'academic-herosection', views.academicherosection_RegulationsViewSet)
router.register(r'academic-regulations-stats', views.acdemic_regulations_statsViewSet)
router.register(r'academic-schedule', views.academic_schedule_regulatioonsViewSet)
router.register(r'academic-events', views.AcademicEventViewSet)
router.register(r'academic-regulations', views.AcademicRegulationViewSet)
router.register(r'academic-stayupdated', views.academic_StayupdatedViewSet)

# ----------------- CBCS Section -----------------
router.register(r'herosection-cbcs', views.herosection_cbcsViewSet)
router.register(r'cbcs-stats', views.cbcs_statsViewSet)
router.register(r'what-is-cbcs', views.what_is_cbcsViewSet)
router.register(r'what-is-cbcs-cards', views.what_is_cbcs_cardsViewSet)
router.register(r'cbcs-grading-scale', views.cbcs_GradingScaleViewSet)
router.register(r'benefits-cbcbs-title', views.benefits_cbcbs_titleViewSet)
router.register(r'benefits-cbcbs', views.benefits_cbcbsViewSet)
router.register(r'explore-cbcs', views.Explore_cbcsViewSet)

# ----------------- Faculty Section -----------------
router.register(r'faculty-directory-herosection', views.faculty_directory_herosectionViewSet)
router.register(r'faculty-directory-stats', views.Facultydirectory_statsViewSet)
router.register(r'faculty-members', views.FacultyMemberViewSet)
router.register(r'faculty-join', views.faculty_joinViewSet)

# ----------------- Centre of Excellence -----------------
router.register(r'herosection-centereofexcellence', views.herosection_centereofexcellenceViewSet)
router.register(r'centre-of-excellence-highlights', views.centre_of_excellence_highlightsViewSet)
router.register(r'centre-of-excellence-title', views.centre_of_excellence_titleViewSet)
router.register(r'center-of-excellence', views.CenterOfExcellenceViewSet)
router.register(r'coe-gallery-title', views.coe_gallery_titleViewSet)
router.register(r'coe-gallery', views.coe_galleryViewSet)
router.register(r'join-coe', views.join_coeViewSet)

# ----------------- MOU & Collaborations -----------------
router.register(r'herosection-mou', views.herosection_mouViewSet)
router.register(r'mous-stats', views.mous_statsViewSet)
router.register(r'partner-institutes', views.PartnerInstituteViewSet)
router.register(r'collaboration-programs', views.CollaborationProgramViewSet)
router.register(r'upcoming-opportunities', views.UpcomingOpportunityViewSet)
router.register(r'collaborations-mou', views.collaborations_mouViewSet)

# ----------------- Institutional Reports -----------------
router.register(r'herosection-reports', views.herosection_reportsViewSet)
router.register(r'institutional-reports-stats', views.institutional_reports_statsViewSet)
router.register(r'institutional-reports', views.InstitutionalReportViewSet)

# ----------------- Schools -----------------
router.register(r'school-herosection', views.School_herosectionViewSet)
router.register(r'school-stats', views.school_statsViewSet)
router.register(r'technology-schools', views.technology_schoolsViewSet)
router.register(r'explore-academic-excellence-schools', views.explore_academic_excellence_schoolsViewSet)
router.register(r'school-journey', views.school_journeyViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
