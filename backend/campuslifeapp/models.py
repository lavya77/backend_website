from django.db import models

# Create your models here.
class CampusHero(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=255)
    video_url = models.URLField()
    background_image = models.ImageField(upload_to='campus_hero/')

    def __str__(self):
        return self.title
class VirtualTour(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='virtual_tours/')
    video_link = models.URLField()

    def __str__(self):
        return self.title
class HostelGalleryImage(models.Model):
    image = models.ImageField(upload_to='hostel_gallery/')
    caption = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.caption or "Hostel Image"
class DepartmentBlock(models.Model):
    block_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='department_blocks/')

    def __str__(self):
        return self.block_name
class StudentClub(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='student_clubs/')
    instagram_link = models.URLField(blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name
class LibraryStat(models.Model):
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class SportFacility(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100, help_text="CSS class or icon")
    image = models.ImageField(upload_to='sports_facilities/')

    def __str__(self):
        return self.title
class FoodCourtCategory(models.Model):
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FoodCourtItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(FoodCourtCategory, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='food_courts/')

    def __str__(self):
        return self.name
class EcoCampusStat(models.Model):
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class EcoInitiative(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='eco_initiatives/')

    def __str__(self):
        return self.title
class ImpactStat(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class StudentTestimonial(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    testimonial = models.TextField()
    image = models.ImageField(upload_to='student_testimonials/', blank=True, null=True)

    def __str__(self):
        return self.name
