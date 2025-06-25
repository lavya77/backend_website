from rest_framework import viewsets
from .models import *
from .serializers import *

class PlacementBrochureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PlacementBrochure.objects.all()
    serializer_class = PlacementBrochureSerializer

class StatsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = stats.objects.all()
    serializer_class = StatsSerializer

class WhatInsideViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = What_inside.objects.all()
    serializer_class = WhatInsideSerializer

class BrochureSectionItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BrochureSectionItem.objects.all()
    serializer_class = BrochureSectionItemSerializer

class InternshipOpportunityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InternshipOpportunity.objects.all()
    serializer_class = InternshipOpportunitySerializer

class CompaniesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = companies.objects.all()
    serializer_class = CompaniesSerializer

class InternshipCardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = internship_cards.objects.all()
    serializer_class = InternshipCardSerializer

class InternshipProvidersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = internship_providers.objects.all()
    serializer_class = InternshipProvidersSerializer

class ApplicationProcessViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = application_process.objects.all()
    serializer_class = ApplicationProcessSerializer

class JourneyCardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = journey_card.objects.all()
    serializer_class = JourneyCardSerializer

class PlacementStatisticViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PlacementStatistic.objects.all()
    serializer_class = PlacementStatisticSerializer

class DepartmentStatsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = department_stats.objects.all()
    serializer_class = DepartmentStatsSerializer

class PackageDistributionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = package_distributons.objects.all()
    serializer_class = PackageDistributionsSerializer

class UGPGPlacementStatsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UGPGPlacementStats.objects.all()
    serializer_class = UGPGPlacementStatsSerializer

class PlacementOfferTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PlacementOfferType.objects.all()
    serializer_class = PlacementOfferTypeSerializer

class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = report.objects.all()
    serializer_class = ReportSerializer

class TrainingCareerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = training_career.objects.all()
    serializer_class = TrainingCareerSerializer

class CareerSupportStatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CareerSupportStat.objects.all()
    serializer_class = CareerSupportStatSerializer

class KeyTopicsTrainingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = keytopics_traning.objects.all()
    serializer_class = KeyTopicsTrainingSerializer

class TrainingProgramViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TrainingProgram.objects.all()
    serializer_class = TrainingProgramSerializer

class CareerServicesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Career_services.objects.all()
    serializer_class = CareerServicesSerializer

class UpcomingWorkshopsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = upcoming_workshops.objects.all()
    serializer_class = UpcomingWorkshopsSerializer

class ReadyEnhanceSkillsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ready_enhanceskills.objects.all()
    serializer_class = ReadyEnhanceSkillsSerializer

class EsteemedCampusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = esteemed_campus.objects.all()
    serializer_class = EsteemedCampusSerializer

class RecruitmentHighlightsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = recuriments_highlights.objects.all()
    serializer_class = RecruitmentHighlightsSerializer

class RecruiterCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RecruiterCompany.objects.all()
    serializer_class = RecruiterCompanySerializer

class WhatRecruitersSayViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = what_recruiters_say.objects.all()
    serializer_class = WhatRecruitersSaySerializer
