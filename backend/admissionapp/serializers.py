from rest_framework import serializers
from .models import *

# ---------------- Admission Process Section ----------------

class AdmissionProcessHeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = admission_process_herosection
        fields = '__all__'

class StepProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = step_process
        fields = '__all__'

class ImportantDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportantDate
        fields = '__all__'

class RequiredDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequiredDocument
        fields = '__all__'

class ActionButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionButton
        fields = '__all__'


# ---------------- Courses Offered Section ----------------

class CoursesOfferedHeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses_offered_herosection
        fields = '__all__'

class StatsCoursesOfferedSerializer(serializers.ModelSerializer):
    class Meta:
        model = stats_coursesoffered
        fields = '__all__'

class SchoolCourseOfferedSerializer(serializers.ModelSerializer):
    class Meta:
        model = School_course_offered
        fields = '__all__'

class SchoolsCoursesOfferedSerializer(serializers.ModelSerializer):
    course = SchoolCourseOfferedSerializer()
    class Meta:
        model = schools_coursesoffered
        fields = '__all__'

class CoursesCoursesOfferedSerializer(serializers.ModelSerializer):
    course = SchoolCourseOfferedSerializer()
    class Meta:
        model = courses_coursesoffered
        fields = '__all__'

class ReadyToApplyCoursesOfferedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ready_to_apply_coussesoffered
        fields = '__all__'


# ---------------- Eligibility and Reservation Section ----------------

class EligibilityReservationHeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = eligibility_rservation_herosection
        fields = '__all__'

class ProgramsEligibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = programs_eligibility
        fields = '__all__'


# ---------------- Fee Structure Section ----------------

class FeeStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee_structure
        fields = '__all__'

class FeeStructureSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee_structure_section
        fields = '__all__'

class ProgramFeeStructureSerializer(serializers.ModelSerializer):
    section_name = FeeStructureSectionSerializer()
    class Meta:
        model = Program_Feestructure
        fields = '__all__'

class FeePaymentsOptionSerializer(serializers.ModelSerializer):
    section_name = FeeStructureSectionSerializer()
    class Meta:
        model = Fee_Payments_option
        fields = '__all__'

class ScholarshipFeeSerializer(serializers.ModelSerializer):
    section_name = FeeStructureSectionSerializer()
    class Meta:
        model = Scholarship_feee
        fields = '__all__'

class ProspectusFeeSerializer(serializers.ModelSerializer):
    section_name = FeeStructureSectionSerializer()
    class Meta:
        model = prospectus_fee
        fields = '__all__'


# ---------------- International Admissions Section ----------------

class InternationalAdmissionsHeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = international_admissions_herosection
        fields = '__all__'

class StatsInternationalSerializer(serializers.ModelSerializer):
    class Meta:
        model = stats_international
        fields = '__all__'

class AdmissionTabInternationalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionTab_international
        fields = '__all__'

class RequiredDocumentInternationalSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequiredDocument_international
        fields = '__all__'

class EligibilityRequirementInternationalSerializer(serializers.ModelSerializer):
    documents = RequiredDocumentInternationalSerializer(many=True, read_only=True)
    class Meta:
        model = EligibilityRequirement_interanational
        fields = '__all__'

class ApplicationStepInternationalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationStep_international
        fields = '__all__'

class FeeStructureInternationalAdmissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeStructure_internationaladdmisions
        fields = '__all__'

class ScholarshipInternationalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholarship_international
        fields = '__all__'

class StudentSupportServiceInternationalSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSupportService_international
        fields = '__all__'

class ContactOfficeInternationalAdmissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactOffice_ainternationaldmissions
        fields = '__all__'

class ReadyToApplyInternationalAdmissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ready_toAplly_internationaladmissions
        fields = '__all__'
