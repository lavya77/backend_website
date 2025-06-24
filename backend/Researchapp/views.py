from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import (
    coe_heroection, ResearchHighlight, ResearchLab, publications_herosection,
    Highlights, publications, Startups_highlights, Startups, join_startups,
    funded_project, funded_stats, funded_project_card
)

def coe_hero_section_view(request):
    data = list(coe_heroection.objects.all().values())
    return JsonResponse(data, safe=False)

def research_highlights_view(request):
    data = list(ResearchHighlight.objects.all().values())
    return JsonResponse(data, safe=False)

def research_labs_view(request):
    data = list(ResearchLab.objects.all().values())
    return JsonResponse(data, safe=False)

def publications_hero_section_view(request):
    data = list(publications_herosection.objects.all().values())
    return JsonResponse(data, safe=False)

def publication_highlights_view(request):
    data = list(Highlights.objects.all().values())
    return JsonResponse(data, safe=False)

def publication_list_view(request):
    data = list(publications.objects.all().values())
    return JsonResponse(data, safe=False)

def startups_highlight_view(request):
    data = list(Startups_highlights.objects.all().values())
    return JsonResponse(data, safe=False)

def startups_list_view(request):
    data = list(Startups.objects.all().values())
    return JsonResponse(data, safe=False)

def join_startups_view(request):
    data = list(join_startups.objects.all().values())
    return JsonResponse(data, safe=False)

def funded_project_view(request):
    data = list(funded_project.objects.all().values())
    return JsonResponse(data, safe=False)

def funded_stats_view(request):
    data = list(funded_stats.objects.all().values())
    return JsonResponse(data, safe=False)

def funded_project_cards_view(request):
    data = list(funded_project_card.objects.all().values())
    return JsonResponse(data, safe=False)
