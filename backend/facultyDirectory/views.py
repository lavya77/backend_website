from rest_framework import viewsets
from .models import *
from .serializers import *

# For each model, define a ModelViewSet

class ResearchAreaViewSet(viewsets.ModelViewSet):
    queryset = ResearchArea.objects.all()
    serializer_class = ResearchAreaSerializer

class FacultyDirectoryViewSet(viewsets.ModelViewSet):
    queryset = FacultyDirectory.objects.all()
    serializer_class = FacultyDirectorySerializer

class SummaryDashboardViewSet(viewsets.ModelViewSet):
    queryset = SummaryDashboard.objects.all()
    serializer_class = SummaryDashboardSerializer

class AboutOverviewViewSet(viewsets.ModelViewSet):
    queryset = AboutOverview.objects.all()
    serializer_class = AboutOverviewSerializer

class OverviewResearchViewSet(viewsets.ModelViewSet):
    queryset = OverviewResearch.objects.all()
    serializer_class = OverviewResearchSerializer

class OverviewQuickLinkViewSet(viewsets.ModelViewSet):
    queryset = OverviewQuickLink.objects.all()
    serializer_class = OverviewQuickLinkSerializer

class EducationalQualificationViewSet(viewsets.ModelViewSet):
    queryset = EducationalQualification.objects.all()
    serializer_class = EducationalQualificationSerializer

class ProfessionalExperienceQualificationViewSet(viewsets.ModelViewSet):
    queryset = ProfessionalExperienceQualification.objects.all()
    serializer_class = ProfessionalExperienceQualificationSerializer

class TeachingViewSet(viewsets.ModelViewSet):
    queryset = Teaching.objects.all()
    serializer_class = TeachingSerializer

class CourseCodeViewSet(viewsets.ModelViewSet):
    queryset = CourseCode.objects.all()
    serializer_class = CourseCodeSerializer

class CoursesTaughtTeachingViewSet(viewsets.ModelViewSet):
    queryset = CoursesTaughtTeaching.objects.all()
    serializer_class = CoursesTaughtTeachingSerializer

class LectureSlideTeachingViewSet(viewsets.ModelViewSet):
    queryset = LectureSlideTeaching.objects.all()
    serializer_class = LectureSlideTeachingSerializer

class TeachingStatViewSet(viewsets.ModelViewSet):
    queryset = TeachingStat.objects.all()
    serializer_class = TeachingStatSerializer

class AdministrationRoleViewSet(viewsets.ModelViewSet):
    queryset = AdministrationRole.objects.all()
    serializer_class = AdministrationRoleSerializer

class CommitteeMembershipAdministrationViewSet(viewsets.ModelViewSet):
    queryset = CommitteeMembershipAdministration.objects.all()
    serializer_class = CommitteeMembershipAdministrationSerializer

class AdministrativeImpactViewSet(viewsets.ModelViewSet):
    queryset = AdministrativeImpact.objects.all()
    serializer_class = AdministrativeImpactSerializer

class ResearchCollaboratorViewSet(viewsets.ModelViewSet):
    queryset = ResearchCollaborator.objects.all()
    serializer_class = ResearchCollaboratorSerializer

class ResearchProjectViewSet(viewsets.ModelViewSet):
    queryset = ResearchProject.objects.all()
    serializer_class = ResearchProjectSerializer

class ResearchStatViewSet(viewsets.ModelViewSet):
    queryset = ResearchStat.objects.all()
    serializer_class = ResearchStatSerializer

class ResearchGroupOverviewStatViewSet(viewsets.ModelViewSet):
    queryset = ResearchGroupOverviewStat.objects.all()
    serializer_class = ResearchGroupOverviewStatSerializer

class ResearchGroupOverviewDescriptionViewSet(viewsets.ModelViewSet):
    queryset = ResearchGroupOverviewDescription.objects.all()
    serializer_class = ResearchGroupOverviewDescriptionSerializer

class ResearchCategoryViewSet(viewsets.ModelViewSet):
    queryset = ResearchCategory.objects.all()
    serializer_class = ResearchCategorySerializer

class ResearchGroupOverviewViewSet(viewsets.ModelViewSet):
    queryset = ResearchGroupOverview.objects.all()
    serializer_class = ResearchGroupOverviewSerializer

class ResearchAssistantViewSet(viewsets.ModelViewSet):
    queryset = ResearchAssistant.objects.all()
    serializer_class = ResearchAssistantSerializer

class PublicationsViewSet(viewsets.ModelViewSet):
    queryset = publications.objects.all()
    serializer_class = PublicationsSerializer

class PublicationStatisticsViewSet(viewsets.ModelViewSet):
    queryset = publication_satistics.objects.all()
    serializer_class = PublicationStatisticsSerializer

class PatentPortfolioStatsViewSet(viewsets.ModelViewSet):
    queryset = patent_portfolio_stats.objects.all()
    serializer_class = PatentPortfolioStatsSerializer

class PatentPortfolioDescriptionViewSet(viewsets.ModelViewSet):
    queryset = patent_portfolio_description.objects.all()
    serializer_class = PatentPortfolioDescriptionSerializer

class PatentApplicationViewSet(viewsets.ModelViewSet):
    queryset = Patent_application.objects.all()
    serializer_class = PatentApplicationSerializer

class PatentFilingTimelineViewSet(viewsets.ModelViewSet):
    queryset = Patent_filing_timeline.objects.all()
    serializer_class = PatentFilingTimelineSerializer

class ProfessionalCertificationsStatusViewSet(viewsets.ModelViewSet):
    queryset = Professional_certifications_status.objects.all()
    serializer_class = ProfessionalCertificationsStatusSerializer

class ProfessionalCertificationsDescriptionViewSet(viewsets.ModelViewSet):
    queryset = Professional_certifications_description.objects.all()
    serializer_class = ProfessionalCertificationsDescriptionSerializer

class SkillsCertificationsViewSet(viewsets.ModelViewSet):
    queryset = Skilss_Certifications.objects.all()
    serializer_class = SkillsCertificationsSerializer

class CertificationPortfolioViewSet(viewsets.ModelViewSet):
    queryset = Certification_portfolio.objects.all()
    serializer_class = CertificationPortfolioSerializer

class ProfessionalDevelopmentCertificationsViewSet(viewsets.ModelViewSet):
    queryset = Professional_Development_certifications.objects.all()
    serializer_class = ProfessionalDevelopmentCertificationsSerializer

class InvitedTalksStatsViewSet(viewsets.ModelViewSet):
    queryset = invited_talks_stats.objects.all()
    serializer_class = InvitedTalksStatsSerializer

class InvitedTalksDescriptionViewSet(viewsets.ModelViewSet):
    queryset = invited_talks_description.objects.all()
    serializer_class = InvitedTalksDescriptionSerializer

class SpeakingEngagementsViewSet(viewsets.ModelViewSet):
    queryset = Speaking_engagements.objects.all()
    serializer_class = SpeakingEngagementsSerializer

class SpeakingExpertiseViewSet(viewsets.ModelViewSet):
    queryset = speaking_expertise.objects.all()
    serializer_class = SpeakingExpertiseSerializer

class AwardAchievementsStatsViewSet(viewsets.ModelViewSet):
    queryset = award_achievements_stats.objects.all()
    serializer_class = AwardAchievementsStatsSerializer

class AwardAchievementsDescriptionViewSet(viewsets.ModelViewSet):
    queryset = award_achievements_description.objects.all()
    serializer_class = AwardAchievementsDescriptionSerializer

class AwardRecognitionViewSet(viewsets.ModelViewSet):
    queryset = award_recognition.objects.all()
    serializer_class = AwardRecognitionSerializer

class NotableAchievementsAwardViewSet(viewsets.ModelViewSet):
    queryset = notatble_achievements_award.objects.all()
    serializer_class = NotableAchievementsAwardSerializer

class AwardsTimelineViewSet(viewsets.ModelViewSet):
    queryset = Awards_timeline.objects.all()
    serializer_class = AwardsTimelineSerializer

class SocialImpactStatsViewSet(viewsets.ModelViewSet):
    queryset = Social_imapcat_stats.objects.all()
    serializer_class = SocialImpactStatsSerializer

class SocialImpactDescriptionViewSet(viewsets.ModelViewSet):
    queryset = Social_impact_description.objects.all()
    serializer_class = SocialImpactDescriptionSerializer

class CommunityInitiativeSocialViewSet(viewsets.ModelViewSet):
    queryset = community_initiative_social.objects.all()
    serializer_class = CommunityInitiativeSocialSerializer

class SocialImpactSummaryViewSet(viewsets.ModelViewSet):
    queryset = social_impact_summary.objects.all()
    serializer_class = SocialImpactSummarySerializer
