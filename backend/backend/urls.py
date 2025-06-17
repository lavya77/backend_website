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
    path('virtual_experience/',appview.VirtualExperience_views)
]
