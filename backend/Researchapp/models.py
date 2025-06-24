from django.db import models

class coe_heroection(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    background_color=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class ResearchHighlight(models.Model):
    values= models.CharField(max_length=100, help_text="e.g., 20+")
    title= models.CharField(max_length=100, help_text="e.g., Research Centers")
    color = models.CharField(max_length=20, help_text="Hex or Tailwind color name, e.g., 'blue', 'green'")
    icon = models.CharField(max_length=50, null=True, blank=True, help_text="Optional: icon class if needed")

    def __str__(self):
        return f"{self.title} - {self.description}"

class ResearchLab(models.Model):
    title = models.CharField(max_length=255)
    established_year = models.PositiveIntegerField()
    category = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    technologies = models.CharField(max_length=255)
    facilities=models.CharField(max_length=255)
    research_areas=models.CharField(max_length=255)
    head = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='labs/', null=True, blank=True)
    button1_text=models.CharField(max_length=255)
    button2_text=models.CharField(max_length=255)
    url1=models.URLField()
    url2=models.URLField()

    def __str__(self):
        return self.title

class publications_herosection(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.title
class Highlights(models.Model):
    values= models.CharField(max_length=100, help_text="e.g., 20+")
    title= models.CharField(max_length=100, help_text="e.g., Research Centers")
    color = models.CharField(max_length=20, help_text="Hex or Tailwind color name, e.g., 'blue', 'green'")
    icon = models.CharField(max_length=50, null=True, blank=True, help_text="Optional: icon class if needed")

    def __str__(self):
        return f"{self.title} - {self.description}"

class publications(models.Model):
    category=models.CharField(max_length=255,help_text="research publicatons or patents")
    card_title=models.CharField(max_length=255)
    authors= models.CharField(max_length=255)
    journals=models.CharField(max_length=255)
    year=models.PositiveIntegerField()
    Type=models.CharField(max_length=255)
    impact_factor=models.DecimalField(max_digits=5, decimal_places=5)
    citations=models.PositiveIntegerField() 
    scopus_id=models.CharField(max_length=255)
    doi=models.CharField(max_length=255)
    issn_ibbn=models.CharField(max_length=255)
    indexing=models.CharField(max_length=255)
    quartile=models.CharField(max_length=255)
    
    def __str__(self):
        return self.card_title

class Startups_highlights(models.Model):
    values= models.CharField(max_length=100, help_text="e.g., 20+")
    title= models.CharField(max_length=100)
    color = models.CharField(max_length=20, help_text="Hex or Tailwind color name, e.g., 'blue', 'green'")
    icon = models.CharField(max_length=50, null=True, blank=True, help_text="Optional: icon class if needed")

    def __str__(self):
        return self.title  

class Startups(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    card_title=models.CharField()
    card_description=models.TextField()
    card_icon=models.CharField(max_length=200)
    background_color=models.CharField(max_length=255)
    slider_image=models.ImageField(upload_to='startupimg/', null=True, blank=True)
    

    def __str__(self):
        return f"{self.title} - {self.description}"     

class join_startups(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    values= models.CharField(max_length=100, help_text="e.g 1 , 2 ,3")
    stats_title= models.CharField(max_length=100,)
    stats_description = models.CharField(max_length=50, null=True, blank=True)
    icon_color = models.CharField(max_length=20, help_text="Hex or Tailwind color name, e.g., 'blue', 'green'")
    

    def __str__(self):
        return f"{self.title} - {self.description}"     

class funded_project(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()

    def __str__(self):
        return self.title

class funded_stats(models.Model):
    values= models.CharField(max_length=100, help_text="e.g., 20+")
    title= models.CharField(max_length=100)
    color = models.CharField(max_length=20, help_text="Hex or Tailwind color name, e.g., 'blue', 'green'")
    icon = models.CharField(max_length=50, null=True, blank=True, help_text="Optional: icon class if needed")

    def __str__(self):
        return self.title

class funded_project_card(models.Model):
    card_title=models.CharField(max_length=255)
    school_tag=models.CharField(max_length=255,help_text="engeineering or biotechnology")
    card_description=models.TextField()
    principal=models.CharField(max_length=255)
    funding_agency=models.CharField(max_length=255)
    amount=models.CharField(max_length=255,help_text="45.2 lakhs")
    duration=models.CharField(max_length=255,help_text="3 years(2022-2025)")
    status=models.CharField(max_length=255)
    category=models.CharField(max_length=255)

    def __str__(self):
        return f'{self.card_title}-{self.school_tag}'
