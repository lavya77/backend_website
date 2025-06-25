from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JoinOurAlumniViewSet, BranchViewSet, AlumniProfileViewSet

router = DefaultRouter()
router.register(r'join-our-alumni', JoinOurAlumniViewSet)
router.register(r'branches', BranchViewSet)
router.register(r'alumni', AlumniProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
