from rest_framework import viewsets
from .models import JoinOurAlumni, Branch, AlumniProfile
from .serializers import JoinOurAlumniSerializer, BranchSerializer, AlumniProfileSerializer


class JoinOurAlumniViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Join Our Alumni Banner section.
    Supports: list, retrieve, create, update, delete
    """
    queryset = JoinOurAlumni.objects.all()
    serializer_class = JoinOurAlumniSerializer


class BranchViewSet(viewsets.ModelViewSet):
    """
    ViewSet for academic branches.
    """
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class AlumniProfileViewSet(viewsets.ModelViewSet):
    """
    ViewSet for alumni profiles.
    """
    queryset = AlumniProfile.objects.all()
    serializer_class = AlumniProfileSerializer
