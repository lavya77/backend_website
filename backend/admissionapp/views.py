from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import (
    admission_process, step_process, ImportantDate, RequiredDocument, ActionButton,
    Courses_offered, stats_coursesoffered, schools_coursesoffered, courses_coursesoffered,
    ready_to_apply_coussesoffered, eligibility_rservation, programs_eligibility,
    Fee_structure, Program_Feestructure, international_admissions, stats_international,
    AdmissionTab_international, EligibilityRequirement_interanational, RequiredDocument_international,
    ApplicationStep_international, FeeStructure_internationaladdmisions,
    Scholarship_international, StudentSupportService_international, ContactOffice_ainternationaldmissions
)

# --- Admission Section ---

def admission_process_view(request):
    data = list(admission_process.objects.all().values())
    return JsonResponse(data, safe=False)

def step_process_view(request):
    data = list(step_process.objects.all().values())
    return JsonResponse(data, safe=False)

def important_dates_view(request):
    data = list(ImportantDate.objects.all().values())
    return JsonResponse(data, safe=False)

def required_documents_view(request):
    data = list(RequiredDocument.objects.all().values())
    return JsonResponse(data, safe=False)

def action_buttons_view(request):
    data = list(ActionButton.objects.all().values())
    return JsonResponse(data, safe=False)

# --- Courses Offered Section ---

def courses_offered_view(request):
    data = list(Courses_offered.objects.all().values())
    return JsonResponse(data, safe=False)

def stats_courses_offered_view(request):
    data = list(stats_coursesoffered.objects.all().values())
    return JsonResponse(data, safe=False)

def schools_courses_offered_view(request):
    data = list(schools_coursesoffered.objects.all().values())
    return JsonResponse(data, safe=False)

def courses_list_view(request):
    data = list(courses_coursesoffered.objects.all().values())
    return JsonResponse(data, safe=False)

def apply_courses_view(request):
    data = list(ready_to_apply_coussesoffered.objects.all().values())
    return JsonResponse(data, safe=False)

# --- Eligibility & Reservation ---

def eligibility_reservation_view(request):
    data = list(eligibility_rservation.objects.all().values())
    return JsonResponse(data, safe=False)

def programs_eligibility_view(request):
    data = list(programs_eligibility.objects.all().values())
    return JsonResponse(data, safe=False)

# --- Fee Structure ---

def fee_structure_overview_view(request):
    data = list(Fee_structure.objects.all().values())
    return JsonResponse(data, safe=False)

def program_fee_structure_view(request):
    data = list(Program_Feestructure.objects.all().values())
    return JsonResponse(data, safe=False)

# --- International Admissions ---

def international_admissions_view(request):
    data = list(international_admissions.objects.all().values())
    return JsonResponse(data, safe=False)

def stats_international_view(request):
    data = list(stats_international.objects.all().values())
    return JsonResponse(data, safe=False)

def admission_tabs_view(request):
    data = list(AdmissionTab_international.objects.all().values())
    return JsonResponse(data, safe=False)

def eligibility_requirements_international_view(request):
    data = list(EligibilityRequirement_interanational.objects.all().values())
    return JsonResponse(data, safe=False)

def required_documents_international_view(request):
    data = list(RequiredDocument_international.objects.all().values())
    return JsonResponse(data, safe=False)

def application_steps_international_view(request):
    data = list(ApplicationStep_international.objects.all().values())
    return JsonResponse(data, safe=False)

def international_fee_structure_view(request):
    data = list(FeeStructure_internationaladdmisions.objects.all().values())
    return JsonResponse(data, safe=False)

def international_scholarships_view(request):
    data = list(Scholarship_international.objects.all().values())
    return JsonResponse(data, safe=False)

def student_support_services_view(request):
    data = list(StudentSupportService_international.objects.all().values())
    return JsonResponse(data, safe=False)

def international_contact_offices_view(request):
    data = list(ContactOffice_ainternationaldmissions.objects.all().values())
    return JsonResponse(data, safe=False)
