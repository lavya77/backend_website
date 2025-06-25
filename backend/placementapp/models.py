from django.db import models

# Create your models here.
class PlacementBrochure(models.Model):
    title = models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    file = models.FileField(upload_to='placement_brochures/')

    def __str__(self):
        return self.title

class stats(models.Model):
    icon_class = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class What_inside(models.Model):
    card_title=models.CharField(max_length=255)
    description=models.TextField()
    background_color=models.CharField(max_length=255)
    icon_clas=models.CharField(max_length=255)
    
    def __str__(self):
        return self.card_title

class BrochureSectionItem(models.Model):
    text = models.CharField(max_length=200)
    year=models.CharField(max_length=255,help_text="2024-2025")
    gradient_background = models.CharField( max_length=255,help_text="Enter a CSS gradient e.g., 'linear-gradient(to right, #ff7e5f, #feb47b)'")
    card_title=models.CharField(max_length=255,help_text="Ready to expore?")
    card_description=models.TextField()
    button_text=models.CharField(max_length=255,help_text="Download full brochure")
    button_url=models.URLField()
    
    def __str__(self):
        return self.text

class InternshipOpportunity(models.Model):
    title = models.CharField(max_length=150)
    description=models.CharField(max_length=255)
    button_text=models.CharField(max_length=255,help_text="apply for internship")
    url=models.URLField()

    def __str__(self):
        return self.title
class companies(models.Model):
    name=models.CharField(max_length=255)
    category=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.name        

class internship_cards(models.Model):
    program_choices=[
        ('summer', 'Summer Internships'),
        ('industrial', 'Industrial Training'),
        ('research', 'Research Internships'),
        ('international', 'International Programs'),
    ]

    eligibility_choices=[
       ('2nd_year', '2nd Year'),
        ('3rd_year', '3rd Year'),
        ('final_year', 'Final Year'),
        ('all_years', 'All Years'),
        ('top_performers', 'Top Performers'),
    ]
    program_type=models.CharField(max_length=255, choices=program_choices,unique=20)
    description=models.TextField()
    durations=models.CharField(max_length=255, help_text="8-12 weeks")
    stipened=models.CharField(max_length=255)
    eligibility=models.CharField(max_length=255,choices=eligibility_choices)
    company=models.ManyToManyField(companies, blank=True)
    application_deadlne=models.CharField(max_length=255, help_text="March 31, 2024")
    button1_text=models.CharField(max_length=255,help_text='Apply now')
    button2_text=models.CharField(max_length=255,help_text="Learn More")
    button1_url=models.URLField()
    button2_url=models.URLField()
    icon_backgroundcolor=models.CharField(max_length=255)
    icon_clas=models.CharField(max_length=255)

    def __str__(self):
        return self.program_type

class Technologies(models.Model):
    name=models.CharField(max_length=255)
     
    def __str__(self):
        return self.name

class internship_providers(models.Model):
    company=models.ManyToManyField(companies,blank=True)   
    interns=models.PositiveIntegerField()
    tech=models.ManyToManyField(Technologies,blank=True)  

    def __str__(self):
        return self.company  

class application_process(models.Model):
    step_number = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_backgroundcolor=models.CharField(max_length=255)

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"

class journey_card(models.Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    button1_text=models.CharField(max_length=255)
    button2_text=models.CharField(max_length=255)
    button1_url=models.URLField()
    button2_url=models.URLField()

    def __str__(self):
        return self.title       

class PlacementStatistic(models.Model):
    title = models.CharField(max_length=200)
    value = models.CharField(max_length=100)  
    description=models.CharField(max_length=255)
    chart_year = models.JSONField(blank=True, null=True)
    chart_sector=models.JSONField(blank=True)
    
    def __str__(self):
        return self.title

class department_stats(models.Model):
    title=models.CharField(max_length=255)
    value=models.CharField(max_length=200)
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.title 

class package_distributons(models.Model):
    packages=models.CharField(max_length=200)
    value=models.CharField(max_length=200)

    def __str__(slef):
        return f'{self.packages}-{self.value}'

class UGPGPlacementStats(models.Model):
    CATEGORY_CHOICES = [
        ("Undergraduate", "Undergraduate"),
        ("Postgraduate", "Postgraduate"),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, unique=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.category} - {self.percentage}%"


class PlacementOfferType(models.Model):
    OFFER_TYPE_CHOICES = [
        ("Domestic", "Domestic Placements"),
        ("International", "International Offers"),
    ]
    offer_type = models.CharField(max_length=20, choices=OFFER_TYPE_CHOICES, unique=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.offer_type} - {self.percentage}%"

class report(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    button_text=models.CharField(max_length=255)
    button1_url=models.URLField()

    def __str__(self):
        return self.title

class training_career(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()

    def __str__(self):
        return self.title        
      
class CareerSupportStat(models.Model):
    value = models.CharField(max_length=50)
    label = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.lable}-{self.value}'

class keytopics_traning(models.Model):
    name=models.CharField(max_length=255,help_text="Quantitative aptitude")

    def __str__(self):
        return self.name

class TrainingProgram(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon_class = models.CharField(max_length=100, blank=True)
    duration=models.CharField(max_length=255,help_text="3 weeks")
    occurence=models.CharField(max_length=255,help_text="3x per week")
    key_topics=models.ManyToManyField(keytopics_traning,blank=True)

    def __str__(self):
        return self.title

class Career_services(models.Model):
    title=models.CharField(max_length=200,help_text="Personalized career counselling")
    description=models.TextField()
    points=models.CharField(max_length=255)

    def __str__(self):
        return self.title

class upcoming_workshops(models.Model):
    levels=[
        ('beginner','Beginner'),
        ('intermediate','Intermediate'),
        ('expert','Expert'),
        ('All levels','All Levels')
    ]

    title=models.CharField(max_length=255)
    date=models.CharField(max_length=255,help_text="December 12,2024")
    duration=models.CharField(max_length=255,help_text="10:00 AM- 4:00PM")
    faculty_name=models.CharField(max_length=255)
    level=models.CharField(max_length=255, choices=levels)
    button1_text=models.CharField(max_length=255)
    button1_url=models.URLField()

    def __str__(self):
        return self.title

class Ready_enhanceskills(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    button1_text=models.CharField(max_length=255)
    button2_text=models.CharField(max_length=255)
    button1_url=models.URLField()
    button2_url=models.URLField()

    def __str__(self):
        return self.title

class esteemed_campus(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()

    def __str__(self):
        return self.title

class recuriments_highlights(models.Model):
    value=models.CharField(max_length=255)
    label=models.CharField(max_length=255)

    def __str__(self):
        return self.label

class RecruiterCompany(models.Model):
    SECTOR_CHOICES = [
        ("IT & Tech", "IT & Tech"),
        ("Core Engineering", "Core Engineering"),
        ("Consulting & Finance", "Consulting & Finance"),
        ("Government & Research", "Government & Research"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    hired_count = models.CharField(max_length=10, help_text="e.g. '32+', '25+'")
    role_types = models.PositiveIntegerField(default=2)
    active_since = models.PositiveIntegerField(default=2024)
    sector = models.CharField(max_length=50, choices=SECTOR_CHOICES)

    def __str__(self):
        return self.name        

class what_recruiters_say(models.Model):
    designation=models.CharField(max_length=255)
    services=models.CharField(max_length=255)
    description=models.TextField
    profile_photo=models.ImageField(upload_to='profile_photo/',blank=True)

    def __str__(self):
        return self.designation