from django.db import models

# Create your models here.
from django.db import models

class academicherosection(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    background_color = models.CharField(max_length=20, default="#ffffff")
    icon_class = models.CharField(max_length=100, help_text="CSS class for icon, e.g., 'fa fa-home'")
    icon_text = models.CharField(max_length=50)
    ssemester_count = models.IntegerField()
    teaching_days = models.IntegerField()
    examination_periods = models.IntegerField()
    academic_regulations = models.IntegerField()

    def __str__(self):
        return self.title

class AcademicEvent(models.Model):
    heading = models.CharField(max_length=20)
    desc = models.TextField()
    background_color = models.CharField(max_length=20, default="#ffffff")
    title = models.CharField(max_length=255)
    date = models.DateField()
    category = models.CharField(max_length=50, choices=[('admission', 'Admission'), ('exam', 'Examination'), ('break', 'Break'), ('holiday', 'Holiday'), ('academic', 'Academic')])
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[('completed', 'Completed'), ('upcoming', 'Upcoming')])

    def __str__(self):
        return self.title

class AcademicRegulation(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    document = models.FileField(upload_to='regulations/')
    last_updated = models.DateField()
    background_color = models.CharField(max_length=20, default="#ffffff")

    def __str__(self):
        return self.title

class academic_Stayupdated(models.Model):
    background_color = models.CharField(max_length=20, default="#ffffff")
    title = models.CharField(max_length=255)
    description = models.TextField()
    button1_text = models.CharField(max_length=50)
    button2_text = models.CharField(max_length=50)
    url1 = models.URLField()
    url2 = models.URLField()

    def __str__(self):
        return self.title

class herosection_cbcs(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    background_color = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=50)
    icon_text = models.CharField(max_length=50)
    credits_coount = models.TextField()
    elective_courses = models.TextField()
    grading_scale = models.TextField()
    flexebility = models.TextField()

    def __str__(self):
        return self.title

class what_is_cbcs(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    icon_class = models.CharField(max_length=50)
    card_title = models.CharField(max_length=50)
    card_desc = models.TextField()

    def __str__(self):
        return self.card_title

class cbcs_courses(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    card_title = models.CharField(max_length=50)
    card_desc = models.TextField()
    credit_range = models.CharField(max_length=50)
    examples = models.CharField(max_length=50)
    background_color = models.CharField(max_length=50)

    def __str__(self):
        return self.card_title

class cbcs_GradingScale(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    grade = models.CharField(max_length=2)
    points = models.IntegerField()
    percentage_range = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.grade} - {self.points}"

class benefits_cbcbs(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    card_desc = models.TextField()
    icon_class = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Explore_cbcs(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    button_text = models.CharField(max_length=50)
    url = models.URLField()
    background_color = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Facultydirectory(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    background_color = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=50)
    icon_text = models.CharField(max_length=50)
    faculty_members = models.IntegerField()
    phd_qualified = models.IntegerField()
    Research_publications = models.IntegerField()
    collaborations_count = models.IntegerField()

    def __str__(self):
        return self.title

class FacultyMember(models.Model):
    
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    specialization = models.TextField()
    experience_years = models.IntegerField()
    publications = models.IntegerField()
    education = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='faculty/')
    icon_class = models.CharField(max_length=50),null=True,blank=True
    background_color = models.CharField(max_length=50,null=True,blank=True)
    faculty_url = models.URLField()

    class Rank(models.TextChoices):
        PROFESSOR = "Professor"
        ASSOCIATE_PROFESSOR = "Associate Professor"
        ASSISTANT_PROFESSOR = "Assistant Professor"

    rank = models.CharField(max_length=50, choices=Rank.choices)

    def __str__(self):
        return self.name

class faculty_join(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    button1_text = models.CharField(max_length=50)
    button2_text = models.CharField(max_length=50)
    url1 = models.URLField()
    url2 = models.URLField()

    def __str__(self):
        return self.title

class herosection_centereofexcellence(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    background_color = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=50)
    icon_text = models.CharField(max_length=50)
    coe_count = models.IntegerField()
    ResearchAndstudents = models.IntegerField()
    projects_count = models.IntegerField()
    memberrs_count = models.IntegerField()

    def __str__(self):
        return self.title

class CenterOfExcellence(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    card_title = models.CharField(max_length=50)
    card_desc = models.TextField()
    director = models.CharField(max_length=100)
    faculty_count = models.IntegerField()
    student_count = models.IntegerField()
    project_count = models.IntegerField()

    def __str__(self):
        return self.card_title

class coe_gallery(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='folder_name/')
    card_desc = models.TextField()

    def __str__(self):
        return self.title

class join_coe(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    button1_text = models.CharField(max_length=50)
    button2_text = models.CharField(max_length=50)
    url1 = models.URLField()
    url2 = models.URLField()

    def __str__(self):
        return self.title

class herosection_mou(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    icon_class = models.CharField(max_length=50)
    activemou_count = models.IntegerField()
    participants_counts = models.IntegerField()
    countries_count = models.IntegerField()
    publications_count = models.IntegerField()
    icon_text = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class PartnerInstitute(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    card_title = models.CharField(max_length=50)
    card_desc = models.TextField()
    country = models.CharField(max_length=100)
    since_year = models.IntegerField()
    types = models.CharField(max_length=50, choices=[("Academic MOU", "Academic MOU"), ("Research MOU", "Research MOU")])
    url = models.URLField()

    def __str__(self):
        return self.card_title

class CollaborationProgram(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    card_title = models.CharField(max_length=255)
    card_desc = models.TextField()
    duration = models.CharField(max_length=100)
    participants = models.CharField(max_length=100)
    benefits = models.TextField()

    def __str__(self):
        return self.card_title

class UpcomingOpportunity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    card_title = models.CharField(max_length=255)
    deadline = models.DateField()
    duration = models.CharField(max_length=100)
    types = models.CharField(max_length=50)
    benefits = models.TextField()
    elegibility = models.CharField(max_length=255)
    button_text = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.title

class collaborations_mou(models.Model):
    background_color = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()
    button1_text = models.CharField(max_length=50)
    button2_text = models.CharField(max_length=50)
    url1 = models.URLField()
    url2 = models.URLField()

    def __str__(self):
        return self.title

class herosection_reports(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    sub_title = models.CharField(max_length=50)
    sub_description = models.TextField()
    background_color = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=50)
    icon_text = models.CharField(max_length=50)
    reprts_count = models.IntegerField()
    accreditation_count = models.IntegerField()
    acheivements_counts = models.IntegerField()

    def __str__(self):
        return self.title

class InstitutionalReport(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    card_title = models.CharField(max_length=50)
    card_desc = models.TextField()
    category = models.CharField(max_length=50, choices=[('institutional', 'Institutional'), ('accreditation', 'Accreditation'), ('finance', 'Finance'), ('student', 'Student')])
    date = models.DateField()
    downloads = models.IntegerField()
    pages = models.IntegerField()
    file_size_mb = models.FloatField()
    file = models.FileField(upload_to='reports/')

    def __str__(self):
        return self.title

class School(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    School_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='schools/')
    url = models.URLField()

    def __str__(self):
        return self.School_name
