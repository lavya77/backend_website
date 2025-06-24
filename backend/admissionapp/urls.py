from django.contrib import admin
from django.urls import path
from admissionapp import views as admissionview

urlpatterns = [
    # Admission & Process
    path('admission-process/', admissionview.admission_process_view),
    path('step-process/', admissionview.step_process_view),
    path('important-dates/', admissionview.important_dates_view),
    path('required-documents/', admissionview.required_documents_view),
    path('action-buttons/', admissionview.action_buttons_view),

    # Courses Offered
    path('courses-offered/', admissionview.courses_offered_view),
    path('stats-courses-offered/', admissionview.stats_courses_offered_view),
    path('schools-courses-offered/', admissionview.schools_courses_offered_view),
    path('courses-list/', admissionview.courses_list_view),
    path('apply-courses/', admissionview.apply_courses_view),

    # Eligibility & Reservation
    path('eligibility-reservation/', admissionview.eligibility_reservation_view),
    path('programs-eligibility/', admissionview.programs_eligibility_view),

    # Fee Structure
    path('fee-structure-overview/', admissionview.fee_structure_overview_view),
    path('program-fee-structure/', admissionview.program_fee_structure_view),

    # International Admissions
    path('international-admissions/', admissionview.international_admissions_view),
    path('stats-international/', admissionview.stats_international_view),
    path('admission-tabs/', admissionview.admission_tabs_view),
    path('international-eligibility/', admissionview.eligibility_requirements_international_view),
    path('international-documents/', admissionview.required_documents_international_view),
    path('international-application-steps/', admissionview.application_steps_international_view),
    path('international-fee-structure/', admissionview.international_fee_structure_view),
    path('international-scholarships/', admissionview.international_scholarships_view),
    path('international-support-services/', admissionview.student_support_services_view),
    path('international-contact-offices/', admissionview.international_contact_offices_view),
]
