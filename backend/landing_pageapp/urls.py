from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BannerViewSet, QuickAccessViewSet, AboutViewSet, LeadershipViewSet,
    GlanceStatViewSet, CampusGalleryViewSet, ExcellenceInEducationViewSet,
    CampusLifeViewSet, CompaniesHiringViewSet, VirtualExperienceViewSet,
    NewsAndEventsViewSet
)

router = DefaultRouter()
router.register(r'banner', BannerViewSet)
router.register(r'quick-access', QuickAccessViewSet)
router.register(r'about', AboutViewSet)
router.register(r'leadership', LeadershipViewSet)
router.register(r'glance-stat', GlanceStatViewSet)
router.register(r'campus-gallery', CampusGalleryViewSet)
router.register(r'excellence-in-education', ExcellenceInEducationViewSet)
router.register(r'campus-life', CampusLifeViewSet)
router.register(r'companies-hiring', CompaniesHiringViewSet)
router.register(r'virtual-experience', VirtualExperienceViewSet)
router.register(r'news-and-events', NewsAndEventsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
