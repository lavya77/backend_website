
from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    video = models.FileField(upload_to='videos/') 
    button_text = models.CharField(max_length=100) 
    button_link = models.URLField(null = True)
    def __str__(self):
        return self.title

class QuickAccess(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    icon= models.CharField(max_length=50)
    url = models.URLField(blank=True, null=True)

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='aboutimg/')
    def __str__(self):
        return self.title
class Leadership(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    message = models.TextField()
    photo = models.ImageField(upload_to='leadership/')

    def __str__(self):
        return self.name


class GlanceStat(models.Model):
    label = models.CharField(max_length=100) 
    value = models.CharField(max_length=50)   # e.g., "400+"
    icon = models.CharField(max_length=50)    # Optional (for showing icons with stat)


class NewsandEvents(models.Model):
    title=models.CharField(max_length=20)
    date=models.DateTimeField()
    content_text= models.TextField()
    category=models.CharField(max_length=50 , choices=[('Latest News', 'Latest News'), ('Notices', 'Notices'), ('Academic Events', 'Academic Events')])
    url=models.URLField(blank=True, null=True)  
    def __str__(self):
        return self.title

class Campus_gallery(models.Model):
    image = models.ImageField(upload_to='campusimg/')
    text=models.CharField(max_length=20)

class Excellence_in_Education(models.Model):
    title=models.CharField(max_length=20)
    content_text=models.TextField()
    image = models.ImageField(upload_to='realtedimg/')
    def __str__(self):
        return self.title

class Campus_life(models.Model):
    image = models.ImageField(upload_to='realtedimg/')
    content=models.TextField()
    name=models.CharField(max_length=20)
    course=models.CharField(max_length=20)

class Companies_hiring(models.Model):
    title=models.CharField(max_length=20)
    logo = models.ImageField(upload_to='companies/')
    content_text=models.TextField()
    value = models.CharField(max_length=50) # hiring , alumini , placements

class VirtualExperience(models.Model):
    title = models.CharField(max_length=100)
    video_link = models.URLField()

    def __str__(self):
        return self.title



                
    
        

