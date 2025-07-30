from django.db import models

# Create your models here.
class CampusHero(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    video_url = models.CharField(max_length=255,null=True,blank=True)
    button1_text=models.CharField(max_length=255,null=True,blank=True)
    button2_text=models.CharField(max_length=255,null=True,blank=True)
    button1_url=models.CharField(max_length=255,null=True,blank=True)
    button2_url=models.CharField(max_length=255,null=True,blank=True)
    background_image = models.ImageField(upload_to='campus_hero/',blank=True,null=True)

    def __str__(self):
        return self.title
class VirtualTour(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True)
    thumbnail = models.ImageField(upload_to='virtual_tours/',null=True,blank=True)
    video_link = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title

class key_highlights(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.CharField(max_length=255,null=True,blank=True)
    icon_class=models.CharField(max_length=255,null=True,blank=True)
    button1_text=models.CharField(max_length=255,null=True,blank=True)
    button2_text=models.CharField(max_length=255,null=True,blank=True)
    button1_url=models.CharField(max_length=255,null=True,blank=True)
    button2_url=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title

class campus_life_stats(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    value=models.CharField(max_length=255,null=True,blank=True)
    icon_class=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title      

from django.db import models


class HostelLifeSection(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True)
    background_color = models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Hostel Life Section"


class Hostel(models.Model):
    """Model for hostel cards"""
    name = models.CharField(max_length=255,null=True,blank=True)
    capacity_text = models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField(upload_to='hostel_images/')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class HostelDetail(models.Model):
    """Model for detailed hostel view (like International Students Hostel expanded section)"""
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='detail')
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True)
    amenities_title = models.CharField(max_length=100, null=True ,default="Amenities")
    image = models.ImageField(upload_to='hostel_detail_images/')
    
    # Button 1
    button1_text = models.CharField(max_length=50, default="View Details")
    button1_url =models.CharField(max_length=255,null=True,blank=True)
    # Button 2
    button2_text = models.CharField(max_length=50, default="Book Room")
    button2_url = models.CharField(max_length=255,null=True,blank=True)
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
    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True)
    president_name = models.CharField(max_length=100)
    member_count = models.PositiveIntegerField(default=0)
    contact_email = models.EmailField(null=True)
    cover_image = models.ImageField(upload_to= 'Student_clubs/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    button_text=models.CharField(max_length=255,null=True,blank=True)
    button_url=models.CharField(max_length=255,null=True,blank=True)
    
    
    def __str__(self):
        return self.name


class Activity(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Student club Activites'    

class Achievement(models.Model):
    Student_club = models.ForeignKey('Student_club', on_delete=models.CASCADE, related_name='achievements')
    title =models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True)
    icon =models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Student club Achieveents' 

class Library_gbu(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField()

    def __str__(self):
        return self.title        

class LibraryStat(models.Model):
    label =models.CharField(max_length=255,null=True,blank=True)
    value =models.CharField(max_length=255,null=True,blank=True)
    icon_class=models.CharField(max_length=255)

    def __str__(self):
        return self.label
class LibraryFacility(models.Model):
    name =models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='library/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Library Facilities'
    
    def __str__(self):
        return self.name


class LibraryStats(models.Model):
    label =models.CharField(max_length=255,null=True,blank=True)
    value =models.CharField(max_length=255,null=True,blank=True)
    color =models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Library Statistics'
    
    def __str__(self):
        return f"{self.label}: {self.value}"

class SportsFacility(models.Model):
    """Sports Facilities"""
    name =models.CharField(max_length=255,null=True,blank=True)
    facility_type =models.CharField(max_length=255,null=True,blank=True)
    location =models.CharField(max_length=255,null=True,blank=True)
    capacity = models.CharField(max_length=255,null=True,blank=True)
    access = models.CharField(max_length=255,null=True,blank=True)
    timings =models.CharField(max_length=255,null=True,blank=True)
    contact =models.CharField(max_length=255,null=True,blank=True)
    booking = models.TextField(null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='facilities/', blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Sports Facilities"

    def __str__(self):
        return self.name


class FacilityFeature(models.Model):
    """Facility Features & Amenities"""
    facility = models.ForeignKey(SportsFacility, on_delete=models.CASCADE, related_name='features')
    name = models.CharField(max_length=255,null=True,blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'sports facility'   

class FoodCourtCategory(models.Model):
    title =models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='campus_dining/',blank=True)
    

    def __str__(self):
        return self.title

class FoodCourtItem(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    icon_class = models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField(upload_to='food_courts/',blank=True)

    def __str__(self):
        return self.name
class FoodOutlet(models.Model):
    name =models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True)
    location =models.CharField(max_length=255,null=True,blank=True)
    price_range = models.CharField(max_length=255,null=True,blank=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    review_count = models.PositiveIntegerField(default=0)
    is_open = models.BooleanField(default=True)
    image = models.ImageField(upload_to='outlets/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    button1_text=models.CharField(max_length=255,null=True,blank=True)
    button1_url=models.CharField(max_length=255,null=True,blank=True)
    button2_text=models.CharField(max_length=255,null=True,blank=True)
    button2_url=models.CharField(max_length=255,null=True,blank=True)

    
    def __str__(self):
        return self.name


class Tag(models.Model):
    outlet = models.ForeignKey(FoodOutlet, on_delete=models.CASCADE, related_name='tags')
    name = models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self):
        return f"{self.outlet.name} - {self.name}"
    class Meta:
        verbose_name_plural = 'Food tag'   


class EcoCampusStat(models.Model):
    title =models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True)
    

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'eco campus_titlesection'       


class EcoInitiative_stats(models.Model):
    title =models.CharField(max_length=255,null=True,blank=True)
    value =models.CharField(max_length=255,null=True,blank=True)
    icon_class=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title

class GreenInitiative(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True)
    impact_value =models.CharField(max_length=255,null=True,blank=True)
    impact_label =models.CharField(max_length=255,null=True,blank=True)
    impact_type =models.CharField(max_length=255,null=True,blank=True)
    icon_color = models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField(upload_to='initiatives/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class ImpactStat(models.Model):
    icon = models.CharField(max_length=255,null=True,blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    description=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title
class StudentTestimonial(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    course =models.CharField(max_length=255,null=True,blank=True)
    testimonial = models.TextField(null=True)
    year=models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField(upload_to='student_testimonials/', blank=True, null=True)

    def __str__(self):
        return self.name

class Meditation_herosection(models.Model):
    icon_class=models.CharField(max_length=255,null=True,blank=True)
    title=models.CharField(max_length=255,null=True)
    background_color = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title


class MeditationSession(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    icon_color = models.CharField(max_length=255,null=True,blank=True)
    icon_class=models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class MeditationBenefit(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True)
    color =models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class MeditationTechnique(models.Model):
    name =models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True)
    color = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
     
class Organization(models.Model):
    ORGANIZATION_TYPES = [
        ('nss', 'NSS'),
        ('ncc', 'NCC'),
    ]
    
    name = models.CharField(max_length=10, choices=ORGANIZATION_TYPES)
    full_name =models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True)
    icon_color =models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self):
        return self.get_name_display()
class join_nssandncc(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    button1_text=models.CharField(max_length=255,null=True,blank=True)
    button1_url=models.CharField(max_length=255,null=True,blank=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title
