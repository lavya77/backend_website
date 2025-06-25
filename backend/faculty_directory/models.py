from django.db import models

class contact_herosection(models.Model):
    title=models.CharField(max_length=255)
    uni_name=models.CharField(max_length=255)
    description=models.TextField()
    background_color=models.CharField(max_length=255, blank=True)
    background_image=models.ImageField(upload_to='contact_directory/',blank=True)
    gradient_color=models.CharField(max_length=255,blank=True)

class Contact(models.Model):
    # Basic Info
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    # Office Info
    office = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=100, blank=True)
    
    # Profile Image
    image = models.ImageField(upload_to='contacts/', blank=True, null=True)
    
    # Category for filtering
    CATEGORIES = [
        ('vice_chancellor', 'Vice Chancellor'),
        ('pro_vice_chancellor', 'Pro Vice Chancellor'),
        ('registrar', 'Registrar'),
        ('deputy_registrar', 'Deputy Registrar'),
        ('other', 'Other'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORIES, default='other')
    
    # Status
    is_active = models.BooleanField(default=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_initials(self):
        """Get initials for profile display"""
        words = self.name.split()
        if len(words) >= 2:
            return f"{words[0][0]}{words[-1][0]}".upper()
        return self.name[0].upper() if self.name else "?"
        




    