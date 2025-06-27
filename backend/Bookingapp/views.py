from rest_framework import viewsets
from .models import BookingHeroSection, UserRole, BookingFacility
from .serializers import (
    BookingHeroSectionSerializer,
    UserRoleSerializer,
    BookingFacilitySerializer
)

class BookingHeroSectionViewSet(viewsets.ModelViewSet):
    queryset = BookingHeroSection.objects.all()
    serializer_class = BookingHeroSectionSerializer


class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer


class BookingFacilityViewSet(viewsets.ModelViewSet):
    queryset = BookingFacility.objects.all()
    serializer_class = BookingFacilitySerializer
