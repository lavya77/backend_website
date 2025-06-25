from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactHeroSectionViewSet, ContactViewSet

router = DefaultRouter()
router.register(r'contact-hero-section', ContactHeroSectionViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
