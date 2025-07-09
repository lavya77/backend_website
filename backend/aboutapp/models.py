from django.db import models

# Create your models here.pyhto
from django.db import models

class HeroSectionAboutUs(models.Model):
    title =models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField()
    background_image=models.CharField(max_length=255,null=True,blank=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title

class Aboutus_Stats(models.Model):
    icon_class=models.CharField(max_length=255,null=True,blank=True)
    value=models.CharField(max_length=255,null=True,blank=True)
    label=models.CharField(max_length=255,null=True,blank=True)
    color=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title
class aboutus_gbu(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    color=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    background_image=models.ImageField(upload_to='about_gbu/',null=True,blank=True)

    def __str__(self):
        return self.title
class about_us_cards(models.Model):
    icon=models.CharField(max_length=255,null=True,blank=True)
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)

    def __str__(self):
        return self.title
class Governance_organizatonal_highlights(models.Model):
    icon=models.CharField(max_length=255,null=True,blank=True)
    title=models.CharField(max_length=255,null=True,blank=True)
    label=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.label

class Academic_school_programs_stats(models.Model):
    icon=models.CharField(max_length=255,null=True,blank=True)
    title=models.CharField(max_length=255,null=True,blank=True)
    label=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.label

class facilities_infrastructure_highlights(models.Model):
    icon=models.CharField(max_length=255,null=True,blank=True)
    title=models.CharField(max_length=255,null=True,blank=True)
    label=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.label

class Hostel_resedential_life(models.Model):
    image=models.ImageField(upload_to='hostel_image/',null=True,blank=True)
    facilities=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.fscilities

class WMeditation_ellness_Feature(models.Model):
    label = models.CharField(max_length=100, help_text="The name of the feature (e.g. Yoga)")
    icon = models.CharField(max_length=20, help_text="Emoji or icon class (e.g. 🧘‍♂️ or fa-yoga)")
    order = models.PositiveIntegerField(default=0, help_text="Custom ordering")

    def __str__(self):
        return f"{self.icon} {self.label}"


class Meditation_wellnes_center(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    features = models.ManyToManyField(WMeditation_ellness_Feature, blank=True)
    button1_text=models.CharField(max_length=255,null=True,blank=True)
    button1_url=models.CharField(max_length=255,null=True,blank=True)
    image=models.ImageField(upload_to='meditation_image/',null=True,blank=True)

    def __str__(self):
        return self.title

class Green_eco_friendly_campus_highlights(models.Model):
    icon=models.CharField(max_length=255,null=True,blank=True)
    label=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.label

class sports_reaction_features(models.Model):
    icon=models.CharField(max_length=255,null=True,blank=True)
    title=models.CharField(max_length=255,null=True,blank=True)
    label=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title

class Sports_Reaction_highlights(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    sub_title=models.CharField(max_length=255,null=True,blank=True)
    feature=models.ManyToManyField(sports_reaction_features,blank=True)

    def __str__(self):
        return self.title

class Research_innovation_highlights(models.Model):
    value=models.CharField(max_length=255,null=True,blank=True)
    label=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.label

class student_life_community_highlights(models.Model):
    icon=models.CharField(max_length=255,null=True,blank=True)
    label=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.label

class aboutus_joingbu(models.Model):
    background_color=models.CharField(max_length=255,null=True,blank=True)
    background_image=models.ImageField(upload_to='join_gbu/',null=True,blank=True)
    title=models.CharField(max_length=255,null=True,blank=True)
    button1_text=models.CharField(max_length=255,null=True,blank=True)
    button2_text=models.CharField(max_length=255,null=True,blank=True)
    button3_text=models.CharField(max_length=255,null=True,blank=True)
    button1_url=models.CharField(max_length=255,null=True,blank=True)
    button2_url=models.CharField(max_length=255,null=True,blank=True)
    button3_url=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title




class ChancellorHeroSection(models.Model):
    background_color = models.CharField(max_length=255,null=True,blank=True)
    background_image=models.ImageField(upload_to='chancellor_background/',blank=True,null=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    sub_title=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title


class ChancellorMessage(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)
    role=models.CharField(max_length=255,null=True,blank=True)
    designation=models.CharField(max_length=255,null=True,blank=True)
    place=models.CharField(max_length=255,null=True,blank=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)
    message=models.TextField(null=True)
    profile_image=models.ImageField(upload_to='chancellors_image',null=True,blank=True)

    def __str__(self):
        return self.name

class ViceChancellorHeroSection(models.Model):
    background_color = models.CharField(max_length=255,null=True,blank=True)
    background_image=models.ImageField(upload_to='chancellor_background/',blank=True,null=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    sub_title=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title


class ViceChancellorMessage(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)
    role=models.CharField(max_length=255,null=True,blank=True)
    designation=models.CharField(max_length=255,null=True,blank=True)
    place=models.CharField(max_length=255,null=True,blank=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)
    message=models.TextField(null=True)
    profile_image=models.ImageField(upload_to='vicechancellors_image',null=True,blank=True)

    def __str__(self):
        return self.name


class Governance_committee_highlights(models.Model):
    profile_photo=models.ImageField(upload_to='profile_image/',null=True,blank=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    designation=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name    

class GovernanceHeroSection(models.Model):
    commitee_category=[
        ('Finance Committee','Finance Committee'),
        ('Executive Council','Executive Council'),
        ('Academic Council','Aacademic Council')
    ]
    highlights=models.ManyToManyField(Governance_committee_highlights,blank=True)
    icon=models.CharField(max_length=255,null=True,blank=True)
    category=models.CharField(max_length=255,null=True,blank=True,choices=commitee_category)

    def __str__(self):
        return self.category

class Governance_organizational_structure(models.Model):
    background_color=models.CharField(max_length=255,null=True,blank=True)
    icon=models.CharField(max_length=255,null=True,blank=True)
    title=models.CharField(max_length=255,null=True,blank=True)
    name=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title

class PoliciesHeroSection(models.Model):
    background_image=models.ImageField(upload_to='policies/',null=True,blank=True)
    background_color = models.CharField(max_length=255,null=True,blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    sub_title=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title or "Policies Hero"


class UniversityPolicy(models.Model):
    category_choices= [
        ('Academic','Academic'),
        ('Resarch','Research'),
        ('Student Affairs','Student Affairs'),
        ('Financial','Financial'),
        ('Admission','Admission')

    ]
    category=models.CharField(max_length=255,null=True,blank=True,choices=category_choices)
    card_title = models.CharField(max_length=255,null=True,blank=True)
    card_desc = models.TextField(null=True)
    year = models.CharField(max_length=255,null=True,blank=True)
    button_text=models.CharField(max_length=255,null=True,blank=True)
    button_url =models.CharField(max_length=255,null=True,blank=True)
    icon_class =models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.card_title or "Policy"


class MandatoryHeroSection(models.Model):
    background_image=models.ImageField(upload_to='policies/',null=True,blank=True)
    background_color = models.CharField(max_length=255,null=True,blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    sub_title=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title  or "Mandatory Disclosure Hero"

class Mandatory_compliance_dashboard(models.Model):
    color=models.CharField(max_length=255,null=True,blank=True)
    value=models.CharField(max_length=255,null=True,blank=True)
    title=models.CharField(max_length=255,null=True,blank=True)
    label=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title

class Mandatory_compliance_items(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    last_updated=models.CharField(max_length=255,null=True,blank=True)
    pdf=models.FileField(upload_to='wellnes_icons',null=True,blank=True)

    def __str__(self):
        return self.title 


class Mandatory_compliance_information_available(models.Model):
    category_information=[
        ('Academic Information','Academic Information'),
        ('Financial Disclosure','Financial Disclosure'),
        ('Faculty Information','Faculty Information'),
        ('Infrastructure Details','Infrastructure Details')
    ]
    information_title=models.CharField(max_length=255,null=True,blank=True,choices=category_information)
    

class Regulatory_compliance_highlights(models.Model):
    icon=models.CharField(max_length=255,null=True,blank=True)
    title=models.CharField(max_length=255,null=True,blank=True)
    label=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title        

