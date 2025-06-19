from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import QuickAccess , About , Leadership , Banner , GlanceStat ,Campus_gallery ,Excellence_in_Education , Campus_life , Companies_hiring , VirtualExperience
from django.http import JsonResponse

def Banner_views(request):
    queryset = list(Banner.objects.all().values())

    return JsonResponse(queryset,safe=False)
       

def QuickAccess_views(request):
    queryset = list(QuickAccess.objects.all().values())

    return JsonResponse(queryset,safe=False)
       

def About_view(request):
    queryset = list(About.objects.all().values())

    return JsonResponse(queryset,safe=False)

def Leadership_view(request):
    queryset = list(Le.objects.all().values())

    return JsonResponse(queryset,safe=False)    

def GlanceStat_views(request):
    queryset = list(GlanceStat.objects.all().values())

    return JsonResponse(queryset,safe=False)

def Campus_gallery_views(request):
    queryset=list(NewsandEvents.objects.all().values)
    return JsonResponse(queryset,safe=False)

def Excellence_in_Education_views(request):
    queryset=list(NewsandEvents.objects.all().values)
    return JsonResponse(queryset,safe=False)

def Campus_life_views(request):
    queryset=list(NewsandEvents.objects.all().values)
    return JsonResponse(queryset,safe=False)

def Companies_hiring_views(request):
    queryset=list(NewsandEvents.objects.all().values)
    return JsonResponse(queryset,safe=False)

def VirtualExperience_views(request):
    queryset=list(NewsandEvents.objects.all().values)
    return JsonResponse(queryset,safe=False)                

        
       

