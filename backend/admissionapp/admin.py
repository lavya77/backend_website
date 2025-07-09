from django.contrib import admin
from .models import *

# ---------- Admission Process ----------
admin.site.register(admission_process_herosection)
admin.site.register(step_process)
admin.site.register(ImportantDate)
admin.site.register(RequiredDocument)
admin.site.register(ActionButton)

# ---------- Courses Offered ----------
admin.site.register(Courses_offered_herosection)
admin.site.register(stats_coursesoffered)
admin.site.register(School_course_offered)
admin.site.register(schools_coursesoffered)
admin.site.register(courses_coursesoffered)
admin.site.register(ready_to_apply_coussesoffered)

# ---------- Eligibility & Reservation ----------
admin.site.register(eligibility_rservation_herosection)
admin.site.register(programs_eligibility)

# ---------- Fee Structure ----------
admin.site.register(Fee_structure)
admin.site.register(Fee_structure_section)
admin.site.register(Program_Feestructure)
admin.site.register(Fee_Payments_option)
admin.site.register(Scholarship_feee)
admin.site.register(prospectus_fee)

# ---------- International Admissions ----------
admin.site.register(international_admissions_herosection)
admin.site.register(stats_international)
admin.site.register(AdmissionTab_international)
admin.site.register(EligibilityRequirement_interanational)
admin.site.register(RequiredDocument_international)
admin.site.register(ApplicationStep_international)
admin.site.register(FeeStructure_internationaladdmisions)
admin.site.register(Scholarship_international)
admin.site.register(StudentSupportService_international)
admin.site.register(ContactOffice_ainternationaldmissions)
admin.site.register(Ready_toAplly_internationaladmissions)
