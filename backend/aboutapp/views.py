from django.shortcuts import render
from django.http import JsonResponse
from .models import (
    HeroSection, GenericCard, TimelineElement, TabSection, ImageCard,
    ProgressBar, DocumentCard, GlobalCollaborationCard, GovernanceCard
)

def hero_section_view(request):
    queryset = list(HeroSection.objects.all().values())
    return JsonResponse(queryset, safe=False)

def generic_card_view(request):
    queryset = list(GenericCard.objects.all().values())
    return JsonResponse(queryset, safe=False)

def timeline_element_view(request):
    queryset = list(TimelineElement.objects.all().values())
    return JsonResponse(queryset, safe=False)

def tab_section_view(request):
    queryset = list(TabSection.objects.all().values())
    return JsonResponse(queryset, safe=False)

def image_card_view(request):
    queryset = list(ImageCard.objects.all().values())
    return JsonResponse(queryset, safe=False)

def progress_bar_view(request):
    queryset = list(ProgressBar.objects.all().values())
    return JsonResponse(queryset, safe=False)

def document_card_view(request):
    queryset = list(DocumentCard.objects.all().values())
    return JsonResponse(queryset, safe=False)

def global_collaboration_view(request):
    queryset = list(GlobalCollaborationCard.objects.all().values())
    return JsonResponse(queryset, safe=False)

def governance_card_view(request):
    queryset = list(GovernanceCard.objects.all().values())
    return JsonResponse(queryset, safe=False)
