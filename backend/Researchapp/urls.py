from django.urls import path
from Researchapp import views as research_views  
urlpatterns = [
    path('coe-hero-section/', research_views.coe_hero_section_view),
    path('research-highlights/', research_views.research_highlights_view),
    path('research-labs/', research_views.research_labs_view),
    path('publications-hero-section/', research_views.publications_hero_section_view),
    path('publication-highlights/', research_views.publication_highlights_view),
    path('publication-list/', research_views.publication_list_view),
    path('startups-highlights/', research_views.startups_highlight_view),
    path('startups/', research_views.startups_list_view),
    path('join-startups/', research_views.join_startups_view),
    path('funded-projects/', research_views.funded_project_view),
    path('funded-stats/', research_views.funded_stats_view),
    path('funded-project-cards/', research_views.funded_project_cards_view),
]
