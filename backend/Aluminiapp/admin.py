from django.contrib import admin
from .models import JoinOurAlumni, Branch, AlumniProfile


@admin.register(JoinOurAlumni)
class JoinOurAlumniAdmin(admin.ModelAdmin):
    list_display = ('title', 'background_color')
    search_fields = ('title', 'description')
    list_editable = ('background_color',)


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(AlumniProfile)
class AlumniProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'branch', 'graduation_year', 'current_company', 'created_at')
    search_fields = ('full_name', 'email', 'current_company')
    list_filter = ('graduation_year', 'branch', 'available_for_job_referrals', 'available_for_career_mentoring')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
