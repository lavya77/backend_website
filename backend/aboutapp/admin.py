from django.contrib import admin
from .models import (
    HeroSectionAboutUs,
    AboutUsCard,
    ChancellorHeroSection,
    ChancellorMessage,
    ViceChancellorHeroSection,
    ViceChancellorMessage,
    KnowViceChancellor,
    GovernanceHeroSection,
    GovernanceCard,
    PoliciesHeroSection,
    UniversityPolicy,
    RTI,
    MandatoryHeroSection,
    MandatoryBodySection,
    RegulatoryCompliance,
)

admin.site.register(HeroSectionAboutUs)
admin.site.register(AboutUsCard)
admin.site.register(ChancellorHeroSection)
admin.site.register(ChancellorMessage)
admin.site.register(ViceChancellorHeroSection)
admin.site.register(ViceChancellorMessage)
admin.site.register(KnowViceChancellor)
admin.site.register(GovernanceHeroSection)
admin.site.register(GovernanceCard)
admin.site.register(PoliciesHeroSection)
admin.site.register(UniversityPolicy)
admin.site.register(RTI)
admin.site.register(MandatoryHeroSection)
admin.site.register(MandatoryBodySection)
admin.site.register(RegulatoryCompliance)
