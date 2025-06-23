from django.contrib import admin
from .models import *

# Academic Section
admin.site.register(academicherosection)
admin.site.register(AcademicEvent)
admin.site.register(AcademicRegulation)
admin.site.register(academic_Stayupdated)

# CBCS Section
admin.site.register(herosection_cbcs)
admin.site.register(what_is_cbcs)
admin.site.register(cbcs_courses)
admin.site.register(cbcs_GradingScale)
admin.site.register(benefits_cbcbs)
admin.site.register(Explore_cbcs)

# Faculty Section
admin.site.register(Facultydirectory)
admin.site.register(FacultyMember)
admin.site.register(faculty_join)

# Center of Excellence
admin.site.register(herosection_centereofexcellence)
admin.site.register(CenterOfExcellence)
admin.site.register(coe_gallery)
admin.site.register(join_coe)

# MOU & Collaborations
admin.site.register(herosection_mou)
admin.site.register(PartnerInstitute)
admin.site.register(CollaborationProgram)
admin.site.register(UpcomingOpportunity)
admin.site.register(collaborations_mou)

# Institutional Reports
admin.site.register(herosection_reports)
admin.site.register(InstitutionalReport)

# Schools
admin.site.register(School)
