from django.db import models

# Create your models here.
class admission_process(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    sub_title =models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

class step_process(models.Model):
    step_title=models.CharField(max_length=255)
    step_description=models.CharField(max_length=255)
    duration=models.CharField(max_length=255)
    icon_clas=models.CharField(max_length=255,null=True)
    status=models.CharField(max_length=255,help_text="current or upcoming")

    def __str__(self):
        return sefl.step_title

class ImportantDate(models.Model):
    EVENT_STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('upcoming', 'Upcoming'),
    ]

    event_name = models.CharField(max_length=100)
    event_date = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=EVENT_STATUS_CHOICES, default='upcoming')
    icon_class = models.CharField(
        max_length=100,
        default='fa fa-calendar',
        help_text="CSS class for icon, e.g., 'fa fa-calendar-check'"
    )

    def __str__(self):
        return f"{self.event_name} - {self.event_date}"


class RequiredDocument(models.Model):
    name = models.CharField(max_length=200)
    is_required = models.BooleanField(default=True)
    icon_class = models.CharField(
        max_length=100,
        default='fa fa-check-circle',
        help_text="CSS class for icon, e.g., 'fa fa-id-card'"
    )

    def __str__(self):
        return self.name


class ActionButton(models.Model):
    button_text = models.CharField(max_length=100)  # e.g., "Start Application"
    url = models.URLField(help_text="Target URL or file download link")
    icon_class = models.CharField(
        max_length=100,
        blank=True,
        help_text="CSS class for button icon, e.g., 'fa fa-download'"
    )

    def __str__(self):
        return self.button_text

class Courses_offered(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()

    def __str__(self):
        return self.title
class stats_coursesoffered(models.Model):
    values= models.CharField(max_length=100, help_text="e.g., 20+")
    title= models.CharField(max_length=100, help_text="e.g., Schools, programs")
    color = models.CharField(max_length=20, help_text="Hex or Tailwind color name, e.g., 'blue', 'green'")
    icon = models.CharField(max_length=50, null=True, blank=True, help_text="Optional: icon class if needed")

    def __str__(self):
        return self.title

class schools_coursesoffered(models.Model):
    school_name=models.CharField(max_length=255)
    image = models.ImageField(upload_to='school_images/', null=True, blank=True)
    
    def __str__(self):
        return self.school_name

class courses_coursesoffered(models.Model):
    graduate_category=models.CharField(max_length=255,help_text="undergraduate or postgraduate")
    card_title=models.CharField(max_length=255)
    specialisation=models.CharField(max_length=255)
    seats=models.PositiveIntegerField(max_length=255)
    year=models.PositiveIntegerField(max_length=255)
    eligibility=models.CharField(max_length=255)
    Highlights=models.TextField()

    def __str__(self):
        return self.card_title

class ready_to_apply_coussesoffered(models.Model):
    title=models.CharField(max_length=255)
    background_color=models.CharField(max_length=255)
    description=models.TextField()
    button_text=models.CharField(max_length=255)
    button_url=models.URLField()

    def __str__(self):
        return self.button_text

class eligibility_rservation(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    notice_title=models.CharField(max_length=255,null=True)
    notice_description=models.TextField(null=True)
    notice_backgroundcolor=models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.title
class programs_eligibility(models.Model):
    category=models.CharField(max_length=255,help_text="elegibility criteria or reservation policy") 
    PROGRAM_LEVEL_CHOICES = [
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
    ]

    name = models.CharField(max_length=50)  # e.g., B.Tech, MBA
    level = models.CharField(max_length=2, choices=PROGRAM_LEVEL_CHOICES)
    academic_qualification = models.TextField()
    entrance_exam = models.CharField(max_length=200)
    age_limit = models.CharField(
        max_length=100,
        help_text="Example: 'Born on or after October 1, 1999' or 'No age limit'"
    )
    general_eligibility_percent = models.DecimalField(
        max_digits=5, decimal_places=2,
        help_text="General category minimum percentage"
    )
    reserved_eligibility_percent = models.DecimalField(
        max_digits=5, decimal_places=2,
        help_text="Reserved category minimum percentage"
    )

    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"       

class Fee_structure(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    fee_policy=models.TextField()
    icon_feepolicy=models.CharField(max_length=255,null=True)
    color_fee=models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Program_Feestructure(models.Model):
    PROGRAM_LEVEL_CHOICES = [
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
    ]

    program_name = models.CharField(max_length=50)  # e.g., B.Tech, MBA
    level = models.CharField(max_length=2, choices=PROGRAM_LEVEL_CHOICES)
    
    yearly_fee = models.PositiveIntegerField(help_text="Total fee per year (INR)")
    total_fee = models.PositiveIntegerField(help_text="Total fee for entire duration (INR)")

    tuition_fee = models.PositiveIntegerField(default=0)
    hostel_fee = models.PositiveIntegerField(default=0)
    mess_fee = models.PositiveIntegerField(default=0)
    other_fee = models.PositiveIntegerField(default=0)

    scholarship_info = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="e.g., 'Merit-based scholarships available'"
    )

    def __str__(self):
        return f"{self.program_name} ({self.get_level_display()})"

class international_admissions(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()

    def __str__(self):
        return self.title

class stats_international(models.Model):
    values= models.CharField(max_length=100, help_text="e.g., 20+")
    title= models.CharField(max_length=100, help_text="e.g., Schools, programs")
    color = models.CharField(max_length=20, help_text="Hex or Tailwind color name, e.g., 'blue', 'green'")
    icon = models.CharField(max_length=50, null=True, blank=True, help_text="Optional: icon class if needed")

    def __str__(self):
        return self.title

class AdmissionTab_international(models.Model):
    title = models.CharField(max_length=100)
    anchor_id = models.CharField(max_length=100, help_text="HTML ID for scrolling")

    def __str__(self):
        return self.title


class EligibilityRequirement_interanational(models.Model):
    PROGRAM_LEVEL_CHOICES = [
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
        ('PhD', 'Doctoral'),
    ]

    level = models.CharField(max_length=5, choices=PROGRAM_LEVEL_CHOICES)
    academic_requirement = models.TextField()
    english_proficiency = models.TextField()
    additional_requirements = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_level_display()} Eligibility"


class RequiredDocument_international(models.Model):
    eligibility = models.ForeignKey(EligibilityRequirement_interanational, on_delete=models.CASCADE, related_name='documents')
    document_name = models.CharField(max_length=200)

    def __str__(self):
        return self.document_name

class ApplicationStep_international(models.Model):
    step_number = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=100, blank=True, null=True)  # e.g., "1-2 weeks", optional

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"
class FeeStructure_internationaladdmisions(models.Model):
    PROGRAM_LEVEL_CHOICES = [
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
        ('PhD', 'Doctoral'),
    ]

    level = models.CharField(max_length=5, choices=PROGRAM_LEVEL_CHOICES)
    tuition_fee_min = models.IntegerField()
    tuition_fee_max = models.IntegerField()
    accommodation_min = models.IntegerField()
    accommodation_max = models.IntegerField()
    living_expenses_min = models.IntegerField()
    living_expenses_max = models.IntegerField()

    def __str__(self):
        return f"{self.get_level_display()} Fee Structure"
class Scholarship_international(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title
class StudentSupportService_international(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title
class ContactOffice_ainternationaldmissions(models.Model):
    OFFICE_CHOICES = [
        ('admissions', 'International Admissions Office'),
        ('services', 'Student Services'),
    ]

    office_type = models.CharField(max_length=20, choices=OFFICE_CHOICES)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    working_hours = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.get_office_type_display()} Contact"
