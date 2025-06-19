from django.contrib import admin
from .models import (
    HeroSection, GenericCard, TimelineElement, TabSection, ImageCard,
    ProgressBar, DocumentCard, GlobalCollaborationCard, GovernanceCard
)

admin.site.register(HeroSection)
admin.site.register(GenericCard)
admin.site.register(TimelineElement)
admin.site.register(TabSection)
admin.site.register(ImageCard)
admin.site.register(ProgressBar)
admin.site.register(DocumentCard)
admin.site.register(GlobalCollaborationCard)
admin.site.register(GovernanceCard)
