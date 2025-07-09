from django.db import models

# Create your models here.
from django.db import models

class academicherosection_Regulations(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(null=True)
    background_color = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.title

class acdemic_regulations_stats(models.Model):
    icon=models.CharField(max_length=255,blank=True,null=True)
    value=models.CharField(max_length=255,blank=True,null=True)
    label=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.label 

class academic_schedule_regulatioons(models.Model):
    title=models.CharField(max_length=255,blank=True,null=True)
    description=models.CharField(max_length=255,blank=True,null=True)
    pdf=models.FileField(upload_to='schedule/',null=True)

    def __str__(self):
        return self.title

class AcademicEvent(models.Model):
    heading = models.CharField(max_length=255,blank=True,null=True)
    desc = models.TextField(null=True)
    background_color = models.CharField(max_length=255,blank=True,null=True)
    title =models.CharField(max_length=255,blank=True,null=True)
    date = models.DateField()
    category = models.CharField(max_length=250, choices=[('admission', 'Admission'), ('exam', 'Examination'), ('break', 'Break'), ('holiday', 'Holiday'), ('academic', 'Academic')])
    description = models.TextField()
    status = models.CharField(max_length=250, choices=[('completed', 'Completed'), ('upcoming', 'Upcoming')])

    def __str__(self):
        return self.title

class AcademicRegulation(models.Model):
    icon_class=models.CharField(max_length=255,blank=True,null=True)
    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(null=True)
    document = models.FileField(upload_to='regulations/')
    last_updated = models.DateField()
    background_color = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.title

class academic_Stayupdated(models.Model):
    background_color = models.CharField(max_length=255,blank=True,null=True)
    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(null=True)
    button1_text = models.CharField(max_length=255,blank=True,null=True)
    button2_text = models.CharField(max_length=255,blank=True,null=True)
    url1 =models.CharField(max_length=255,blank=True,null=True)
    url2 = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.title

class herosection_cbcs(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(null=True)
    background_color = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.title
class cbcs_stats(models.Model):
    value=models.CharField(max_length=255,blank=True,null=True)
    icon=models.CharField(max_length=255,blank=True,null=True)
    label=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.label

class what_is_cbcs(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(null=True)
    def __str__(self):
        return self.title
class what_is_cbcs_cards(models.Model):
    icon_class = models.CharField(max_length=255,blank=True,null=True)
    card_title =models.CharField(max_length=255,blank=True,null=True)
    card_desc = models.TextField(null=True)

    def __str__(self):
        return self.card_title        


class cbcs_GradingScale(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(null=True)
    grade =models.CharField(max_length=255,blank=True,null=True)
    points = models.IntegerField(null=True)
    percentage_range = models.CharField(max_length=255,blank=True,null=True)
    description = models.CharField(max_length=255,blank=True,null=True)
    status = models.CharField(max_length=255,blank=True,null=True,choices=[('Pass','Pass'),('Fail','Fail')])

    def __str__(self):
        return f"{self.grade} - {self.points}"

class benefits_cbcbs_title(models.Model):
    title=models.CharField(max_length=255,blank=True,null=True)
    description=models.TextField(null=True)

    def __str__(self):
        return self.title

class benefits_cbcbs(models.Model):
    card_desc = models.TextField(null=True)
    icon_class = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.card_desc

class Explore_cbcs(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(null=True)
    button_text = models.CharField(max_length=255,blank=True,null=True)
    url =models.CharField(max_length=255,blank=True,null=True)
    background_color = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.title

class faculty_directory_herosection(models.Model):
    background_color=models.CharField(max_length=255,blank=True,null=True)
    background_image=models.ImageField(upload_to='faculty_background/',blank=True,null=True)
    title=models.CharField(max_length=255,blank=True,null=True)
    description=models.TextField(null=True)

    def __str__(self):
        return self.title

class Facultydirectory_stats(models.Model):
    icon_class=models.CharField(max_length=255,blank=True,null=True)
    value=models.CharField(max_length=255,blank=True,null=True)
    label=models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.label

class FacultyMember(models.Model):
    school_category = [
        ('School of Information and Communication Technology', 'School of Information and Communication Technology'),
        ('School of Biotechnology', 'School of Biotechnology'),
        ('School of Engineering', 'School of Engineering'),
        ('School of Management', 'School of Management'),
        ('School of Humanities', 'School of Humanities'),
        ('School of Law', 'School of Law')
    ]

    name = models.CharField(max_length=255, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True, choices=school_category)
    specialization = models.TextField(null=True)
    experience_years = models.CharField(max_length=255, blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='faculty/', null=True, blank=True)
    icon_class = models.CharField(max_length=50, null=True, blank=True)
    background_color = models.CharField(max_length=50, null=True, blank=True)
    faculty_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name



class faculty_join(models.Model):
    title =models.CharField(max_length=255,blank=True,null=True)
    button1_text = models.CharField(max_length=255,blank=True,null=True)
    button2_text = models.CharField(max_length=255,blank=True,null=True)
    url1 = models.CharField(max_length=255,blank=True,null=True)
    url2 = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.title

class herosection_centereofexcellence(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(null=True)
    background_color = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.title

class centre_of_excellence_highlights(models.Model):
    icon=models.CharField(max_length=255,blank=True,null=True)
    value=models.CharField(max_length=255,blank=True,null=True)
    label=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.label        
        
class centre_of_excellence_title(models.Model):
    title=models.CharField(max_length=255,blank=True,null=True)
    description=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.title

class CenterOfExcellence(models.Model):
    icon=models.CharField(max_length=255,blank=True,null=True)
    image=models.ImageField(upload_to="coe/",null=True,blank=True)
    card_title = models.CharField(max_length=255,blank=True,null=True)
    card_desc = models.TextField(null=True)
    director = models.CharField(max_length=255,blank=True,null=True)
    faculty_count =models.CharField(max_length=255,blank=True,null=True)
    student_count = models.CharField(max_length=255,blank=True,null=True)
    project_count = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.card_title

class coe_gallery_title(models.Model):
    title=models.CharField(max_length=255,blank=True,null=True)
    description=models.TextField(null=True)

    def __str__(self):
        return self.title        

class coe_gallery(models.Model):
    image = models.ImageField(upload_to='folder_name/')
    card_desc = models.TextField(null=True)

    def __str__(self):
        return self.title

class join_coe(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(null=True)
    button1_text =models.CharField(max_length=255,blank=True,null=True)
    button2_text =models.CharField(max_length=255,blank=True,null=True)
    url1 =models.CharField(max_length=255,blank=True,null=True)
    url2 =models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.title

class herosection_mou(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.title
class mous_stats(models.Model):
    icon_class= models.CharField(max_length=255,blank=True,null=True)
    value=models.CharField(max_length=255,blank=True,null=True)
    label=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.label  

class PartnerInstitute(models.Model):
    card_title = models.CharField(max_length=255,blank=True,null=True)
    card_desc = models.TextField(null=True)
    country =models.CharField(max_length=255,blank=True,null=True)
    since_year =models.CharField(max_length=255,blank=True,null=True)
    types = models.CharField(max_length=255,
     choices=[("Academic MOU", "Academic MOU"), ("Research MOU", "Research MOU")])
    url =models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.card_title

class CollaborationProgram(models.Model):
    card_title = models.CharField(max_length=255,blank=True,null=True)
    card_desc =models.TextField(null=True) 
    duration = models.CharField(max_length=255,blank=True,null=True)
    participants =models.CharField(max_length=255,blank=True,null=True)
    benefits = models.TextField(null=True)

    def __str__(self):
        return self.card_title

class UpcomingOpportunity(models.Model):
    card_title = models.CharField(max_length=255,blank=True,null=True)
    deadline = models.DateField()
    duration = models.CharField(max_length=255,blank=True,null=True)
    types = models.CharField(max_length=255,blank=True,null=True)
    benefits = models.TextField(null=True)
    elegibility = models.CharField(max_length=255,blank=True,null=True)
    button_text = models.CharField(max_length=255,blank=True,null=True)
    url = models.CharField(max_length=255,blank=True,null=True)
    icon_class=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.card_title

class collaborations_mou(models.Model):
    background_color = models.CharField(max_length=255,blank=True,null=True)
    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(null=True)
    button1_text = models.CharField(max_length=255,blank=True,null=True)
    button2_text =models.CharField(max_length=255,blank=True,null=True)
    url1 = models.CharField(max_length=255,blank=True,null=True)
    url2 = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.title

class herosection_reports(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(null=True)
    background_color=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.title

class institutional_reports_stats(models.Model):
    icon_class=models.CharField(max_length=255,blank=True,null=True)
    value=models.CharField(max_length=255,blank=True,null=True)
    label=models.CharField(max_length=255,blank=True,null=True)
    description=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.label


class InstitutionalReport(models.Model):
    card_title = models.CharField(max_length=255,blank=True,null=True)
    card_desc = models.TextField(null=True)
    category = models.CharField(max_length=250, choices=[('institutional', 'Institutional'), ('accreditation', 'Accreditation'), ('finance', 'Finance'), ('student', 'Student')])
    date = models.DateField(null=True)
    downloads = models.IntegerField(null=True)
    pages = models.IntegerField(null=True)
    file_size_mb = models.FloatField(null=True)
    file = models.FileField(upload_to='reports/',blank=True,null=True)
    button1_text=models.CharField(max_length=255,blank=True,null=True)
    button1_url=models.CharField(max_length=255,blank=True,null=True)
    view_details=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.title

class School_herosection(models.Model):
    background_color=models.CharField(max_length=255,blank=True,null=True)
    title=models.CharField(max_length=255,blank=True,null=True)
    description=models.TextField(null=True)

    def __str__(self):
        return self.title

class school_stats(models.Model):
    icon_class=models.CharField(max_length=255,blank=True,null=True)
    value=models.CharField(max_length=255,blank=True,null=True)
    label=models.CharField(max_length=255,blank=True,null=True)
    background_color=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.label

class technology_schools(models.Model):
       technology=models.CharField(max_length=255,blank=True,null=True)

       def __str__(self):
        return self.technology     

class explore_academic_excellence_schools(models.Model):
    image=models.ImageField(upload_to='Schools/',blank=True,null=True)
    school_name=models.CharField(max_length=255,blank=True,null=True)
    description=models.TextField(null=True)
    technology=models.ManyToManyField(technology_schools,blank=True,null=True)
    url=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.school_name

class school_journey(models.Model):
    title=models.CharField(max_length=255,blank=True,null=True)
    description=models.TextField(null=True)
    background_color=models.CharField(max_length=255,blank=True,null=True)
    button1_text=models.CharField(max_length=255,blank=True,null=True)
    button_url=models.CharField(max_length=255,blank=True,null=True)
    button2_url=models.CharField(max_length=255,blank=True,null=True)
    button2_text=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.title


