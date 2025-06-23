from django.http import JsonResponse
from .models import *

# Academic Section
def academic_hero_section_view(request):
    data = list(academicherosection.objects.all().values())
    return JsonResponse(data, safe=False)

def academic_events_view(request):
    data = list(AcademicEvent.objects.all().values())
    return JsonResponse(data, safe=False)

def academic_regulations_view(request):
    data = list(AcademicRegulation.objects.all().values())
    return JsonResponse(data, safe=False)

def academic_stay_updated_view(request):
    data = list(academic_Stayupdated.objects.all().values())
    return JsonResponse(data, safe=False)


# CBCS Section
def hero_section_cbcs_view(request):
    data = list(herosection_cbcs.objects.all().values())
    return JsonResponse(data, safe=False)

def what_is_cbcs_view(request):
    data = list(what_is_cbcs.objects.all().values())
    return JsonResponse(data, safe=False)

def cbcs_courses_view(request):
    data = list(cbcs_courses.objects.all().values())
    return JsonResponse(data, safe=False)

def cbcs_grading_scale_view(request):
    data = list(cbcs_GradingScale.objects.all().values())
    return JsonResponse(data, safe=False)

def benefits_cbcs_view(request):
    data = list(benefits_cbcbs.objects.all().values())
    return JsonResponse(data, safe=False)

def explore_cbcs_view(request):
    data = list(Explore_cbcs.objects.all().values())
    return JsonResponse(data, safe=False)


# Faculty Section
def faculty_directory_view(request):
    data = list(Facultydirectory.objects.all().values())
    return JsonResponse(data, safe=False)

def faculty_members_view(request):
    data = list(FacultyMember.objects.all().values())
    return JsonResponse(data, safe=False)

def faculty_join_view(request):
    data = list(faculty_join.objects.all().values())
    return JsonResponse(data, safe=False)


# Centre of Excellence
def hero_section_coe_view(request):
    data = list(herosection_centereofexcellence.objects.all().values())
    return JsonResponse(data, safe=False)

def coe_view(request):
    data = list(CenterOfExcellence.objects.all().values())
    return JsonResponse(data, safe=False)

def coe_gallery_view(request):
    data = list(coe_gallery.objects.all().values())
    return JsonResponse(data, safe=False)

def join_coe_view(request):
    data = list(join_coe.objects.all().values())
    return JsonResponse(data, safe=False)


# MOU & Collaborations
def hero_section_mou_view(request):
    data = list(herosection_mou.objects.all().values())
    return JsonResponse(data, safe=False)

def partner_institutes_view(request):
    data = list(PartnerInstitute.objects.all().values())
    return JsonResponse(data, safe=False)

def collaboration_programs_view(request):
    data = list(CollaborationProgram.objects.all().values())
    return JsonResponse(data, safe=False)

def upcoming_opportunities_view(request):
    data = list(UpcomingOpportunity.objects.all().values())
    return JsonResponse(data, safe=False)

def collaborations_mou_view(request):
    data = list(collaborations_mou.objects.all().values())
    return JsonResponse(data, safe=False)


# Institutional Reports
def hero_section_reports_view(request):
    data = list(herosection_reports.objects.all().values())
    return JsonResponse(data, safe=False)

def institutional_reports_view(request):
    data = list(InstitutionalReport.objects.all().values())
    return JsonResponse(data, safe=False)


# Schools
def schools_view(request):
    data = list(School.objects.all().values())
    return JsonResponse(data, safe=False)
