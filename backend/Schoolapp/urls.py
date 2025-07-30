from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

# Register viewsets here
router.register(r'specializations', SpecializationViewSet)
router.register(r'category-labs', CtaegoryLabViewSet)
router.register(r'faculty-members', FacultyMemberViewSet)
router.register(r'expertise-skills', ExpertiseSkillsStudentAchieverViewSet)

router.register(r'school-ict-hero', SchoolICTHeroSectionViewSet)
router.register(r'school-about', SchoolAboutUsViewSet)
router.register(r'stats-speak', StatsSpeakForThemselvesViewSet)
router.register(r'dean-message', DeanMessageViewSet)
router.register(r'departments-school', DepartmentsSchoolViewSet)
router.register(r'our-programs', OurProgramsViewSet)
router.register(r'faculty-of-ict', FacultyOfICTViewSet)
router.register(r'notices', NoticesViewSet)
router.register(r'event-gallery', EventGalleryViewSet)
router.register(r'student-clubs', StudentClubsActivitiesViewSet)
router.register(r'placement-stats', PlacementStatsViewSet)
router.register(r'recent-placements', RecentPlacementViewSet)
router.register(r'recruiters', RecruitersViewSet)
router.register(r'startup-stats', StartupStatsViewSet)
router.register(r'student-startup', StudentStartupViewSet)
router.register(r'student-achievements', StudentAchievementsViewSet)
router.register(r'faculty-hero', FacultyHeroSectionViewSet)
router.register(r'departments-name', DepartmentsNameViewSet)
router.register(r'faculty-department-hero', FacultyDepartmentHeroSectionViewSet)
router.register(r'faculty-profile', FacultyProfileViewSet)
router.register(r'board-studies', BoardStudiesViewSet)
router.register(r'laboratory-excellence', LaboratoryExcellenceViewSet)
router.register(r'conference-activity', ConferenceActivityViewSet)
router.register(r'department-hod-message', DepartmentHodMessageViewSet)
router.register(r'department-statistics', DepartmentStatisticsViewSet)
router.register(r'academic-programs', AcademicProgramsDepartmentViewSet)
router.register(r'curriculum-department', CurriculumDepartmentViewSet)
router.register(r'research-excellence', ResearchExcellenceDepartmentsViewSet)
router.register(r'research-projects', ResearchExcellenceDepartmentsProjectsViewSet)
router.register(r'research-stats', ResearchExcellenceDepartmentsStatsViewSet)
router.register(r'student-achievers-department', StudentAchieversDepartmentViewSet)
router.register(r'our-achievements-department', OurAchievementsDepartmentsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
