from django.db import models

class ResearchArea(models.Model):
    topic_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.topic_name or ""


class FacultyDirectory(models.Model):
    profile_image = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True)
    categories = models.ManyToManyField(ResearchArea, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    university_name = models.CharField(max_length=255, null=True, blank=True)
    button1_text = models.CharField(max_length=255, null=True, blank=True)
    button2_text = models.CharField(max_length=255, null=True, blank=True)
    button3_text = models.CharField(max_length=255, null=True, blank=True)
    url1 = models.FileField(upload_to='cv/', null=True, blank=True)
    url2 = models.CharField(max_length=255, null=True, blank=True)
    url3 = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name or ""


class SummaryDashboard(models.Model):
    background_color = models.CharField(max_length=255, null=True, blank=True)
    text_color = models.CharField(max_length=255, null=True, blank=True)
    value = models.CharField(max_length=255, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.value}-{self.label}'


class AboutOverview(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title or ""


class OverviewResearch(models.Model):
    card_title = models.CharField(max_length=255, null=True, blank=True)
    card_desc = models.CharField(max_length=255, null=True, blank=True)
    background_color = models.CharField(max_length=255, null=True, blank=True)
    text_color = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.card_title or ""


class OverviewQuickLink(models.Model):
    text = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.text or ""


class EducationalQualification(models.Model):
    GRADUATE_CHOICES = [
        ('Doctorate', 'Doctorate'),
        ('Masters', 'Masters'),
        ('Bachelors', 'Bachelors')
    ]
    degree = models.CharField(max_length=255, null=True, blank=True)
    institute_name = models.CharField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    year = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    graduation_tag = models.CharField(max_length=255, choices=GRADUATE_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.degree or ""


class ProfessionalExperienceQualification(models.Model):
    EDUCATIONAL_CHOICES = [
        ('Academic', 'Academic')
    ]
    educational_tag = models.CharField(max_length=255, choices=EDUCATIONAL_CHOICES, null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True)
    assigned_under = models.CharField(max_length=255, null=True, blank=True)
    university_name = models.CharField(max_length=255, null=True, blank=True)
    year_present = models.CharField(max_length=255, null=True, blank=True, help_text="e.g., 2022-Present")
    key_responsibilities = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.designation or ""


class Teaching(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title or ""


class CourseCode(models.Model):
    code = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.code or ""


class CoursesTaughtTeaching(models.Model):
    GRADUATE_LEVELS = [
        ('UG', 'UG'),
        ('PG', 'PG'),
        ('PhD', 'PhD')
    ]
    course_code = models.ForeignKey(CourseCode, on_delete=models.CASCADE, null=True, blank=True)
    topic_title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    year = models.CharField(max_length=255, null=True, blank=True)
    no_of_students = models.CharField(max_length=255, null=True, blank=True)
    credits = models.CharField(max_length=255, null=True, blank=True)
    batch = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.topic_title or ""


class LectureSlideTeaching(models.Model):
    subject_name = models.CharField(max_length=255, null=True, blank=True)
    pdf_name = models.CharField(max_length=255, null=True, blank=True)
    upload_on = models.CharField(max_length=255, null=True, blank=True)
    file_upload = models.FileField(upload_to='lecture_slides/', null=True, blank=True)

    def __str__(self):
        return self.subject_name or ""


class TeachingStat(models.Model):
    value = models.CharField(max_length=255, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
    background_color = models.CharField(max_length=255, null=True, blank=True)
    text_color = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.value or ""


class AdministrationRole(models.Model):
    STATUS_CHOICES = [
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed')
    ]
    role = models.CharField(max_length=255, null=True, blank=True)
    role_level = models.CharField(max_length=255, null=True, blank=True)
    university_name = models.CharField(max_length=255, null=True, blank=True)
    year = models.CharField(max_length=255, null=True, blank=True)
    key_responsibilities = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.role or ""


class CommitteeMembershipAdministration(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)
    year = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title or ""


class AdministrativeImpact(models.Model):
    value = models.CharField(max_length=255, null=True, blank=True)
    roles = models.CharField(max_length=255, null=True, blank=True)
    background_color = models.CharField(max_length=255, null=True, blank=True)
    text_color = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.roles or ""


class ResearchCollaborator(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name or ""


class ResearchProject(models.Model):
    STATUS_CHOICES = [
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed')
    ]
    title = models.CharField(max_length=255, null=True, blank=True)
    durations = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)
    budget = models.CharField(max_length=255, null=True, blank=True)
    details = models.FileField(upload_to='research_projects/', null=True, blank=True)
    collaborators = models.ManyToManyField(ResearchCollaborator, blank=True)
    key_deliverables = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.title or ""


class ResearchStat(models.Model):
    value = models.CharField(max_length=255, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
    background_color = models.CharField(max_length=255, null=True, blank=True)
    text_color = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.value or ""


class ResearchGroupOverviewStat(models.Model):
    value = models.CharField(max_length=255, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
    background_color = models.CharField(max_length=255, null=True, blank=True)
    text_color = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.value or ""


class ResearchGroupOverviewDescription(models.Model):
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return (self.description or "")[:50]


class ResearchCategory(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, help_text="Either PhD Scholars or Postdoctoral Fellows")

    def __str__(self):
        return self.name or ""


class ResearchGroupOverview(models.Model):
    title = models.ForeignKey(ResearchCategory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    role_degree_subject = models.CharField(max_length=255, null=True, blank=True)
    research_area = models.ForeignKey(ResearchArea, on_delete=models.SET_NULL, null=True, blank=True)
    thesis = models.CharField(max_length=255, null=True, blank=True)
    year = models.CharField(max_length=255, null=True, blank=True)
    previous_institute = models.CharField(max_length=255, null=True, blank=True)
    publications = models.CharField(max_length=255, null=True, blank=True)
    contact_button = models.CharField(max_length=255, null=True, blank=True)
    profile_button = models.CharField(max_length=255, null=True, blank=True)
    contact_url = models.CharField(max_length=255, null=True, blank=True)
    profile_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name or ""


class ResearchAssistant(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)
    year = models.CharField(max_length=255, null=True, blank=True)
    contact_button = models.CharField(max_length=255, null=True, blank=True)
    contact_url = models.CharField(max_length=255, null=True, blank=True)
    project = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title or ""

class publications(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    