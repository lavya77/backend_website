from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    coe_heroection, ResearchHighlight, ResearchLab, publications_herosection,
    Highlights, publications, Startups_highlights, Startups, join_startups,
    funded_project, funded_stats, funded_project_card
)

admin.site.register(coe_heroection)
admin.site.register(ResearchHighlight)
admin.site.register(ResearchLab)
admin.site.register(publications_herosection)
admin.site.register(Highlights)
admin.site.register(publications)
admin.site.register(Startups_highlights)
admin.site.register(Startups)
admin.site.register(join_startups)
admin.site.register(funded_project)
admin.site.register(funded_stats)
admin.site.register(funded_project_card)
