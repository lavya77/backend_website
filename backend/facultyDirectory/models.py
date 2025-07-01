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
    publication_choice=[
        ('Journal','Journal'),
        ('Conference','Conference'),
    ]
    grade_choice=[
        ('Q1','Q1'),
        ('A','A'),
        ('A+','A+')
    ]
    title=models.CharField(max_length=255,null=True,blank=True)
    names=models.CharField(max_length=255,null=True,blank=True)
    topic=models.CharField(max_length=255,null=True,blank=True)
    type_of_publication=models.CharField(max_length=255,null=True,blank=True,choices=publication_choice)
    grade=models.CharField(max_length=255,null=True,blank=True,choices=grade_choice)
    citations=models.CharField(max_length=255,null=True,blank=True)
    doi=models.CharField(max_length=255,null=True,blank=True)
    button1_text=models.CharField(max_length=255,null=True,blank=True)
    button1_url=models.CharField(max_length=255,null=True,blank=True)
    button2_text=models.CharField(max_length=255,null=True,blank=True)
    button2_url=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title

class publication_satistics(models.Model):
    value=models.CharField(max_length=255,null=True,blank=True)
    label=models.CharField(max_length=255,null=True,blank=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)
    text_color=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.label

class patent_portfolio_stats(models.Model):
    value=models.CharField(max_length=255,null=True,blank=True)
    label=models.CharField(max_length=255,null=True,blank=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)
    text_color=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.label
class patent_portfolio_description(models.Model):
    description=models.TextField(null=True)

    def __str__(self):
        return self.description
class Patent_application(models.Model):
    status_choices=[
        ('Filed','Filed'),
        ('Under Examination','Under Examination'),
        ('Published','Published')
    ]
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    application_number=models.CharField(max_length=255,null=True,blank=True)
    location=models.CharField(max_length=255,null=True,blank=True)
    technical_field=models.CharField(max_length=255,null=True,blank=True)
    patent_office=models.CharField(max_length=255,null=True,blank=True)
    filed_on=models.CharField(max_length=255,null=True,blank=True)
    year=models.CharField(max_length=255,null=True,blank=True)
    inventors=models.ManyToManyField(FacultyDirectory,related_name="inventos")
    status=models.CharField(max_length=255,null=True,blank=True,choices=status_choices)
    button1_text=models.CharField(max_length=255,null=True,blank=True)
    button1_url=models.CharField(max_length=255,null=True,blank=True)
    button2_text=models.CharField(max_length=255,null=True,blank=True)
    button2_url=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title
class Patent_filing_timeline(models.Model):
    status_choices=[
        ('Filed','Filed'),
        ('Under Examination','Under Examination'),
        ('Published','Published')
    ]
    title=models.CharField(max_length=255,null=True,blank=True)
    file_number=models.CharField(max_length=255,null=True,blank=True)
    year=models.CharField(max_length=255,null=True,blank=True)
    status=models.CharField(max_length=255,null=True,blank=True,choices=status_choices)

    def __str__(self):
        return self.title
class Professional_certifications_status(models.Model):
    value=models.CharField(max_length=255,null=True,blank=True)
    label=models.CharField(max_length=255,null=True,blank=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)
    text_color=models.CharField(max_length=255,null=True,blank=True)

    def  __str__(self):
        return self.label
class Professional_certifications_description(models.Model):
    description=models.CharField(max_length=255,null=True,blank=True)

    def __str__(slef):
        return self.description

class Skilss_Certifications(models.Model):
    skill_name=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.skill_name        

class Certification_portfolio(models.Model):
    designation_choices=[
        ('Associate','Associate'),
        ('Professional','Professional'),
        ('Specialiaton','Specialization')
    ]
    status_choices=[
        ('Verified','Verified'),
        ('Pending','Pending'),
        ('Not Verified','Not Verified')
    ]
    icon_class=models.CharField(max_length=255,null=True,blank=True)
    title=models.CharField(max_length=255,null=True,blank=True)
    comapany_name=models.CharField(max_length=255,null=True,blank=True)
    obtained_year=models.CharField(max_length=255,null=True,blank=True)
    valid_until=models.CharField(max_length=255,null=True,blank=True)
    credential_id=models.CharField(max_length=255,null=True,blank=True)
    level=models.CharField(max_length=255,null=True,blank=True)
    skills_covered=models.ManyToManyField(Skilss_Certifications,related_name="skilss")
    button1_text=models.CharField(max_length=255,null=True,blank=True)
    button1_url=models.CharField(max_length=255,null=True,blank=True)
    button2_text=models.CharField(max_length=255,null=True,blank=True)
    button2_url=models.CharField(max_length=255,null=True,blank=True)
    designation=models.CharField(max_length=255,null=True,blank=True,choices=designation_choices)
    status=models.CharField(max_length=255,null=True,blank=True,choices=status_choices)

    def __str__(self):
        return self.title

class Professional_Development_certifications(models.Model):
    type_choice=[
        ('Workshop','Workshop'),
        ('FDP','FDP'),
        ('Conference','Conference')
    ]
    title=models.CharField(max_length=255,null=True,blank=True)
    university_name=models.CharField(max_length=255,null=True,blank=True)
    duration=models.CharField(max_length=255,null=True,blank=True)
    year=models.CharField(max_length=255,null=True,blank=True)
    Type=models.CharField(max_length=255,null=True,blank=True,choices=type_choice)

    def __str__(self):
        return self.title
class invited_talks_stats(models.Model):
    value=models.CharField(max_length=255,null=True,blank=True)
    label=models.CharField(max_length=255,null=True,blank=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)
    text_color=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.label
class invited_talks_description(models.Model):
    description=models.TextField(null=True)

    def __str__(self):
        return self.description

class Speaking_engagements(models.Model):
    talks_choices=[
        ('Keynote','Keynote'),
        ('Invited Talk','Invited Talk'),
        ('Guest Lecture','Guest Lecture'),
        ('Panel Discussion','Pannel Discussion')
    ]
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.CharField(max_length=255,null=True,blank=True)
    event_type=models.CharField(max_length=255,null=True,blank=True)
    host=models.CharField(max_length=255,null=True,blank=True)
    role=models.CharField(max_length=255,null=True,blank=True)
    date=models.CharField(max_length=255,null=True,blank=True)
    location=models.CharField(max_length=255,null=True,blank=True)
    number_of_people=models.CharField(max_length=255,null=True,blank=True)
    slides_available = models.BooleanField(default=False)
    recording_available = models.BooleanField(default=False)
    button1_text=models.CharField(max_length=255,null=True,blank=True)
    button1_url=models.CharField(max_length=255,null=True,blank=True)
    button2_text=models.CharField(max_length=255,null=True,blank=True)
    button2_url=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title
class speaking_expertise(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    number_of_talks=models.CharField(max_length=255,null=True,blank=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)
    text_color=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title

class award_achievements_stats(models.Model):
    value=models.CharField(max_length=255,null=True,blank=True)
    label=models.CharField(max_length=255,null=True,blank=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)
    text_color=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.label
class award_achievements_description(models.Model):
    description=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.description
class award_recognition(models.Model):
    icon_class=models.CharField(max_length=255,null=True,blank=True)
    Institutional=models.BooleanField(default=False)
    University=models.BooleanField(default=False)
    Academic=models.BooleanField(default=False)
    International=models.BooleanField(default=False)
    Professional=models.BooleanField(default=False)
    Nattional=models.BooleanField(default=False)
    Department=models.BooleanField(default=False)
    Governmnet=models.BooleanField(default=False)
    Academic=models.BooleanField(default=False)
    title=models.CharField(max_length=255,null=True,blank=True)
    place=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    comment=models.TextField(null=True)
    year=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title
class notatble_achievements_award(models.Model):
    icon_class=models.CharField(max_length=255,null=True,blank=True)
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.CharField(max_length=255,null=True,blank=True)
    number_of_journals=models.CharField(max_length=255,null=True,blank=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title
class Awards_timeline(models.Model):
    type_choice=[
        ('University','University'),
        ('Institutional','Institutional'),
        ('National','National')
    ]
    title=models.CharField(max_length=255,null=True,blank=True)
    place=models.CharField(max_length=255,null=True,blank=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)
    secondary_color=models.CharField(max_length=255,null=True,blank=True)
    year=models.CharField(max_length=255,null=True,blank=True)
    Type=models.CharField(max_length=255,null=True,blank=True,choices=type_choice)

    def __str__(self):
        return self.title

class Social_imapcat_stats(models.Model):
    value=models.CharField(max_length=255,null=True,blank=True)
    label=models.CharField(max_length=255,null=True,blank=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)
    text_color=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.label
class Social_impact_description(models.Model):
    description=models.TextField(null=True)

    def __str__(self):
        return self.description
        
class community_initiative_social(models.Model):
    reach_choice=[
        {'Coomunity Outreach','Community Outreach'},
        ('Environmnental Conservation','Environmenta Conservation'),
        ('Education Access','Education Access'),
        ('Cybersecurtiy Awareness','Cybersecurty Awareness'),
        ('Healthcare Support','Healthcare Support'),
        ('Technology For Good','Technollogy For Good')
    ]
    category=models.CharField(max_length=255,null=True,blank=True,choices=reach_choice)
    title=models.CharField(max_length=255,null=True,blank=True)
    place=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    duration=models.CharField(max_length=255,null=True,blank=True)
    beneficairies=models.CharField(max_length=255,null=True,blank=True) 
    location=models.CharField(max_length=255,null=True,blank=True)
    photos=models.CharField(max_length=255,null=True,blank=True)
    key_impact=models.TextField(null=True)
    button1_text=models.CharField(max_length=255,null=True,blank=True)
    button1_url=models.CharField(max_length=255,null=True,blank=True)
    button2_text=models.CharField(max_length=255,null=True,blank=True)
    button2_url=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title

class social_impact_summary(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    label=models.CharField(max_length=255,null=True,blank=True)
    number_of_contributons=models.CharField(max_length=255,null=True,blank=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)
    text_color=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title
