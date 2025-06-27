from django.db import models

class BookingHeroSection(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    button1_text = models.CharField(max_length=255, null=True, blank=True)
    button2_text = models.CharField(max_length=255, null=True, blank=True)
    button1_url = models.CharField(max_length=255, null=True, blank=True)
    button2_url = models.CharField(max_length=255, null=True, blank=True)
    background_color = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title or ""

class UserRole(models.Model):
    role_type = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.role_type or ""

class BookingFacility(models.Model):
    FACILITY_CHOICES = [
        ('Auditoriums', 'Auditoriums'),
        ('Conference Rooms', 'Conference Rooms'),
        ('Accommodation', 'Accommodation'),
        ('Sports Facility', 'Sports Facility'),
        ('Kitchen and Dining', 'Kitchen and Dining')
    ]

    CAPACITY_CHOICES = [
        ('50+ people', '50+ people'),
        ('100+ people', '100+ people'),
        ('200+ people', '200+ people'),
        ('300+ people', '300+ people')
    ]

    PRICE_CHOICES = [
        ('0-5000', '0-5000'),
        ('5000-10,000', '5000-10,000'),
        ('10,000-15,000', '10,000-15,000'),
        ('15,000+', '15,000+')
    ]

    SEASON_CHOICES = [
        ('Peak Season', 'Peak Season'),
        ('Off-Peak Season', 'Off-Peak Season')
    ]

    role = models.ForeignKey(UserRole, on_delete=models.CASCADE, null=True, blank=True)
    auditorium_number = models.CharField(max_length=255, null=True, blank=True)
    no_of_seats = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    incharge_name = models.CharField(max_length=255, null=True, blank=True)
    incharge_phone_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    peakseason_pricing = models.CharField(max_length=255, null=True, blank=True)
    off_peakseason_pricing = models.CharField(max_length=255, null=True, blank=True)
    half_day_pricing = models.CharField(max_length=255, null=True, blank=True)
    full_day_pricing = models.CharField(max_length=255, null=True, blank=True)
    your_rate = models.CharField(max_length=255, null=True, blank=True)
    available_slots = models.CharField(max_length=255, null=True, blank=True)

    # Uploading files
    rate_chart = models.FileField(upload_to="ratechart/", null=True, blank=True)
    booking_rules = models.FileField(upload_to="bookingrule/", null=True, blank=True)
    terms_conditions_file = models.FileField(upload_to="termsandcondition/", null=True, blank=True)

    # Guidelines
    booking_guidelines = models.TextField(null=True, blank=True)
    terms_conditions = models.TextField(null=True, blank=True)
    cancellation_policy = models.TextField(null=True, blank=True)

    # Buttons
    button1_text = models.CharField(max_length=255, null=True, blank=True)
    button2_text = models.CharField(max_length=255, null=True, blank=True)
    button1_url = models.CharField(max_length=255, null=True, blank=True)
    button2_url = models.CharField(max_length=255, null=True, blank=True)

    # Choices
    facility_type = models.CharField(max_length=255, choices=FACILITY_CHOICES, null=True, blank=True)
    capacity = models.CharField(max_length=255, choices=CAPACITY_CHOICES, null=True, blank=True)
    price_range = models.CharField(max_length=255, choices=PRICE_CHOICES, null=True, blank=True)
    season = models.CharField(max_length=255, choices=SEASON_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.auditorium_number or ""
