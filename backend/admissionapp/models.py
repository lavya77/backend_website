from django.db import models

# Create your models here.
class admission_process_herosection(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self):
        return self.title

class step_process(models.Model):
    step_title=models.CharField(max_length=255,null=True,blank=True)
    step_description=models.CharField(max_length=255,null=True,blank=True)
    duration=models.CharField(max_length=255,null=True,blank=True)
    icon_clas=models.CharField(max_length=255,null=True,blank=True)
    status=models.CharField(max_length=255,null=True,blank=True,choices=[
        ('Completd','Completed'),
        ('Upcoming','Upcoming')
    ])

    def __str__(self):
        return self.step_title

class ImportantDate(models.Model):
    EVENT_STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('upcoming', 'Upcoming'),
    ]

    event_name = models.CharField(max_length=255,null=True,blank=True)
    event_date = models.CharField(max_length=255,null=True,blank=True)
    status = models.CharField(max_length=255, choices=EVENT_STATUS_CHOICES, default='upcoming')
    icon_class = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return f"{self.event_name} - {self.event_date}"


class RequiredDocument(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    is_required = models.BooleanField(default=True)
    icon_class = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name


class ActionButton(models.Model):
    button_text = models.CharField(max_length=255,null=True,blank=True)
    url = models.CharField(max_length=255,null=True,blank=True)
    button_text2=models.CharField(max_length=255,null=True,blank=True)
    pdf=models.FileField(upload_to='prospectu/',null=True,blank=True)

    def __str__(self):
        return self.button_text

class Courses_offered_herosection(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title
class stats_coursesoffered(models.Model):
    values= models.CharField(max_length=100, help_text="e.g., 20+")
    title= models.CharField(max_length=100, help_text="e.g., Schools, programs")
    color = models.CharField(max_length=20, help_text="Hex or Tailwind color name, e.g., 'blue', 'green'")
    icon = models.CharField(max_length=50, null=True, blank=True, help_text="Optional: icon class if needed")

    def __str__(self):
        return self.title

class School_course_offered(models.Model):
    course_name=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.course_name

class schools_coursesoffered(models.Model):
    course=models.ForeignKey(School_course_offered,on_delete=models.CASCADE)
    school_name=models.CharField(max_length=255)
    image = models.ImageField(upload_to='school_images/', null=True, blank=True)
    
    def __str__(self):
        return self.school_name


class courses_coursesoffered(models.Model):
    course=models.ForeignKey(School_course_offered,on_delete=models.CASCADE)
    graduate_category=models.CharField(max_length=255,choices=[
        ('Undergraduate','Undergraduate'),
        ('Postgraduate','Postgraduate'),
        ('Doctoral','Doctoral')
    ],null=True)
    card_title=models.CharField(max_length=255,null=True,blank=True)
    specialisation=models.CharField(max_length=255,null=True,blank=True)
    seats=models.PositiveIntegerField(null=True)
    year=models.PositiveIntegerField(null=True)
    eligibility=models.CharField(max_length=255,null=True,blank=True)
    Highlights=models.TextField(null=True)

    def __str__(self):
        return self.card_title

class ready_to_apply_coussesoffered(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    button_text=models.CharField(max_length=255,null=True,blank=True)
    url=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.button_text

class eligibility_rservation_herosection(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)
    notice_title=models.CharField(max_length=255,null=True,blank=True)
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
    name = models.CharField(max_length=255,null=True,blank=True)
    level = models.CharField(max_length=255,null=True, choices=PROGRAM_LEVEL_CHOICES)
    academic_qualification = models.TextField(null=True)
    entrance_exam = models.CharField(max_length=200)
    age_limit = models.CharField(max_length=255,null=True,blank=True)
    general_eligibility_percent = models.CharField(max_length=255,null=True,blank=True,
        help_text="General category minimum percentage"
    )
    reserved_eligibility_percent =  models.CharField(max_length=255,null=True,blank=True,
        help_text="Reserved category minimum percentage"
    )

    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"       

class Fee_structure(models.Model):
    background_color= models.CharField(max_length=255,null=True,blank=True)
    title= models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    fee_policy=models.TextField(null=True)
    icon_feepolicy= models.CharField(max_length=255,null=True,blank=True)
    color_fee= models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title
class Fee_structure_section(models.Model):
    name= models.CharField(max_length=255,null=True,blank=True,help_text="Fee structre or Payment optionsor Scholoardhips")

    def __str__(self):
        return self.name
class Program_Feestructure(models.Model):
    PROGRAM_LEVEL_CHOICES = [
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
    ]
    section_name=models.ForeignKey(Fee_structure_section,on_delete=models.CASCADE)
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

class Fee_Payments_option(models.Model):
    section_name=models.ForeignKey(Fee_structure_section,on_delete=models.CASCADE)
    icon= models.CharField(max_length=255,null=True,blank=True)
    title= models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    background_color= models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title
class Scholarship_feee(models.Model):
    section_name=models.ForeignKey(Fee_structure_section,on_delete=models.CASCADE)
    scholarship_name=models.CharField(max_length=255,null=True,blank=True)
    elegibility=models.CharField(max_length=255,null=True,blank=True)
    amount=models.CharField(max_length=255,null=True,blank=True)
    duration=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.scholarship_name
class prospectus_fee(models.Model):
    section_name=models.ForeignKey(Fee_structure_section,on_delete=models.CASCADE)
    title=models.CharField(max_length=255,null=True,blank=True)
    icon=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    sie=models.CharField(max_length=255,null=True,blank=True)
    pages=models.CharField(max_length=255,null=True,blank=True)
    button_text=models.CharField(max_length=255,null=True,blank=True)
    button_url=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title

class international_admissions_herosection(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)


    def __str__(self):
        return self.title

class stats_international(models.Model):
    values= models.CharField(max_length=255,null=True,blank=True)
    title= models.CharField(max_length=255,null=True,blank=True)
    color = models.CharField(max_length=255,null=True,blank=True)
    icon = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title

class AdmissionTab_international(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    anchor_id = models.CharField(max_length=100,null=True, help_text="HTML ID for scrolling")

    def __str__(self):
        return self.title


class EligibilityRequirement_interanational(models.Model):
    PROGRAM_LEVEL_CHOICES = [
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
        ('PhD', 'Doctoral'),
    ]

    level = models.CharField(max_length=5, choices=PROGRAM_LEVEL_CHOICES)
    academic_requirement = models.TextField(null=True)
    english_proficiency = models.TextField(null=True)
    additional_requirements = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_level_display()} Eligibility"


class RequiredDocument_international(models.Model):
    eligibility = models.ForeignKey(EligibilityRequirement_interanational, on_delete=models.CASCADE, related_name='documents')
    document_name =models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.document_name

class ApplicationStep_international(models.Model):
    step_number = models.PositiveIntegerField(null=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True)
    icon=models.CharField(max_length=255,null=True,blank=True)
    duration = models.CharField(max_length=255, blank=True, null=True)  # e.g., "1-2 weeks", optional

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"
class FeeStructure_internationaladdmisions(models.Model):
    PROGRAM_LEVEL_CHOICES = [
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
        ('PhD', 'Doctoral'),
    ]

    level = models.CharField(max_length=5, choices=PROGRAM_LEVEL_CHOICES)
    tuition_fee_min = models.CharField(max_length=255,null=True,blank=True)
    tuition_fee_max = models.CharField(max_length=255,null=True,blank=True)
    accommodation_min =models.CharField(max_length=255,null=True,blank=True)
    accommodation_max = models.CharField(max_length=255,null=True,blank=True)
    living_expenses_min =models.CharField(max_length=255,null=True,blank=True)
    living_expenses_max = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return f"{self.get_level_display()} Fee Structure"
class Scholarship_international(models.Model):
    fee_wavler=models.CharField(max_length=255,null=True,blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title
class StudentSupportService_international(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title
class ContactOffice_ainternationaldmissions(models.Model):
    OFFICE_CHOICES = [
        ('international admissions', 'International Admissions Office'),
        ('student services', 'Student Services'),
    ]

    office_type = models.CharField(max_length=255,null=True, choices=OFFICE_CHOICES)
    email = models.EmailField(null=True,blank=True)
    phone =models.CharField(max_length=255,null=True,blank=True)
    working_hours = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return f"{self.get_office_type_display()} Contact"
class Ready_toAplly_internationaladmissions(models.Model):
    background_color=models.CharField(max_length=255,null=True,blank=True)
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    button1_text=models.CharField(max_length=255,null=True,blank=True)
    button1_url=models.CharField(max_length=255,null=True,blank=True)
    button2_text=models.CharField(max_length=255,null=True,blank=True)
    button2_url=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title       
