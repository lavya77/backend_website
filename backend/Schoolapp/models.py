from django.db import models

# Create your models here.
class school_ict_herosection(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True)
    background_color=models.CharField(max_length=255,null=True,blank=True)
    background_image=models.ImageField(upload_to="school_image/",null=True,blank=True)
    gradient=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title



