from rest_framework import viewsets
from .models import contact_herosection, Contact
from .serializers import ContactHeroSectionSerializer, ContactSerializer

class ContactHeroSectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = contact_herosection.objects.all()
    serializer_class = ContactHeroSectionSerializer


class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contact.objects.filter(is_active=True)
    serializer_class = ContactSerializer
