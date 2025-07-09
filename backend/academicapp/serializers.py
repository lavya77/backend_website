from rest_framework import serializers
from .models import *

class academicherosection_RegulationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = academicherosection_Regulations
        fields = '__all__'

class acdemic_regulations_statsSerializer(serializers.ModelSerializer):
    class Meta:
        model = acdemic_regulations_stats
        fields = '__all__'

class academic_schedule_regulatioonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = academic_schedule_regulatioons
        fields = '__all__'

class AcademicEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicEvent
        fields = '__all__'

class AcademicRegulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicRegulation
        fields = '__all__'

class academic_StayupdatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = academic_Stayupdated
        fields = '__all__'

class herosection_cbcsSerializer(serializers.ModelSerializer):
    class Meta:
        model = herosection_cbcs
        fields = '__all__'

class cbcs_statsSerializer(serializers.ModelSerializer):
    class Meta:
        model = cbcs_stats
        fields = '__all__'

class what_is_cbcsSerializer(serializers.ModelSerializer):
    class Meta:
        model = what_is_cbcs
        fields = '__all__'

class what_is_cbcs_cardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = what_is_cbcs_cards
        fields = '__all__'

class cbcs_GradingScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = cbcs_GradingScale
        fields = '__all__'

class benefits_cbcbs_titleSerializer(serializers.ModelSerializer):
    class Meta:
        model = benefits_cbcbs_title
        fields = '__all__'

class benefits_cbcbsSerializer(serializers.ModelSerializer):
    class Meta:
        model = benefits_cbcbs
        fields = '__all__'

class Explore_cbcsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Explore_cbcs
        fields = '__all__'

class faculty_directory_herosectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = faculty_directory_herosection
        fields = '__all__'

class Facultydirectory_statsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultydirectory_stats
        fields = '__all__'

class FacultyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyMember
        fields = '__all__'

class faculty_joinSerializer(serializers.ModelSerializer):
    class Meta:
        model = faculty_join
        fields = '__all__'

class herosection_centereofexcellenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = herosection_centereofexcellence
        fields = '__all__'

class centre_of_excellence_highlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = centre_of_excellence_highlights
        fields = '__all__'

class centre_of_excellence_titleSerializer(serializers.ModelSerializer):
    class Meta:
        model = centre_of_excellence_title
        fields = '__all__'

class CenterOfExcellenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CenterOfExcellence
        fields = '__all__'

class coe_gallery_titleSerializer(serializers.ModelSerializer):
    class Meta:
        model = coe_gallery_title
        fields = '__all__'

class coe_gallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = coe_gallery
        fields = '__all__'

class join_coeSerializer(serializers.ModelSerializer):
    class Meta:
        model = join_coe
        fields = '__all__'

class herosection_mouSerializer(serializers.ModelSerializer):
    class Meta:
        model = herosection_mou
        fields = '__all__'

class mous_statsSerializer(serializers.ModelSerializer):
    class Meta:
        model = mous_stats
        fields = '__all__'

class PartnerInstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerInstitute
        fields = '__all__'

class CollaborationProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollaborationProgram
        fields = '__all__'

class UpcomingOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcomingOpportunity
        fields = '__all__'

class collaborations_mouSerializer(serializers.ModelSerializer):
    class Meta:
        model = collaborations_mou
        fields = '__all__'

class herosection_reportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = herosection_reports
        fields = '__all__'

class institutional_reports_statsSerializer(serializers.ModelSerializer):
    class Meta:
        model = institutional_reports_stats
        fields = '__all__'

class InstitutionalReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutionalReport
        fields = '__all__'

class School_herosectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = School_herosection
        fields = '__all__'

class school_statsSerializer(serializers.ModelSerializer):
    class Meta:
        model = school_stats
        fields = '__all__'

class technology_schoolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = technology_schools
        fields = '__all__'

class explore_academic_excellence_schoolsSerializer(serializers.ModelSerializer):
    technology = technology_schoolsSerializer(many=True, read_only=True)
    
    class Meta:
        model = explore_academic_excellence_schools
        fields = '__all__'

class school_journeySerializer(serializers.ModelSerializer):
    class Meta:
        model = school_journey
        fields = '__all__'
