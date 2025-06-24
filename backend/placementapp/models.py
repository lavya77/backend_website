from django.db import models

# Create your models here.
class PlacementBrochure(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    file = models.FileField(upload_to='placement_brochures/')

    def __str__(self):
        return f"{self.title} ({self.year})"
class stats(models.Model):
    icon_class = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.label
class BrochureSectionItem(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
class BrochureSectionItem(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
class InternshipOpportunity(models.Model):
    title = models.CharField(max_length=150)
    company_name = models.CharField(max_length=100)
    stipend = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    apply_link = models.URLField()

    def __str__(self):
        return f"{self.title} at {self.company_name}"
class InternshipStep(models.Model):
    step_number = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"
class PlacementStatistic(models.Model):
    label = models.CharField(max_length=200)
    value = models.CharField(max_length=100)  # e.g., "92%", "₹12 LPA"
    chart_data = models.JSONField(blank=True, null=True)  # for bar charts if applicable

    def __str__(self):
        return self.label
class CareerSupportStat(models.Model):
    value = models.CharField(max_length=50)
    label = models.CharField(max_length=200)

    def __str__(self):
        return self.label
class TrainingProgram(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon_class = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
class Workshop(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    registration_link = models.URLField()

    def __str__(self):
        return f"{self.title} on {self.date}"
class Recruiter(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='recruiter_logos/')
    category = models.CharField(max_length=100, blank=True)  # e.g., IT, Core, Startup

    def __str__(self):
        return self.name
class WhyChooseUsPoint(models.Model):
    icon_class = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
