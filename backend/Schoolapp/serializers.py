from rest_framework import serializers
from academicapp.models import FacultyMember
from .models import *

# Related Models First
class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'

class CtaegoryLabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ctaegory_lab
        fields = '__all__'

class FacultyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyMember
        fields = '__all__'

class ExpertiseSkillsStudentAchieverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expertise_skills_student_achiever
        fields = '__all__'

# Main Models
class SchoolICTHeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = school_ict_herosection
        fields = '__all__'

class SchoolAboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = school_aboutus
        fields = '__all__'

class StatsSpeakForThemselvesSerializer(serializers.ModelSerializer):
    class Meta:
        model = stats_spaeak_for_themsleves
        fields = '__all__'

class DeanMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = dean_message
        fields = '__all__'

class DepartmentsSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments_school
        fields = '__all__'

class OurProgramsSerializer(serializers.ModelSerializer):
    specializations = SpecializationSerializer(many=True, read_only=True)
    class Meta:
        model = our_prorams
        fields = '__all__'

class FacultyOfICTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty_of_ICt
        fields = '__all__'

class NoticesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notices
        fields = '__all__'

class EventGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_gallery
        fields = '__all__'

class StudentClubsActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = student_clubs_activities
        fields = '__all__'

class PlacementStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement_stats
        fields = '__all__'

class RecentPlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recent_placement
        fields = '__all__'

class RecruitersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiterss
        fields = '__all__'

class StartupStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = startup_stats
        fields = '__all__'

class StudentStartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = student_startup
        fields = '__all__'

class StudentAchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_achievements
        fields = '__all__'

class FacultyHeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = faculty_herosection
        fields = '__all__'

class DepartmentsNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments_name
        fields = '__all__'

class FacultyDepartmentHeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = faculty_department_herosection
        fields = '__all__'

class FacultyProfileSerializer(serializers.ModelSerializer):
    faculty = FacultyMemberSerializer(read_only=True)
    class Meta:
        model = Faculty_profile
        fields = '__all__'

class BoardStudiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board_studies
        fields = '__all__'

class LaboratoryExcellenceSerializer(serializers.ModelSerializer):
    category = CtaegoryLabSerializer(read_only=True)
    class Meta:
        model = Laboratory_Excellence
        fields = '__all__'

class ConferenceActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = conference_activity
        fields = '__all__'

class DepartmentHodMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = department_hod_message
        fields = '__all__'

class DepartmentStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = department_statistics
        fields = '__all__'

class AcademicProgramsDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic_programs_department
        fields = '__all__'

class CurriculumDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum_department
        fields = '__all__'

class ResearchExcellenceDepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research_excellence_departments
        fields = '__all__'

class ResearchExcellenceDepartmentsProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research_excellence_departments_projects
        fields = '__all__'

class ResearchExcellenceDepartmentsStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research_excellence_departments_stats
        fields = '__all__'

class StudentAchieversDepartmentSerializer(serializers.ModelSerializer):
    expertise = ExpertiseSkillsStudentAchieverSerializer(many=True, read_only=True)
    class Meta:
        model = Studnet_achievers_department
        fields = '__all__'

class OurAchievementsDepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Our_achievements_departemnts
        fields = '__all__'
