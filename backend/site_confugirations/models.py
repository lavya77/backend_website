from django.db import models

# Create your models here.
class themes(models.Model):
    font_color=models.CharField(max_length=255,null=True)
    font_size=models.CharField(max_length=255,null=True)
    font_weight=models.CharField(max_length=255,null=True)
    font_style=models.CharField(max_length=255,null=True)
    button_color=models.CharField(max_length=255,null=True)

class Navbar(models.Model):
    background_color=models.CharField(max_length=255,null=True)
    icon_class=models.CharField(max_length=255,null=True)
    logo=models.ImageField(upload_to='logo_images/')
    icon_url=models.URLField()

class Footer(models.Model):
    logo=models.ImageField(upload_to='logo_images/')
    title=models.CharField(max_length=255,null=True)
    subtext=models.CharField(max_length=255,null=True)
    description=models.TextField()
    icon_class=models.CharField(max_length=255,null=True)
    icon_url=models.URLField()

class footer_links(models.Model):
    title=models.


