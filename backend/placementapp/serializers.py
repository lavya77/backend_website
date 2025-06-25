from rest_framework import serializers
from .models import (
    PlacementBrochure, stats, What_inside, BrochureSectionItem,
    InternshipOpportunity, companies, internship_cards,
    Technologies, internship_providers, application_process, journey_card,
    PlacementStatistic, department_stats, package_distributons,
    UGPGPlacementStats, PlacementOfferType, report, training_career,
    CareerSupportStat, keytopics_traning, TrainingProgram,
    Career_services, upcoming_workshops, Ready_enhanceskills,
    esteemed_campus, recuriments_highlights, RecruiterCompany,
    what_recruiters_say
)


class PlacementBrochureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacementBrochure
        fields = '__all__'


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = stats
        fields = '__all__'


class WhatInsideSerializer(serializers.ModelSerializer):
    class Meta:
        model = What_inside
        fields = '__all__'


class BrochureSectionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrochureSectionItem
        fields = '__all__'


class InternshipOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = InternshipOpportunity
        fields = '__all__'


class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = companies
        fields = '__all__'


class InternshipCardSerializer(serializers.ModelSerializer):
    company = CompaniesSerializer(many=True, read_only=True)
    company_ids = serializers.PrimaryKeyRelatedField(
        queryset=companies.objects.all(),
        many=True,
        write_only=True,
        source='company'
    )

    class Meta:
        model = internship_cards
        fields = '__all__'


class TechnologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technologies
        fields = '__all__'


class InternshipProvidersSerializer(serializers.ModelSerializer):
    company = CompaniesSerializer(many=True, read_only=True)
    company_ids = serializers.PrimaryKeyRelatedField(
        queryset=companies.objects.all(),
        many=True,
        write_only=True,
        source='company'
    )
    tech = TechnologiesSerializer(many=True, read_only=True)
    tech_ids = serializers.PrimaryKeyRelatedField(
        queryset=Technologies.objects.all(),
        many=True,
        write_only=True,
        source='tech'
    )

    class Meta:
        model = internship_providers
        fields = '__all__'


class ApplicationProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = application_process
        fields = '__all__'


class JourneyCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = journey_card
        fields = '__all__'


class PlacementStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacementStatistic
        fields = '__all__'


class DepartmentStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = department_stats
        fields = '__all__'


class PackageDistributionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = package_distributons
        fields = '__all__'


class UGPGPlacementStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UGPGPlacementStats
        fields = '__all__'


class PlacementOfferTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacementOfferType
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = report
        fields = '__all__'


class TrainingCareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = training_career
        fields = '__all__'


class CareerSupportStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerSupportStat
        fields = '__all__'


class KeyTopicsTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = keytopics_traning
        fields = '__all__'


class TrainingProgramSerializer(serializers.ModelSerializer):
    key_topics = KeyTopicsTrainingSerializer(many=True, read_only=True)
    key_topic_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=keytopics_traning.objects.all(),
        write_only=True,
        source='key_topics'
    )

    class Meta:
        model = TrainingProgram
        fields = '__all__'


class CareerServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career_services
        fields = '__all__'


class UpcomingWorkshopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = upcoming_workshops
        fields = '__all__'


class ReadyEnhanceSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ready_enhanceskills
        fields = '__all__'


class EsteemedCampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = esteemed_campus
        fields = '__all__'


class RecruitmentHighlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = recuriments_highlights
        fields = '__all__'


class RecruiterCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruiterCompany
        fields = '__all__'


class WhatRecruitersSaySerializer(serializers.ModelSerializer):
    class Meta:
        model = what_recruiters_say
        fields = '__all__'
