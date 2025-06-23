from django.contrib import admin
from django.urls import path , include
from landing_pageapp import views  as appview
from landing_pageapp import urls as landing_url 
from aboutapp import views as views
from academicapp import views as academicview
 

urlpatterns = [
    path('hero-sections/', views.hero_section_view),
    path('generic-cards/', views.generic_card_view),
    path('timeline-elements/', views.timeline_element_view),
    path('tab-sections/', views.tab_section_view),
    path('image-cards/', views.image_card_view),
    path('progress-bars/', views.progress_bar_view),
    path('document-cards/', views.document_card_view),
    path('global-collaborations/', views.global_collaboration_view),
    path('governance-cards/', views.governance_card_view),
     
]