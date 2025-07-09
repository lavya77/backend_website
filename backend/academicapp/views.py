from rest_framework import viewsets
from .models import *
from .serializers import *

class academicherosection_RegulationsViewSet(viewsets.ModelViewSet):
    queryset = academicherosection_Regulations.objects.all()
    serializer_class = academicherosection_RegulationsSerializer

class acdemic_regulations_statsViewSet(viewsets.ModelViewSet):
    queryset = acdemic_regulations_stats.objects.all()
    serializer_class = acdemic_regulations_statsSerializer

class academic_schedule_regulatioonsViewSet(viewsets.ModelViewSet):
    queryset = academic_schedule_regulatioons.objects.all()
    serializer_class = academic_schedule_regulatioonsSerializer

class AcademicEventViewSet(viewsets.ModelViewSet):
    queryset = AcademicEvent.objects.all()
    serializer_class = AcademicEventSerializer

class AcademicRegulationViewSet(viewsets.ModelViewSet):
    queryset = AcademicRegulation.objects.all()
    serializer_class = AcademicRegulationSerializer

class academic_StayupdatedViewSet(viewsets.ModelViewSet):
    queryset = academic_Stayupdated.objects.all()
    serializer_class = academic_StayupdatedSerializer

class herosection_cbcsViewSet(viewsets.ModelViewSet):
    queryset = herosection_cbcs.objects.all()
    serializer_class = herosection_cbcsSerializer

class cbcs_statsViewSet(viewsets.ModelViewSet):
    queryset = cbcs_stats.objects.all()
    serializer_class = cbcs_statsSerializer

class what_is_cbcsViewSet(viewsets.ModelViewSet):
    queryset = what_is_cbcs.objects.all()
    serializer_class = what_is_cbcsSerializer

class what_is_cbcs_cardsViewSet(viewsets.ModelViewSet):
    queryset = what_is_cbcs_cards.objects.all()
    serializer_class = what_is_cbcs_cardsSerializer

class cbcs_GradingScaleViewSet(viewsets.ModelViewSet):
    queryset = cbcs_GradingScale.objects.all()
    serializer_class = cbcs_GradingScaleSerializer

class benefits_cbcbs_titleViewSet(viewsets.ModelViewSet):
    queryset = benefits_cbcbs_title.objects.all()
    serializer_class = benefits_cbcbs_titleSerializer

class benefits_cbcbsViewSet(viewsets.ModelViewSet):
    queryset = benefits_cbcbs.objects.all()
    serializer_class = benefits_cbcbsSerializer

class Explore_cbcsViewSet(viewsets.ModelViewSet):
    queryset = Explore_cbcs.objects.all()
    serializer_class = Explore_cbcsSerializer

class faculty_directory_herosectionViewSet(viewsets.ModelViewSet):
    queryset = faculty_directory_herosection.objects.all()
    serializer_class = faculty_directory_herosectionSerializer

class Facultydirectory_statsViewSet(viewsets.ModelViewSet):
    queryset = Facultydirectory_stats.objects.all()
    serializer_class = Facultydirectory_statsSerializer

class FacultyMemberViewSet(viewsets.ModelViewSet):
    queryset = FacultyMember.objects.all()
    serializer_class = FacultyMemberSerializer

class faculty_joinViewSet(viewsets.ModelViewSet):
    queryset = faculty_join.objects.all()
    serializer_class = faculty_joinSerializer

class herosection_centereofexcellenceViewSet(viewsets.ModelViewSet):
    queryset = herosection_centereofexcellence.objects.all()
    serializer_class = herosection_centereofexcellenceSerializer

class centre_of_excellence_highlightsViewSet(viewsets.ModelViewSet):
    queryset = centre_of_excellence_highlights.objects.all()
    serializer_class = centre_of_excellence_highlightsSerializer

class centre_of_excellence_titleViewSet(viewsets.ModelViewSet):
    queryset = centre_of_excellence_title.objects.all()
    serializer_class = centre_of_excellence_titleSerializer

class CenterOfExcellenceViewSet(viewsets.ModelViewSet):
    queryset = CenterOfExcellence.objects.all()
    serializer_class = CenterOfExcellenceSerializer

class coe_gallery_titleViewSet(viewsets.ModelViewSet):
    queryset = coe_gallery_title.objects.all()
    serializer_class = coe_gallery_titleSerializer

class coe_galleryViewSet(viewsets.ModelViewSet):
    queryset = coe_gallery.objects.all()
    serializer_class = coe_gallerySerializer

class join_coeViewSet(viewsets.ModelViewSet):
    queryset = join_coe.objects.all()
    serializer_class = join_coeSerializer

class herosection_mouViewSet(viewsets.ModelViewSet):
    queryset = herosection_mou.objects.all()
    serializer_class = herosection_mouSerializer

class mous_statsViewSet(viewsets.ModelViewSet):
    queryset = mous_stats.objects.all()
    serializer_class = mous_statsSerializer

class PartnerInstituteViewSet(viewsets.ModelViewSet):
    queryset = PartnerInstitute.objects.all()
    serializer_class = PartnerInstituteSerializer

class CollaborationProgramViewSet(viewsets.ModelViewSet):
    queryset = CollaborationProgram.objects.all()
    serializer_class = CollaborationProgramSerializer

class UpcomingOpportunityViewSet(viewsets.ModelViewSet):
    queryset = UpcomingOpportunity.objects.all()
    serializer_class = UpcomingOpportunitySerializer

class collaborations_mouViewSet(viewsets.ModelViewSet):
    queryset = collaborations_mou.objects.all()
    serializer_class = collaborations_mouSerializer

class herosection_reportsViewSet(viewsets.ModelViewSet):
    queryset = herosection_reports.objects.all()
    serializer_class = herosection_reportsSerializer

class institutional_reports_statsViewSet(viewsets.ModelViewSet):
    queryset = institutional_reports_stats.objects.all()
    serializer_class = institutional_reports_statsSerializer

class InstitutionalReportViewSet(viewsets.ModelViewSet):
    queryset = InstitutionalReport.objects.all()
    serializer_class = InstitutionalReportSerializer

class School_herosectionViewSet(viewsets.ModelViewSet):
    queryset = School_herosection.objects.all()
    serializer_class = School_herosectionSerializer

class school_statsViewSet(viewsets.ModelViewSet):
    queryset = school_stats.objects.all()
    serializer_class = school_statsSerializer

class technology_schoolsViewSet(viewsets.ModelViewSet):
    queryset = technology_schools.objects.all()
    serializer_class = technology_schoolsSerializer

class explore_academic_excellence_schoolsViewSet(viewsets.ModelViewSet):
    queryset = explore_academic_excellence_schools.objects.all()
    serializer_class = explore_academic_excellence_schoolsSerializer

class school_journeyViewSet(viewsets.ModelViewSet):
    queryset = school_journey.objects.all()
    serializer_class = school_journeySerializer
