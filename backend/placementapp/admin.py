from django.contrib import admin
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

admin.site.register(PlacementBrochure)
admin.site.register(stats)
admin.site.register(What_inside)
admin.site.register(BrochureSectionItem)
admin.site.register(InternshipOpportunity)
admin.site.register(companies)
admin.site.register(internship_cards)
admin.site.register(Technologies)
admin.site.register(internship_providers)
admin.site.register(application_process)
admin.site.register(journey_card)
admin.site.register(PlacementStatistic)
admin.site.register(department_stats)
admin.site.register(package_distributons)
admin.site.register(UGPGPlacementStats)
admin.site.register(PlacementOfferType)
admin.site.register(report)
admin.site.register(training_career)
admin.site.register(CareerSupportStat)
admin.site.register(keytopics_traning)
admin.site.register(TrainingProgram)
admin.site.register(Career_services)
admin.site.register(upcoming_workshops)
admin.site.register(Ready_enhanceskills)
admin.site.register(esteemed_campus)
admin.site.register(recuriments_highlights)
admin.site.register(RecruiterCompany)
admin.site.register(what_recruiters_say)
