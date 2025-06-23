from django.db import models

# Create your models here.pyhto
from django.db import models

class HeroSectionAboutUs(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    button1_text = models.CharField(max_length=50)
    button2_text = models.CharField(max_length=50)
    button1_url = models.URLField()
    button2_url = models.URLField()

    def __str__(self):
        return self.title


class AboutUsCard(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    card_title = models.CharField(max_length=50)
    card_desc = models.TextField()
    background_color = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    card_subtitle = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.card_title


class ChancellorHeroSection(models.Model):
    background_color = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title or "Chancellor Hero Section"


class ChancellorMessage(models.Model):
    name = models.CharField(max_length=50, null=True)
    designation = models.CharField(max_length=50, null=True)
    place = models.CharField(max_length=50, null=True)
    role = models.CharField(max_length=50, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name or "Chancellor Message"


class ViceChancellorHeroSection(models.Model):
    background_color = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title or "VC Hero Section"


class ViceChancellorMessage(models.Model):
    name = models.CharField(max_length=50, null=True)
    place = models.CharField(max_length=50, null=True)
    role = models.CharField(max_length=50, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name or "VC Message"


class KnowViceChancellor(models.Model):
    title = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=255)
    card_title = models.CharField(max_length=100, null=True)
    card_subtitle = models.CharField(max_length=50, null=True, blank=True)
    url = models.URLField(null=True)
    card_description = models.TextField(null=True)
    achievement_title = models.CharField(max_length=50, null=True)
    achievement_subtitle = models.CharField(max_length=50, null=True)
    achievement_description = models.TextField(blank=True)

    def __str__(self):
        return self.title or "Know VC"


class GovernanceHeroSection(models.Model):
    background_color = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True)
    card_title = models.CharField(max_length=120, null=True)
    category = models.CharField(max_length=100, null=True)
    category_icon = models.CharField(max_length=200, null=True)  # Fixed: no hyphens allowed
    name = models.CharField(max_length=50, null=True)
    designation = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title or "Governance Section"


class GovernanceCard(models.Model):
    title = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    background_color = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title or "Governance Card"


class PoliciesHeroSection(models.Model):
    background_color = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title or "Policies Hero"


class UniversityPolicy(models.Model):
    category = models.CharField(max_length=50, null=True)
    card_title = models.CharField(max_length=50, null=True)
    card_desc = models.TextField(null=True)
    year = models.DateField(null=True)
    url = models.URLField(null=True)
    icon_class = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.card_title or "Policy"


class RTI(models.Model):
    card_title = models.CharField(max_length=50, null=True)
    card_desc = models.CharField(max_length=50, null=True)
    icon_class = models.CharField(max_length=50, null=True)
    ques = models.TextField(blank=True)
    button1_text = models.CharField(max_length=50, null=True)
    url = models.URLField(null=True)

    def __str__(self):
        return self.card_title or "RTI Card"


class MandatoryHeroSection(models.Model):
    background_color = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    sub_title = models.CharField(max_length=50, null=True)
    naac_grade = models.CharField(max_length=50, null=True)
    compliance_rate = models.CharField(max_length=50, null=True)
    transparency_index = models.CharField(max_length=50, null=True)
    audit_score = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title or "Mandatory Disclosure Hero"


class MandatoryBodySection(models.Model):  # Fixed: typo in class and `models..Model`
    title = models.CharField(max_length=50, null=True)
    items_available = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=50, null=True)
    card_title = models.CharField(max_length=50, null=True)
    last_updated = models.DateField()
    url = models.URLField()

    def __str__(self):
        return self.card_title or "Mandatory Body"


class RegulatoryCompliance(models.Model):  # Fixed: typo in `mpodels`
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title or "Compliance Entry"
