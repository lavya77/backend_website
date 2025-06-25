from django.db import models

# Create your models here.
class CampusHero(models.Model):
    title = models.CharField(max_length=200)
    description=models.TextField()
    video_url = models.URLField()
    button1_text=models.CharField(max_length=255)
    button2_text=models.CharField(max_length=255)
    button1_url=models.URLField()
    button2_url=models.URLField()
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

class key_highlights(models.Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    icon_class=models.CharField(max_length=255)
    button1_text=models.CharField(max_length=255)
    button2_text=models.CharField(max_length=255)
    button1_url=models.URLField()
    button2_url=models.URLField()

    def __str__(self):
        return self.title

class campus_life_stats(models.Model):
    title=models.CharField(max_length=255)
    value=models.CharField(max_length=255)
    icon_class=models.CharField(max_length=255)

    def __str__(self):
        return self.title      

from django.db import models


class HostelLifeSection(models.Model):
    title = models.CharField(max_length=200, default="Our Hostel Life")
    description = models.TextField()
    background_color = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Hostel Life Section"


class Hostel(models.Model):
    """Model for hostel cards"""
    name = models.CharField(max_length=100)
    capacity_text = models.CharField(max_length=100)  # e.g., "500 Students", "200 Research Scholars"
    image = models.ImageField(upload_to='hostel_images/')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class HostelDetail(models.Model):
    """Model for detailed hostel view (like International Students Hostel expanded section)"""
    hostel = models.OneToOneField(Hostel, on_delete=models.CASCADE, related_name='detail')
    title = models.CharField(max_length=200)
    description = models.TextField()
    amenities_title = models.CharField(max_length=100, default="Amenities")
    image = models.ImageField(upload_to='hostel_detail_images/')
    
    # Button 1
    button1_text = models.CharField(max_length=50, default="View Details")
    button1_url = models.URLField(blank=True, null=True)
    
    # Button 2
    button2_text = models.CharField(max_length=50, default="Book Room")
    button2_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Hostel Detail"


class Amenity(models.Model):
    """Model for amenities list"""
    hostel_detail = models.ForeignKey(HostelDetail, on_delete=models.CASCADE, related_name='amenities')
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Hostel Amenities"

class Student_club(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    president_name = models.CharField(max_length=100)
    member_count = models.PositiveIntegerField(default=0)
    contact_email = models.EmailField()
    cover_image = models.ImageField(upload_to= 'Student_clubs/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    button_text=models.CharField(max_length=255)
    button_url=models.URLField()
    
    
    def __str__(self):
        return self.name


class Activity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Student club Activites'    


class Achievement(models.Model):
    Student = models.ForeignKey( Student_club, on_delete=models.CASCADE, related_name='achievements')
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='🏆')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
class Library_gbu(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()

    def __str__(self):
        return self.title        

class LibraryStat(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    icon_class=models.CharField(max_length=255)

    def __str__(self):
        return self.label
class LibraryFacility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='library/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Library Facilities'
    
    def __str__(self):
        return self.name


class LibraryStats(models.Model):
    label = models.CharField(max_length=50)  # "Books & Resources", "Study Seats", etc.
    value = models.CharField(max_length=20)  # "2M+", "500+", "24/7", "100+"
    color = models.CharField(max_length=20, default='purple')  # purple, blue, etc.
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Library Statistics'
    
    def __str__(self):
        return f"{self.label}: {self.value}"

class SportsFacility(models.Model):
    """Sports Facilities"""
    name = models.CharField(max_length=100)
    facility_type = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    capacity = models.CharField(max_length=50)
    access = models.CharField(max_length=100)
    timings = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    booking = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='facilities/', blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Sports Facilities"

    def __str__(self):
        return self.name


class FacilityFeature(models.Model):
    """Facility Features & Amenities"""
    facility = models.ForeignKey(SportsFacility, on_delete=models.CASCADE, related_name='features')
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'sports facility'   

class FoodCourtCategory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='campus_dining/',blank=True)
    

    def __str__(self):
        return self.title

class FoodCourtItem(models.Model):
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100)
    image = models.ImageField(upload_to='food_courts/',blank=True)

    def __str__(self):
        return self.name
class FoodOutlet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    price_range = models.CharField(max_length=20)  # e.g., "₹50 - ₹200"
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    review_count = models.PositiveIntegerField(default=0)
    is_open = models.BooleanField(default=True)
    image = models.ImageField(upload_to='outlets/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    button1_text=models.CharField(max_length=255)
    button1_url=models.URLField()
    button2_text=models.CharField(max_length=255)
    button2_url=models.URLField()

    
    def __str__(self):
        return self.name


class Tag(models.Model):
    outlet = models.ForeignKey(FoodOutlet, on_delete=models.CASCADE, related_name='tags')
    name = models.CharField(max_length=50,help_text='Popular, Multi-Cuisine, Study Friendly, etc.')  
    
    def __str__(self):
        return f"{self.outlet.name} - {self.name}"
    class Meta:
        verbose_name_plural = 'Food tag'   


class EcoCampusStat(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    

    def __str__(self):
        return self.title


class EcoInitiative_stats(models.Model):
    title = models.CharField(max_length=150)
    value = models.CharField(max_length=20)
    icon_class=models.CharField(max_length=255)

    def __str__(self):
        return self.title

class GreenInitiative(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    impact_value = models.CharField(max_length=50)  # e.g., "80%", "50,000L", "90%", "50+"
    impact_label = models.CharField(max_length=100)  # e.g., "Renewable Energy", "Daily Collection"
    impact_type = models.CharField(max_length=50)  # "Impact Measurement"
    icon_color = models.CharField(max_length=20, default='orange')  # orange, blue, green
    image = models.ImageField(upload_to='initiatives/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class ImpactStat(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description=models.CharField(max_length=255)

    def __str__(self):
        return self.title
class StudentTestimonial(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    testimonial = models.TextField()
    year=models.CharField(max_length=255,help_text="final year or second year")
    image = models.ImageField(upload_to='student_testimonials/', blank=True, null=True)

    def __str__(self):
        return self.name

class Meditation_herosection(models.Model):
    icon_class=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    description = models.TextField()
    background_color = models.CharField(max_length=200) 

    def __str__(self):
        return self.title


class MeditationSession(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    icon_color = models.CharField(max_length=20, default='green')
    icon_class=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class MeditationBenefit(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    color = models.CharField(max_length=20, default='green')  # green, blue, purple
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class MeditationTechnique(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    color = models.CharField(max_length=20, default='green')  # green, blue, purple, orange
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
     
class Organization(models.Model):
    ORGANIZATION_TYPES = [
        ('nss', 'NSS'),
        ('ncc', 'NCC'),
    ]
    
    name = models.CharField(max_length=10, choices=ORGANIZATION_TYPES)
    full_name = models.CharField(max_length=100)
    description = models.TextField()
    icon_color = models.CharField(max_length=20, default='blue')
    
    def __str__(self):
        return self.get_name_display()
class join_nssandncc(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    button1_text=models.CharField(max_length=255)
    button1_url=models.URLField()
    background_color=models.CharField(max_length=255)

    def __str__(self):
        return self.title