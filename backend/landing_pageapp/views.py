from rest_framework import viewsets
from .models import *
from .serializers import *

class BannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class QuickAccessViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = QuickAccess.objects.all()
    serializer_class = QuickAccessSerializer

class AboutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class LeadershipViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Leadership.objects.all()
    serializer_class = LeadershipSerializer

class GlanceStatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GlanceStat.objects.all()
    serializer_class = GlanceStatSerializer

class CampusGalleryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Campus_gallery.objects.all()
    serializer_class = CampusGallerySerializer

class ExcellenceInEducationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Excellence_in_Education.objects.all()
    serializer_class = ExcellenceInEducationSerializer

class CampusLifeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Campus_life.objects.all()
    serializer_class = CampusLifeSerializer

class CompaniesHiringViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Companies_hiring.objects.all()
    serializer_class = CompaniesHiringSerializer

class VirtualExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VirtualExperience.objects.all()
    serializer_class = VirtualExperienceSerializer

class NewsAndEventsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NewsandEvents.objects.all()
    serializer_class = NewsAndEventsSerializer
