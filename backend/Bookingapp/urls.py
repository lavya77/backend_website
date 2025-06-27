from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BookingHeroSectionViewSet,
    UserRoleViewSet,
    BookingFacilityViewSet
)

router = DefaultRouter()
router.register(r'hero-sections', BookingHeroSectionViewSet, basename='hero-section')
router.register(r'user-roles', UserRoleViewSet, basename='user-role')
router.register(r'facilities', BookingFacilityViewSet, basename='facility')

urlpatterns = [
    path('', include(router.urls)),
]
