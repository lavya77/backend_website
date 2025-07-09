from django.contrib import admin
from . import models

# ----------------- Academic Section -----------------
admin.site.register(models.academicherosection_Regulations)
admin.site.register(models.acdemic_regulations_stats)
admin.site.register(models.academic_schedule_regulatioons)
admin.site.register(models.AcademicEvent)
admin.site.register(models.AcademicRegulation)
admin.site.register(models.academic_Stayupdated)

# ----------------- CBCS Section -----------------
admin.site.register(models.herosection_cbcs)
admin.site.register(models.cbcs_stats)
admin.site.register(models.what_is_cbcs)
admin.site.register(models.what_is_cbcs_cards)
admin.site.register(models.cbcs_GradingScale)
admin.site.register(models.benefits_cbcbs_title)
admin.site.register(models.benefits_cbcbs)
admin.site.register(models.Explore_cbcs)

# ----------------- Faculty Section -----------------
admin.site.register(models.faculty_directory_herosection)
admin.site.register(models.Facultydirectory_stats)
@admin.register(models.FacultyMember)
class FacultyMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'department', 'email', 'phone')
    search_fields = ('name', 'designation', 'email')
    list_filter = ('department',)

admin.site.register(models.faculty_join)

# ----------------- Centre of Excellence -----------------
admin.site.register(models.herosection_centereofexcellence)
admin.site.register(models.centre_of_excellence_highlights)
admin.site.register(models.centre_of_excellence_title)
admin.site.register(models.CenterOfExcellence)
admin.site.register(models.coe_gallery_title)
admin.site.register(models.coe_gallery)
admin.site.register(models.join_coe)

# ----------------- MOU & Collaborations -----------------
admin.site.register(models.herosection_mou)
admin.site.register(models.mous_stats)
admin.site.register(models.PartnerInstitute)
admin.site.register(models.CollaborationProgram)
admin.site.register(models.UpcomingOpportunity)
admin.site.register(models.collaborations_mou)

# ----------------- Institutional Reports -----------------
admin.site.register(models.herosection_reports)
admin.site.register(models.institutional_reports_stats)
@admin.register(models.InstitutionalReport)
class InstitutionalReportAdmin(admin.ModelAdmin):
    list_display = ('card_title', 'category', 'date', 'downloads', 'pages')
    search_fields = ('card_title',)
    list_filter = ('category',)

# ----------------- Schools -----------------
admin.site.register(models.School_herosection)
admin.site.register(models.school_stats)
admin.site.register(models.technology_schools)
admin.site.register(models.explore_academic_excellence_schools)
admin.site.register(models.school_journey)
