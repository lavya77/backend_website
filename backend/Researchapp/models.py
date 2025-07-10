from django.db import models

class coe_heroection(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title

class ResearchHighlight(models.Model):
    values= models.CharField(max_length=255,null=True,blank=True)
    title= models.CharField(max_length=255,null=True,blank=True)
    color =models.CharField(max_length=255,null=True,blank=True)
    icon = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return f"{self.title} - {self.description}"

class Research_techonologies(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name

class ResearchLab(models.Model):
    choices_school=[
        ('Biotechnology','Biotechnology'),
        ('Buddhist Studies and Civilization','Buddhist Studies and Civilization'),
        ('Engineering','Engineering'),
        ('Humanities and Social Sciences','Humanities and Social Sciences'),
        ('Information and Communication Technology','Information and Communication Technology'),
        ('Humanitites and Social Sciences','Humanitites and Social Sciences'),
        ('Law, justice and Governanance','Law, justice and Governanance'),
        ('Management','Management'),
        ('Vocational Studies and Applied Sciences','Vocational Studies and Applied Sciences')
    ]
    title = models.CharField(max_length=255,null=True,blank=True)
    established_year = models.PositiveIntegerField()
    category = models.CharField(max_length=255,null=True,blank=True)
    school = models.CharField(max_length=255,null=True,blank=True,choices=choices_school)
    facilities=models.CharField(max_length=255,null=True,blank=True)
    research_areas=models.ManyToManyField(Research_techonologies)
    head= models.CharField(max_length=255,null=True,blank=True)
    location = models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField(upload_to='labs/', null=True, blank=True)
    button1_text=models.CharField(max_length=255,null=True,blank=True)
    button2_text=models.CharField(max_length=255,null=True,blank=True)
    url1=models.CharField(max_length=255,null=True,blank=True)
    url2=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title

class publications_herosection(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)
    background_image=models.ImageField(upload_to='background/',null=True,blank=True)
    def __str__(self):
        return self.title

class Highlights(models.Model):
    values=models.CharField(max_length=255,null=True,blank=True)
    title=models.CharField(max_length=255,null=True,blank=True)
    color =models.CharField(max_length=255,null=True,blank=True)
    icon = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return f"{self.title} - {self.description}"

class publications(models.Model):
    choices_school=[
        ('Biotechnology','Biotechnology'),
        ('Buddhist Studies and Civilization','Buddhist Studies and Civilization'),
        ('Engineering','Engineering'),
        ('Humanities and Social Sciences','Humanities and Social Sciences'),
        ('Information and Communication Technology','Information and Communication Technology'),
        ('Humanitites and Social Sciences','Humanitites and Social Sciences'),
        ('Law, justice and Governanance','Law, justice and Governanance'),
        ('Management','Management'),
        ('Vocational Studies and Applied Sciences','Vocational Studies and Applied Sciences')
    ]
    school = models.CharField(max_length=255,null=True,blank=True,choices=choices_school)
    category=models.CharField(max_length=255,null=True,blank=True,choices=[
        ("Research Publications","Research Publications"),
        ("Patents","Patents")
    ])
    card_title=models.CharField(max_length=255,null=True,blank=True)
    authors= models.CharField(max_length=255,null=True,blank=True)
    journals=models.CharField(max_length=255,null=True,blank=True)
    year=models.CharField(max_length=255,null=True,blank=True)
    Type=models.CharField(max_length=255,null=True,blank=True,choices=[
        ("Article","Article"),
        ("Thesis","Thesis"),
        ("Review","Review"),
        ("Conderence Paper","Conference Paper"),
        ("Book Chapter","Book Chapter"),
        ("Book","Book"),
        ("Book Review","Book Review"),
        ("Letter","Letter"),
        ("News Clippings","News Clippings"),
        ("Editoriial","Editorial")
    ])
    impact_factor=models.FloatField(default=0.0)
    citations=models.PositiveIntegerField() 
    scopus_id=models.CharField(max_length=255,null=True,blank=True)
    doi=models.CharField(max_length=255,null=True,blank=True)
    issn_ibbn=models.CharField(max_length=255,null=True,blank=True)
    indexing=models.CharField(max_length=255,null=True,blank=True)
    quartile=models.CharField(max_length=255,null=True,blank=True)
    
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
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title

class funded_stats(models.Model):
    values= models.CharField(max_length=255,null=True,blank=True)
    title= models.CharField(max_length=255,null=True,blank=True)
    color = models.CharField(max_length=255,null=True,blank=True)
    icon =models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title

class funded_project_card(models.Model):
    choices_school=[
        ('Biotechnology','Biotechnology'),
        ('Buddhist Studies and Civilization','Buddhist Studies and Civilization'),
        ('Engineering','Engineering'),
        ('Humanities and Social Sciences','Humanities and Social Sciences'),
        ('Information and Communication Technology','Information and Communication Technology'),
        ('Humanitites and Social Sciences','Humanitites and Social Sciences'),
        ('Law, justice and Governanance','Law, justice and Governanance'),
        ('Management','Management'),
        ('Vocational Studies and Applied Sciences','Vocational Studies and Applied Sciences')
    ]
    card_title=models.CharField(max_length=255,null=True,blank=True)
    school = models.CharField(max_length=255,null=True,blank=True,choices=choices_school)
    card_description=models.TextField(null=True)
    principal=models.CharField(max_length=255,null=True,blank=True)
    funding_agency=models.CharField(max_length=255,null=True,blank=True)
    amount=models.CharField(max_length=255,null=True,blank=True)
    duration=models.CharField(max_length=255,null=True,blank=True)
    status=models.CharField(max_length=255,null=True,blank=True,choices=[
        ("Completed","Completed"),
        ("Ongoing","Ongoing")
    ])
    category=models.CharField(max_length=255,null=True,blank=True,choices=[
        ("Climate Research","Climate Research"),
        ("Biotechnology","Biotechnology"),
        ("Energy Systems","Energy Systems")
    ])

    def __str__(self):
        return f'{self.card_title}-{self.school_tag}'
