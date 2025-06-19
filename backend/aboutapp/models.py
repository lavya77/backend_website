from django.db import models

# Create your models here.

class HeroSection(models.Model):
    section_name = models.CharField(max_length=100)
    content = models.TextField()
    font_size = models.CharField(max_length=20)
    font_color = models.CharField(max_length=20)
    font_type = models.CharField(max_length=50)  # Now free input
    bg_color = models.CharField(max_length=20)
    size = models.CharField(max_length=50)
    border_radius = models.CharField(max_length=20)
    border_color = models.CharField(max_length=20)
    hover_effect = models.CharField(max_length=50)
    button_text = models.CharField(max_length=50)
    button_shape = models.CharField(max_length=20)  # Now free input

class GenericCard(models.Model):
    section = models.CharField(max_length=100)
    card_bg_color = models.CharField(max_length=20)
    card_logo = models.ImageField(upload_to='card_logos/')
    card_text = models.TextField()
    card_font = models.CharField(max_length=50)
    card_font_size = models.CharField(max_length=20)
    card_icon = models.ImageField(upload_to='card_icons/')
    card_size = models.CharField(max_length=50)
    card_shadow = models.CharField(max_length=50)
    card_border_radius = models.CharField(max_length=20)
    section_background = models.CharField(max_length=20)

class TimelineElement(models.Model):
    section = models.CharField(max_length=100)
    background_color = models.CharField(max_length=20)
    content = models.TextField()
    font_type = models.CharField(max_length=50)
    font_size = models.CharField(max_length=20)
    font_color = models.CharField(max_length=20)
    icon = models.ImageField(upload_to='timeline_icons/')

class TabSection(models.Model):
    section = models.CharField(max_length=100)
    background_color = models.CharField(max_length=20)
    font_type = models.CharField(max_length=50)
    font_size = models.CharField(max_length=20)
    font_color = models.CharField(max_length=20)
    active_tab_color = models.CharField(max_length=20)
    tab_text = models.TextField()

class ImageCard(models.Model):
    section = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image_cards/')
    text = models.TextField()
    font_type = models.CharField(max_length=50)
    font_color = models.CharField(max_length=20)
    font_size = models.CharField(max_length=20)
    bg_color = models.CharField(max_length=20)
    shape = models.CharField(max_length=20)
    border_radius = models.CharField(max_length=20)

class ProgressBar(models.Model):
    section = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    icon = models.ImageField(upload_to='progress_icons/')
    font_type = models.CharField(max_length=50)
    font_size = models.CharField(max_length=20)
    font_color = models.CharField(max_length=20)

class DocumentCard(models.Model):
    section = models.CharField(max_length=100)
    background_color = models.CharField(max_length=20)
    font_type = models.CharField(max_length=50)
    font_size = models.CharField(max_length=20)
    font_weight = models.CharField(max_length=20)
    font_color = models.CharField(max_length=20)
    date = models.DateField()
    shape = models.CharField(max_length=20)
    icon = models.ImageField(upload_to='doc_icons/')
    text = models.TextField()
    subtext = models.TextField()
    hover_effect = models.CharField(max_length=50)

class GlobalCollaborationCard(models.Model):
    section = models.CharField(max_length=100)
    font_type = models.CharField(max_length=50)
    font_size = models.CharField(max_length=20)
    font_color = models.CharField(max_length=20)
    card_shadow = models.CharField(max_length=50)
    bg_color = models.CharField(max_length=20)
    bullet_color = models.CharField(max_length=20)
    content = models.TextField()

class GovernanceCard(models.Model):
    section = models.CharField(max_length=100)
    bg_color = models.CharField(max_length=20)
    font_type = models.CharField(max_length=50)
    font_size = models.CharField(max_length=20)
    font_weight = models.CharField(max_length=20)
    font_color = models.CharField(max_length=20)
    icon = models.ImageField(upload_to='gov_icons/')
    active_tab_color = models.CharField(max_length=20)
    content = models.TextField()
    shape = models.CharField(max_length=20)
    dimension = models.CharField(max_length=50)
    hover_effect = models.CharField(max_length=50)
