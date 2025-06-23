from django.db import models

class ResearchCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ResearchLab(models.Model):
    title = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=50, blank=True, null=True)
    established_year = models.PositiveIntegerField()
    category = models.ForeignKey(ResearchCategory, on_delete=models.SET_NULL, null=True)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    technologies = models.ManyToManyField(Technology, blank=True)
    head = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='labs/', null=True, blank=True)

    def __str__(self):
        return self.title


class Facility(models.Model):
    name = models.CharField(max_length=100)
    lab = models.ForeignKey(ResearchLab, on_delete=models.CASCADE, related_name='facilities')

    def __str__(self):
        return f"{self.name} - {self.lab.title}"


class ResearchArea(models.Model):
    name = models.CharField(max_length=100)
    lab = models.ForeignKey(ResearchLab, on_delete=models.CASCADE, related_name='research_areas')

    def __str__(self):
        return f"{self.name} - {self.lab.title}"
