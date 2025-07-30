from rest_framework import viewsets
from .models import *
from .serializers import *
from academicapp.models import FacultyMember

# Related Models
class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class CtaegoryLabViewSet(viewsets.ModelViewSet):
    queryset = Ctaegory_lab.objects.all()
    serializer_class = CtaegoryLabSerializer

class FacultyMemberViewSet(viewsets.ModelViewSet):
    queryset = FacultyMember.objects.all()
    serializer_class = FacultyMemberSerializer

class ExpertiseSkillsStudentAchieverViewSet(viewsets.ModelViewSet):
    queryset = Expertise_skills_student_achiever.objects.all()
    serializer_class = ExpertiseSkillsStudentAchieverSerializer

# Main Models
class SchoolICTHeroSectionViewSet(viewsets.ModelViewSet):
    queryset = school_ict_herosection.objects.all()
    serializer_class = SchoolICTHeroSectionSerializer

class SchoolAboutUsViewSet(viewsets.ModelViewSet):
    queryset = school_aboutus.objects.all()
    serializer_class = SchoolAboutUsSerializer

class StatsSpeakForThemselvesViewSet(viewsets.ModelViewSet):
    queryset = stats_spaeak_for_themsleves.objects.all()
    serializer_class = StatsSpeakForThemselvesSerializer

class DeanMessageViewSet(viewsets.ModelViewSet):
    queryset = dean_message.objects.all()
    serializer_class = DeanMessageSerializer

class DepartmentsSchoolViewSet(viewsets.ModelViewSet):
    queryset = Departments_school.objects.all()
    serializer_class = DepartmentsSchoolSerializer

class OurProgramsViewSet(viewsets.ModelViewSet):
    queryset = our_prorams.objects.all()
    serializer_class = OurProgramsSerializer

class FacultyOfICTViewSet(viewsets.ModelViewSet):
    queryset = Faculty_of_ICt.objects.all()
    serializer_class = FacultyOfICTSerializer

class NoticesViewSet(viewsets.ModelViewSet):
    queryset = Notices.objects.all()
    serializer_class = NoticesSerializer

class EventGalleryViewSet(viewsets.ModelViewSet):
    queryset = Event_gallery.objects.all()
    serializer_class = EventGallerySerializer

class StudentClubsActivitiesViewSet(viewsets.ModelViewSet):
    queryset = student_clubs_activities.objects.all()
    serializer_class = StudentClubsActivitiesSerializer

class PlacementStatsViewSet(viewsets.ModelViewSet):
    queryset = Placement_stats.objects.all()
    serializer_class = PlacementStatsSerializer

class RecentPlacementViewSet(viewsets.ModelViewSet):
    queryset = Recent_placement.objects.all()
    serializer_class = RecentPlacementSerializer

class RecruitersViewSet(viewsets.ModelViewSet):
    queryset = Recruiterss.objects.all()
    serializer_class = RecruitersSerializer

class StartupStatsViewSet(viewsets.ModelViewSet):
    queryset = startup_stats.objects.all()
    serializer_class = StartupStatsSerializer

class StudentStartupViewSet(viewsets.ModelViewSet):
    queryset = student_startup.objects.all()
    serializer_class = StudentStartupSerializer

class StudentAchievementsViewSet(viewsets.ModelViewSet):
    queryset = Student_achievements.objects.all()
    serializer_class = StudentAchievementsSerializer

class FacultyHeroSectionViewSet(viewsets.ModelViewSet):
    queryset = faculty_herosection.objects.all()
    serializer_class = FacultyHeroSectionSerializer

class DepartmentsNameViewSet(viewsets.ModelViewSet):
    queryset = Departments_name.objects.all()
    serializer_class = DepartmentsNameSerializer

class FacultyDepartmentHeroSectionViewSet(viewsets.ModelViewSet):
    queryset = faculty_department_herosection.objects.all()
    serializer_class = FacultyDepartmentHeroSectionSerializer

class FacultyProfileViewSet(viewsets.ModelViewSet):
    queryset = Faculty_profile.objects.all()
    serializer_class = FacultyProfileSerializer

class BoardStudiesViewSet(viewsets.ModelViewSet):
    queryset = Board_studies.objects.all()
    serializer_class = BoardStudiesSerializer

class LaboratoryExcellenceViewSet(viewsets.ModelViewSet):
    queryset = Laboratory_Excellence.objects.all()
    serializer_class = LaboratoryExcellenceSerializer

class ConferenceActivityViewSet(viewsets.ModelViewSet):
    queryset = conference_activity.objects.all()
    serializer_class = ConferenceActivitySerializer

class DepartmentHodMessageViewSet(viewsets.ModelViewSet):
    queryset = department_hod_message.objects.all()
    serializer_class = DepartmentHodMessageSerializer

class DepartmentStatisticsViewSet(viewsets.ModelViewSet):
    queryset = department_statistics.objects.all()
    serializer_class = DepartmentStatisticsSerializer

class AcademicProgramsDepartmentViewSet(viewsets.ModelViewSet):
    queryset = Academic_programs_department.objects.all()
    serializer_class = AcademicProgramsDepartmentSerializer

class CurriculumDepartmentViewSet(viewsets.ModelViewSet):
    queryset = Curriculum_department.objects.all()
    serializer_class = CurriculumDepartmentSerializer

class ResearchExcellenceDepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Research_excellence_departments.objects.all()
    serializer_class = ResearchExcellenceDepartmentsSerializer

class ResearchExcellenceDepartmentsProjectsViewSet(viewsets.ModelViewSet):
    queryset = Research_excellence_departments_projects.objects.all()
    serializer_class = ResearchExcellenceDepartmentsProjectsSerializer

class ResearchExcellenceDepartmentsStatsViewSet(viewsets.ModelViewSet):
    queryset = Research_excellence_departments_stats.objects.all()
    serializer_class = ResearchExcellenceDepartmentsStatsSerializer

class StudentAchieversDepartmentViewSet(viewsets.ModelViewSet):
    queryset = Studnet_achievers_department.objects.all()
    serializer_class = StudentAchieversDepartmentSerializer

class OurAchievementsDepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Our_achievements_departemnts.objects.all()
    serializer_class = OurAchievementsDepartmentsSerializer
