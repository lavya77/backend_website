"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from landing_pageapp import views as appview
from aboutapp import views
from academicapp import views as academicview

urlpatterns = [
    
    path('hero/', academicview.academic_hero_section_view),
    path('events/', academicview.academic_events_view),
    path('regulations/', academicview.academic_regulations_view),
    path('stayupdated/', academicview.academic_stay_updated_view),

    # CBCS
    path('cbcs/hero/', academicview.hero_section_cbcs_view),
    path('cbcs/what/', academicview.what_is_cbcs_view),
    path('cbcs/courses/', academicview.cbcs_courses_view),
    path('cbcs/grading/', academicview.cbcs_grading_scale_view),
    path('cbcs/benefits/', academicview.benefits_cbcs_view),
    path('cbcs/explore/', academicview.explore_cbcs_view),

    # Faculty
    path('faculty/directory/', academicview.faculty_directory_view),
    path('faculty/members/', academicview.faculty_members_view),
    path('faculty/join/', academicview.faculty_join_view),

    # Centre of Excellence
    path('coe/hero/', academicview.hero_section_coe_view),
    path('coe/list/', academicview.coe_view),
    path('coe/gallery/', academicview.coe_gallery_view),
    path('coe/join/', academicview.join_coe_view),

    # MOUs
    path('mou/hero/', academicview.hero_section_mou_view),
    path('mou/partners/', academicview.partner_institutes_view),
    path('mou/programs/', academicview.collaboration_programs_view),
    path('mou/opportunities/', academicview.upcoming_opportunities_view),
    path('mou/collaborations/', academicview.collaborations_mou_view),

    # Reports
    path('reports/hero/', academicview.hero_section_reports_view),
    path('reports/list/', academicview.institutional_reports_view),

    # Schools
    path('schools/', academicview.schools_view),
]
