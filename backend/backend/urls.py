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
from django.urls import path , include
from landing_pageapp import views  as appview
from landing_pageapp import urls as landing_url 
from aboutapp import views
from academicapp import views as academicview
 

urlpatterns = [
    path("landing/", include("landing_pageapp.urls")),
    path("academic/", include("academicapp.urls")),
    path('admin/', admin.site.urls),
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