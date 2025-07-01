from django.db import models

# Create your models here.
class school_ict_herosection(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)
    background_image=models.ImageField(upload_to="school_image/",null=True,blank=True,default='default/default.jpg')
    gradient=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title

class school_aboutus(models.Model):
    icon_class=models.CharField(max_length=255,null=True,blank=True)
    title=models.CharField(max_length=255,null=True,blank=True)
    description1=models.TextField(null=True)
    description2=models.TextField(null=True)
    color1=models.CharField(max_length=255,null=True,blank=True)
    collor2=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title
class stats_spaeak_for_themsleves(models.Model):
    value=models.CharField(max_length=255,null=True,blank=True)
    label=models.CharField(max_length=255,null=True,blank=True)
    color1=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.label

class dean_message(models.Model):
    image=models.ImageField(upload_to='dean_image/',null=True,blank=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    designation=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)

    def __str__(self):
        return self.name

class Departments_school(models.Model):
    image=models.ImageField(upload_to='department_image/',null=True,blank=True)
    tag=models.CharField(max_length=255,null=True,blank=True,help_text='CSE or IT')
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    faculty_number=models.CharField(max_length=255,null=True,blank=True)
    programs_offered=models.CharField(max_length=255,null=True,blank=True)
    button_text=models.CharField(max_length=255,null=True,blank=True)
    button_url=models.CharField(max_length=255,null=True,blank=True)
    color=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title
class Specialization(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name

class our_prorams(models.Model):
    image=models.ImageField(upload_to='our_program',null=True,blank=True)
    course_name=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    specializations=models.ManyToManyField(Specialization,related_name='specialization')
    year=models.CharField(max_length=255,null=True,blank=True)
    couses_tag=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.course_name
class Faculty_of_ICt(models.Model):
    image=models.ImageField(upload_to='faculty/',blank=True,null=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    designation=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name
class Notices(models.Model):
    type_of_notice_choices=[
        ('Important','Important'),
        ('Administrative','Administrative'),
        ('General','General'),
        ('Academic','Academic'),
        ('Research','Research'),
        ('Placement','Placement'),

    ]
    notice=models.CharField(max_length=255,null=True,blank=True)
    date=models.DateTimeField()
    url=models.CharField(max_length=255,null=True,blank=True)
    type_of_notice=models.CharField(max_length=255,null=True,blank=True,choices=type_of_notice_choices)

    def __str__(self):
        return self.notice
class Event_gallery(models.Model):
    image=models.ImageField(upload_to='event_gallery/',null=True,blank=True)
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    date=models.DateTimeField()
    url=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title

class student_clubs_activities(models.Model):
    type_choice=[
        ('Technical & Cultural','Technical & Cultural'),
        ('Technical','Techincal'),
        ('Professional','Professional'),
        ('Cultural','Cultural'),
        ('Adventure','Adventure')
    ]
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    faculty_advisor=models.CharField(max_length=255,null=True,blank=True)
    members=models.CharField(max_length=255,null=True,blank=True)
    image=models.ImageField(upload_to='clubs_images/',null=True,blank=True)
    type_club=models.CharField(max_length=255,null=True,blank=True,choices=type_choice)
    icon1=models.CharField(max_length=255,null=True,blank=True)
    icon2=models.CharField(max_length=255,null=True,blank=True)
    icon3=models.CharField(max_length=255,null=True,blank=True)
    icon1_url=models.CharField(max_length=255,null=True,blank=True)
    icon2_url=models.CharField(max_length=255,null=True,blank=True)
    icon3_url=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title

class Placement_stats(models.Model):
    background_color=models.CharField(max_length=255,null=True,blank=True)
    value=models.CharField(max_length=255,null=True,blank=True)
    label=models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self):
        return self.label
class Placement_herosection_image(models.Model):
    image=models.ImageField(upload_to='placement/',null=True,blank=True)

    def __str__(self):
        return self.image
class Recent_placement(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)
    course=models.CharField(max_length=255,null=True,blank=True)
    package=models.CharField(max_length=255,null=True,blank=True)
    company_name=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name

class Recruiterss(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)
    image=models.ImageField(upload_to='company_image/',null=True,blank=True)

    def __str__(self):
        return self.name

class startup_stats(models.Model):
    value=models.CharField(max_length=255,null=True,blank=True)
    color=models.CharField(max_length=255,null=True,blank=True)
    label=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.label 
class student_startup(models.Model):
    type_choice=[
        ('Incubated','Incubated'),
    ]
    year=models.CharField(max_length=255,null=True,blank=True)
    image=models.ImageField(upload_to='image/',null=True,blank=True)
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    founded_by=models.CharField(max_length=255,null=True,blank=True)
    funding=models.CharField(max_length=255,null=True,blank=True)
    type_of=models.CharField(max_length=255,null=True,blank=True,choices=type_choice)

    def __str__(self):
        return self.title
class Student_achievements(models.Model):
    image=models.ImageField(upload_to='student_achievement/',null=True,blank=True)
    year=models.CharField(max_length=255,null=True,blank=True)
    department=models.CharField(max_length=255,null=True,blank=True)
    title=models.CharField(max_length=255,null=True,blank=True)
    sub_title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True) 
    who_achieved=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title

class faculty_herosection(models.Model):
    background_color=models.CharField(max_length=255,null=True,blank=True)
    background_image=models.ImageField(upload_to='faculty_memeber_image',null=True,blank=True)
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)

    def __str__(self):
        return self.title

class faculty_department_herosection(models.Model):
    background_color=models.CharField(max_length=255,null=True,blank=True)
    title=models.CharField(max_length=255,null=True,blank=True)
    sub_title=models.CharField(max_length=255,null=True,blank=True)
    background_image=models.ImageField(upload_to='faculty_school',null=True,blank=True)

    def __str__(self):
        return self.title

class Faculty_profile(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)
    designation=models.CharField(max_length=255,null=True,blank=True)
    specializations=models.ManyToManyField(Specialization)
    year_experience=models.CharField(max_length=255,null=True,blank=True)
    publications=models.CharField(max_length=255,null=True,blank=True)
    education=models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(unique=True)
    phone_number=models.CharField(max_length=255,null=True,blank=True)
    profile_image=models.ImageField(upload_to='faculty_image',null=True,blank=True)

    def __str__(self):
        return self.name

