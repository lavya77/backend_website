from rest_framework import viewsets
from .models import *
from .serializers import *

# ---------------- Admission Process Section ----------------

class AdmissionProcessHeroSectionViewSet(viewsets.ModelViewSet):
    queryset = admission_process_herosection.objects.all()
    serializer_class = AdmissionProcessHeroSectionSerializer

class StepProcessViewSet(viewsets.ModelViewSet):
    queryset = step_process.objects.all()
    serializer_class = StepProcessSerializer

class ImportantDateViewSet(viewsets.ModelViewSet):
    queryset = ImportantDate.objects.all()
    serializer_class = ImportantDateSerializer

class RequiredDocumentViewSet(viewsets.ModelViewSet):
    queryset = RequiredDocument.objects.all()
    serializer_class = RequiredDocumentSerializer

class ActionButtonViewSet(viewsets.ModelViewSet):
    queryset = ActionButton.objects.all()
    serializer_class = ActionButtonSerializer


# ---------------- Courses Offered Section ----------------

class CoursesOfferedHeroSectionViewSet(viewsets.ModelViewSet):
    queryset = Courses_offered_herosection.objects.all()
    serializer_class = CoursesOfferedHeroSectionSerializer

class StatsCoursesOfferedViewSet(viewsets.ModelViewSet):
    queryset = stats_coursesoffered.objects.all()
    serializer_class = StatsCoursesOfferedSerializer

class SchoolCourseOfferedViewSet(viewsets.ModelViewSet):
    queryset = School_course_offered.objects.all()
    serializer_class = SchoolCourseOfferedSerializer

class SchoolsCoursesOfferedViewSet(viewsets.ModelViewSet):
    queryset = schools_coursesoffered.objects.all()
    serializer_class = SchoolsCoursesOfferedSerializer

class CoursesCoursesOfferedViewSet(viewsets.ModelViewSet):
    queryset = courses_coursesoffered.objects.all()
    serializer_class = CoursesCoursesOfferedSerializer

class ReadyToApplyCoursesOfferedViewSet(viewsets.ModelViewSet):
    queryset = ready_to_apply_coussesoffered.objects.all()
    serializer_class = ReadyToApplyCoursesOfferedSerializer


# ---------------- Eligibility and Reservation Section ----------------

class EligibilityReservationHeroSectionViewSet(viewsets.ModelViewSet):
    queryset = eligibility_rservation_herosection.objects.all()
    serializer_class = EligibilityReservationHeroSectionSerializer

class ProgramsEligibilityViewSet(viewsets.ModelViewSet):
    queryset = programs_eligibility.objects.all()
    serializer_class = ProgramsEligibilitySerializer


# ---------------- Fee Structure Section ----------------

class FeeStructureViewSet(viewsets.ModelViewSet):
    queryset = Fee_structure.objects.all()
    serializer_class = FeeStructureSerializer

class FeeStructureSectionViewSet(viewsets.ModelViewSet):
    queryset = Fee_structure_section.objects.all()
    serializer_class = FeeStructureSectionSerializer

class ProgramFeeStructureViewSet(viewsets.ModelViewSet):
    queryset = Program_Feestructure.objects.all()
    serializer_class = ProgramFeeStructureSerializer

class FeePaymentsOptionViewSet(viewsets.ModelViewSet):
    queryset = Fee_Payments_option.objects.all()
    serializer_class = FeePaymentsOptionSerializer

class ScholarshipFeeViewSet(viewsets.ModelViewSet):
    queryset = Scholarship_feee.objects.all()
    serializer_class = ScholarshipFeeSerializer

class ProspectusFeeViewSet(viewsets.ModelViewSet):
    queryset = prospectus_fee.objects.all()
    serializer_class = ProspectusFeeSerializer


# ---------------- International Admissions Section ----------------

class InternationalAdmissionsHeroSectionViewSet(viewsets.ModelViewSet):
    queryset = international_admissions_herosection.objects.all()
    serializer_class = InternationalAdmissionsHeroSectionSerializer

class StatsInternationalViewSet(viewsets.ModelViewSet):
    queryset = stats_international.objects.all()
    serializer_class = StatsInternationalSerializer

class AdmissionTabInternationalViewSet(viewsets.ModelViewSet):
    queryset = AdmissionTab_international.objects.all()
    serializer_class = AdmissionTabInternationalSerializer

class EligibilityRequirementInternationalViewSet(viewsets.ModelViewSet):
    queryset = EligibilityRequirement_interanational.objects.all()
    serializer_class = EligibilityRequirementInternationalSerializer

class RequiredDocumentInternationalViewSet(viewsets.ModelViewSet):
    queryset = RequiredDocument_international.objects.all()
    serializer_class = RequiredDocumentInternationalSerializer

class ApplicationStepInternationalViewSet(viewsets.ModelViewSet):
    queryset = ApplicationStep_international.objects.all()
    serializer_class = ApplicationStepInternationalSerializer

class FeeStructureInternationalAdmissionsViewSet(viewsets.ModelViewSet):
    queryset = FeeStructure_internationaladdmisions.objects.all()
    serializer_class = FeeStructureInternationalAdmissionsSerializer

class ScholarshipInternationalViewSet(viewsets.ModelViewSet):
    queryset = Scholarship_international.objects.all()
    serializer_class = ScholarshipInternationalSerializer

class StudentSupportServiceInternationalViewSet(viewsets.ModelViewSet):
    queryset = StudentSupportService_international.objects.all()
    serializer_class = StudentSupportServiceInternationalSerializer

class ContactOfficeInternationalAdmissionsViewSet(viewsets.ModelViewSet):
    queryset = ContactOffice_ainternationaldmissions.objects.all()
    serializer_class = ContactOfficeInternationalAdmissionsSerializer

class ReadyToApplyInternationalAdmissionsViewSet(viewsets.ModelViewSet):
    queryset = Ready_toAplly_internationaladmissions.objects.all()
    serializer_class = ReadyToApplyInternationalAdmissionsSerializer
