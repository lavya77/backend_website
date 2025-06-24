from django.contrib import admin

# Register your models here.
from .models import (
    admission_process, step_process, ImportantDate, RequiredDocument, ActionButton,
    Courses_offered, stats_coursesoffered, schools_coursesoffered, courses_coursesoffered,
    ready_to_apply_coussesoffered, eligibility_rservation, programs_eligibility,
    Fee_structure, Program_Feestructure, international_admissions, stats_international,
    AdmissionTab_international, EligibilityRequirement_interanational, RequiredDocument_international,
    ApplicationStep_international, FeeStructure_internationaladdmisions,
    Scholarship_international, StudentSupportService_international, ContactOffice_ainternationaldmissions
)

admin.site.register(admission_process)
admin.site.register(step_process)
admin.site.register(ImportantDate)
admin.site.register(RequiredDocument)
admin.site.register(ActionButton)
admin.site.register(Courses_offered)
admin.site.register(stats_coursesoffered)
admin.site.register(schools_coursesoffered)
admin.site.register(courses_coursesoffered)
admin.site.register(ready_to_apply_coussesoffered)
admin.site.register(eligibility_rservation)
admin.site.register(programs_eligibility)
admin.site.register(Fee_structure)
admin.site.register(Program_Feestructure)
admin.site.register(international_admissions)
admin.site.register(stats_international)
admin.site.register(AdmissionTab_international)
admin.site.register(EligibilityRequirement_interanational)
admin.site.register(RequiredDocument_international)
admin.site.register(ApplicationStep_international)
admin.site.register(FeeStructure_internationaladdmisions)
admin.site.register(Scholarship_international)
admin.site.register(StudentSupportService_international)
admin.site.register(ContactOffice_ainternationaldmissions)
