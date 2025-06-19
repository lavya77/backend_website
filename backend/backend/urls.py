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
from myapp import views as appview
from aboutapp import views
from academicapp import views as academicview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aboutus/',appview.About_view),
    path('banner/',appview.Banner_views),
    path('quickaccess/',appview.QuickAccess_views),
    path('ledership/',appview.Leadership_view),
    path('Glance/',appview.GlanceStat_views),
    path('CampusGallery/',appview.Campus_gallery_views),
    path('Excellence_education/',appview.Excellence_in_Education_views),
    path('Campus_life/',appview.Campus_life_views),
    path('companies/',appview.Companies_hiring_views),
    path('virtual_experience/',appview.VirtualExperience_views),
    path('hero-sections/', views.hero_section_view),
    path('generic-cards/', views.generic_card_view),
    path('timeline-elements/', views.timeline_element_view),
    path('tab-sections/', views.tab_section_view),
    path('image-cards/', views.image_card_view),
    path('progress-bars/', views.progress_bar_view),
    path('document-cards/', views.document_card_view),
    path('global-collaborations/', views.global_collaboration_view),
    path('governance-cards/', views.governance_card_view),
     # Academic
    path('academic/hero/', academicview.academic_hero_section_view),
    path('academic/events/', academicview.academic_events_view),
    path('academic/regulations/', academicview.academic_regulations_view),
    path('academic/stayupdated/', academicview.academic_stay_updated_view),

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
