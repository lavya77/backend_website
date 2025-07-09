from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

# Admissions Process
router.register(r'admission-process-hero', views.AdmissionProcessHeroSectionViewSet)
router.register(r'step-process', views.StepProcessViewSet)
router.register(r'important-dates', views.ImportantDateViewSet)
router.register(r'required-documents', views.RequiredDocumentViewSet)
router.register(r'action-buttons', views.ActionButtonViewSet)

# Courses Offered
router.register(r'courses-offered-hero', views.CoursesOfferedHeroSectionViewSet)
router.register(r'stats-courses-offered', views.StatsCoursesOfferedViewSet)
router.register(r'school-course-offered', views.SchoolCourseOfferedViewSet)
router.register(r'schools-courses-offered', views.SchoolsCoursesOfferedViewSet)
router.register(r'courses-courses-offered', views.CoursesCoursesOfferedViewSet)
router.register(r'ready-to-apply-courses-offered', views.ReadyToApplyCoursesOfferedViewSet)

# Eligibility & Reservation
router.register(r'eligibility-hero', views.EligibilityReservationHeroSectionViewSet)
router.register(r'programs-eligibility', views.ProgramsEligibilityViewSet)

# Fee Structure
router.register(r'fee-structure', views.FeeStructureViewSet)
router.register(r'fee-structure-section', views.FeeStructureSectionViewSet)
router.register(r'program-fee-structure', views.ProgramFeeStructureViewSet)
router.register(r'fee-payments-option', views.FeePaymentsOptionViewSet)
router.register(r'scholarship-fee', views.ScholarshipFeeViewSet)
router.register(r'prospectus-fee', views.ProspectusFeeViewSet)

# International Admissions
router.register(r'international-hero', views.InternationalAdmissionsHeroSectionViewSet)
router.register(r'stats-international', views.StatsInternationalViewSet)
router.register(r'admission-tab-international', views.AdmissionTabInternationalViewSet)
router.register(r'eligibility-requirement-international', views.EligibilityRequirementInternationalViewSet)
router.register(r'required-document-international', views.RequiredDocumentInternationalViewSet)
router.register(r'application-step-international', views.ApplicationStepInternationalViewSet)
router.register(r'fee-structure-international', views.FeeStructureInternationalAdmissionsViewSet)
router.register(r'scholarship-international', views.ScholarshipInternationalViewSet)
router.register(r'student-support-international', views.StudentSupportServiceInternationalViewSet)
router.register(r'contact-office-international', views.ContactOfficeInternationalAdmissionsViewSet)
router.register(r'ready-to-apply-international', views.ReadyToApplyInternationalAdmissionsViewSet)

urlpatterns = router.urls

