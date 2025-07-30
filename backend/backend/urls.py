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
from aboutapp import urls as aboutapp_urls
from academicapp import views as academicview
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("landing/", include("landing_pageapp.urls")),
    path("academic/", include("academicapp.urls")),
    path('admin/', admin.site.urls),
    path('aboutus/',include("aboutapp.urls")),
    path('admission/',include("admissionapp.urls")),
    path('resarch/',include("Researchapp.urls")),
    path('alumini/',include("Aluminiapp.urls")),
    path('placement/',include("placementapp.urls")),
    path('campuslife/',include("campuslifeapp.urls")),
    path('contact_directory/',include("contact_directory.urls")),
    path('Faculty_Directory/',include("facultyDirectory.urls")),
    path('Bookingapp',include("Bookingapp.urls")),
    path('Schools',include("Schoolapp.urls")),
  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)