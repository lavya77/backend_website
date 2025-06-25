from django.db import models


class JoinOurAlumni(models.Model):
    """Model for Join Our Alumni banner section"""
    background_color = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Join Our Alumni Banner"
        verbose_name_plural = "Join Our Alumni Banners"


class Branch(models.Model):
    """Model for academic branches/majors"""
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Branches"


class AlumniProfile(models.Model):
    """Main model for alumni registration"""
    
    # Personal Information
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    current_location = models.CharField(max_length=200, blank=True, null=True)
    
    # Academic Information
    graduation_year = models.IntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    degree_certificate = models.FileField(upload_to='certificates/', blank=True, null=True)
    
    # Professional Information
    current_job_title = models.CharField(max_length=200, blank=True, null=True)
    current_company = models.CharField(max_length=200, blank=True, null=True)
    linkedin_profile_url = models.URLField(blank=True, null=True)
    professional_bio = models.TextField(blank=True, null=True)
    
    # Help preferences
    available_for_job_referrals = models.BooleanField(default=False)
    available_for_resume_reviews = models.BooleanField(default=False)
    available_for_career_mentoring = models.BooleanField(default=False)
    
    # Dynamic button
    button1_text = models.CharField(max_length=200, default="Submit Registration")
    button1_url = models.URLField(blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.full_name} ({self.graduation_year})"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Alumni Profile"
        verbose_name_plural = "Alumni Profiles"