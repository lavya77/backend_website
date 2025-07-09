from rest_framework import serializers
from .models import *

# ResearchArea
class ResearchAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchArea
        fields = '__all__'

# FacultyDirectory
class FacultyDirectorySerializer(serializers.ModelSerializer):
    categories = ResearchAreaSerializer(many=True, read_only=True)
    class Meta:
        model = FacultyDirectory
        fields = '__all__'

# SummaryDashboard
class SummaryDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SummaryDashboard
        fields = '__all__'

# AboutOverview
class AboutOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutOverview
        fields = '__all__'

# OverviewResearch
class OverviewResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverviewResearch
        fields = '__all__'

# OverviewQuickLink
class OverviewQuickLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverviewQuickLink
        fields = '__all__'

# EducationalQualification
class EducationalQualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalQualification
        fields = '__all__'

# ProfessionalExperienceQualification
class ProfessionalExperienceQualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalExperienceQualification
        fields = '__all__'

# Teaching
class TeachingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teaching
        fields = '__all__'

# CourseCode
class CourseCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCode
        fields = '__all__'

# CoursesTaughtTeaching
class CoursesTaughtTeachingSerializer(serializers.ModelSerializer):
    course_code = CourseCodeSerializer(read_only=True)
    class Meta:
        model = CoursesTaughtTeaching
        fields = '__all__'

# LectureSlideTeaching
class LectureSlideTeachingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureSlideTeaching
        fields = '__all__'

# TeachingStat
class TeachingStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachingStat
        fields = '__all__'

# AdministrationRole
class AdministrationRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministrationRole
        fields = '__all__'

# CommitteeMembershipAdministration
class CommitteeMembershipAdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommitteeMembershipAdministration
        fields = '__all__'

# AdministrativeImpact
class AdministrativeImpactSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministrativeImpact
        fields = '__all__'

# ResearchCollaborator
class ResearchCollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchCollaborator
        fields = '__all__'

# ResearchProject
class ResearchProjectSerializer(serializers.ModelSerializer):
    collaborators = ResearchCollaboratorSerializer(many=True, read_only=True)
    class Meta:
        model = ResearchProject
        fields = '__all__'

# ResearchStat
class ResearchStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchStat
        fields = '__all__'

# ResearchGroupOverviewStat
class ResearchGroupOverviewStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchGroupOverviewStat
        fields = '__all__'

# ResearchGroupOverviewDescription
class ResearchGroupOverviewDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchGroupOverviewDescription
        fields = '__all__'

# ResearchCategory
class ResearchCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchCategory
        fields = '__all__'

# ResearchGroupOverview
class ResearchGroupOverviewSerializer(serializers.ModelSerializer):
    title = ResearchCategorySerializer(read_only=True)
    research_area = ResearchAreaSerializer(read_only=True)
    class Meta:
        model = ResearchGroupOverview
        fields = '__all__'

# ResearchAssistant
class ResearchAssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchAssistant
        fields = '__all__'

# publications
class PublicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = publications
        fields = '__all__'

# publication_statistics
class PublicationStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = publication_satistics
        fields = '__all__'

# patent_portfolio_stats
class PatentPortfolioStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = patent_portfolio_stats
        fields = '__all__'

# patent_portfolio_description
class PatentPortfolioDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = patent_portfolio_description
        fields = '__all__'

# Patent_application
class PatentApplicationSerializer(serializers.ModelSerializer):
    inventors = FacultyDirectorySerializer(many=True, read_only=True)
    class Meta:
        model = Patent_application
        fields = '__all__'

# Patent_filing_timeline
class PatentFilingTimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patent_filing_timeline
        fields = '__all__'

# Professional_certifications_status
class ProfessionalCertificationsStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional_certifications_status
        fields = '__all__'

# Professional_certifications_description
class ProfessionalCertificationsDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional_certifications_description
        fields = '__all__'

# Skilss_Certifications
class SkillsCertificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skilss_Certifications
        fields = '__all__'

# Certification_portfolio
class CertificationPortfolioSerializer(serializers.ModelSerializer):
    skills_covered = SkillsCertificationsSerializer(many=True, read_only=True)
    class Meta:
        model = Certification_portfolio
        fields = '__all__'

# Professional_Development_certifications
class ProfessionalDevelopmentCertificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional_Development_certifications
        fields = '__all__'

# invited_talks_stats
class InvitedTalksStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = invited_talks_stats
        fields = '__all__'

# invited_talks_description
class InvitedTalksDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = invited_talks_description
        fields = '__all__'

# Speaking_engagements
class SpeakingEngagementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaking_engagements
        fields = '__all__'

# speaking_expertise
class SpeakingExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = speaking_expertise
        fields = '__all__'

# award_achievements_stats
class AwardAchievementsStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = award_achievements_stats
        fields = '__all__'

# award_achievements_description
class AwardAchievementsDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = award_achievements_description
        fields = '__all__'

# award_recognition
class AwardRecognitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = award_recognition
        fields = '__all__'

# notatble_achievements_award
class NotableAchievementsAwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = notatble_achievements_award
        fields = '__all__'

# Awards_timeline
class AwardsTimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awards_timeline
        fields = '__all__'

# Social_imapcat_stats
class SocialImpactStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social_imapcat_stats
        fields = '__all__'

# Social_impact_description
class SocialImpactDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social_impact_description
        fields = '__all__'

# community_initiative_social
class CommunityInitiativeSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = community_initiative_social
        fields = '__all__'

# social_impact_summary
class SocialImpactSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = social_impact_summary
        fields = '__all__'
