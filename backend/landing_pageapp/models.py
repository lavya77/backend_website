
from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    video = models.FileField(upload_to='videos/') 
    button1_text = models.CharField(max_length=100, null=True)
    button2_text = models.CharField(max_length=100, null=True)
    button1_url = models.URLField(null=True)
    button2_url = models.URLField(null=True)

    def __str__(self):
        return self.title


class QuickAccess(models.Model):
    title = models.CharField(max_length=200)
    card_title = models.CharField(max_length=100)
    card_description = models.CharField(max_length=255, null=True)
    icon = models.CharField(max_length=50)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.card_title


class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='aboutimg/')
    button1_text = models.CharField(max_length=100)
    button2_text = models.CharField(max_length=100)
    button1_url = models.URLField()

    def __str__(self):
        return self.title


class Leadership(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    message = models.TextField()
    photo = models.ImageField(upload_to='leadership/')
    url=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name


class GlanceStat(models.Model):
    label = models.CharField(max_length=200)
    student_count = models.CharField(max_length=50, null=True)
    programs_count = models.CharField(max_length=50, null=True)
    faculty_member = models.CharField(max_length=50, null=True)
    acres_camus = models.CharField(max_length=50, null=True)
    placement_rate = models.CharField(max_length=50, null=True)
    icon = models.CharField(max_length=50)
    background_color = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.label


class NewsandEvents(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    content_text = models.TextField()
    category = models.CharField(max_length=50, choices=[
        ('Latest News', 'Latest News'),
        ('Notices/Circular', 'Notices'),
        ('Upcoming Events', 'Academic Events')
    ])
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Campus_gallery(models.Model):
    image = models.ImageField(upload_to='campusimg/')
    text = models.CharField(max_length=200)
    button1_text = models.CharField(max_length=50)
    button1_url = models.URLField()

    def __str__(self):
        return self.text


class Excellence_in_Education(models.Model):
    category_choices=[
        {'centre of excellence',"Centers OF EXcellence"},
        ("Research Labs","Researc Labs"),
        ("infrastructure","Infrastructure")
    ]
    title = models.CharField(max_length=200)
    content_text = models.TextField()
    category = models.CharField(max_length=50,choices=category_choices)
    image = models.ImageField(upload_to='realtedimg/')

    def __str__(self):
        return self.title


class Campus_life(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='realtedimg/')
    card_content = models.TextField(null=True)
    name = models.CharField(max_length=20,null=True)
    course = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title


class Companies_hiring(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='companies/')
    content_text = models.TextField()
    Companies_hiring = models.CharField(max_length=50, null=True)
    alumini_count = models.CharField(max_length=50, null=True)
    placement_rate = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title


class VirtualExperience(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    button1_text = models.CharField(max_length=50)
    video_link = models.URLField()
    background_color = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title
