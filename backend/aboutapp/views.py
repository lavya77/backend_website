from django.shortcuts import render
from django.http import JsonResponse
from .models import (
    HeroSectionAboutUs, AboutUsCard, ChancellorHeroSection, ChancellorMessage,
    ViceChancellorHeroSection, ViceChancellorMessage, KnowViceChancellor,
    GovernanceHeroSection, GovernanceCard, PoliciesHeroSection, UniversityPolicy,
    RTI, MandatoryHeroSection, MandatoryBodySection, RegulatoryCompliance
)

def hero_section_view(request):
    queryset = list(HeroSectionAboutUs.objects.all().values())
    return JsonResponse(queryset, safe=False)

def generic_card_view(request):
    queryset = list(AboutUsCard.objects.all().values())
    return JsonResponse(queryset, safe=False)

def timeline_element_view(request):
    queryset = list(ChancellorHeroSection.objects.all().values())
    return JsonResponse(queryset, safe=False)

def tab_section_view(request):
    queryset = list(ChancellorMessage.objects.all().values())
    return JsonResponse(queryset, safe=False)

def image_card_view(request):
    queryset = list(ViceChancellorHeroSection.objects.all().values())
    return JsonResponse(queryset, safe=False)

def progress_bar_view(request):
    queryset = list(ViceChancellorMessage.objects.all().values())
    return JsonResponse(queryset, safe=False)

def document_card_view(request):
    queryset = list(KnowViceChancellor.objects.all().values())
    return JsonResponse(queryset, safe=False)

def global_collaboration_view(request):
    queryset = list(GovernanceHeroSection.objects.all().values())
    return JsonResponse(queryset, safe=False)

def governance_card_view(request):
    queryset = list(GovernanceCard.objects.all().values())
    return JsonResponse(queryset, safe=False)
