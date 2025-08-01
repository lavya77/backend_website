# Generated by Django 5.2.3 on 2025-06-26 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Student club Activites',
            },
        ),
        migrations.CreateModel(
            name='campus_life_stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('icon_class', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CampusHero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('video_url', models.URLField()),
                ('button1_text', models.CharField(max_length=255)),
                ('button2_text', models.CharField(max_length=255)),
                ('button1_url', models.URLField()),
                ('button2_url', models.URLField()),
                ('background_image', models.ImageField(upload_to='campus_hero/')),
            ],
        ),
        migrations.CreateModel(
            name='EcoCampusStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'eco campus_titlesection',
            },
        ),
        migrations.CreateModel(
            name='EcoInitiative_stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('value', models.CharField(max_length=20)),
                ('icon_class', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FoodCourtCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='campus_dining/')),
            ],
        ),
        migrations.CreateModel(
            name='FoodCourtItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon_class', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='food_courts/')),
            ],
        ),
        migrations.CreateModel(
            name='FoodOutlet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('price_range', models.CharField(max_length=20)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('review_count', models.PositiveIntegerField(default=0)),
                ('is_open', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, upload_to='outlets/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('button1_text', models.CharField(max_length=255)),
                ('button1_url', models.URLField()),
                ('button2_text', models.CharField(max_length=255)),
                ('button2_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='GreenInitiative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('impact_value', models.CharField(max_length=50)),
                ('impact_label', models.CharField(max_length=100)),
                ('impact_type', models.CharField(max_length=50)),
                ('icon_color', models.CharField(default='orange', max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='initiatives/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('capacity_text', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='hostel_images/')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='HostelLifeSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Our Hostel Life', max_length=200)),
                ('description', models.TextField()),
                ('background_color', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Hostel Life Section',
            },
        ),
        migrations.CreateModel(
            name='ImpactStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='join_nssandncc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('button1_text', models.CharField(max_length=255)),
                ('button1_url', models.URLField()),
                ('background_color', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='key_highlights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('icon_class', models.CharField(max_length=255)),
                ('button1_text', models.CharField(max_length=255)),
                ('button2_text', models.CharField(max_length=255)),
                ('button1_url', models.URLField()),
                ('button2_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Library_gbu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LibraryFacility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='library/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Library Facilities',
            },
        ),
        migrations.CreateModel(
            name='LibraryStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=50)),
                ('icon_class', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LibraryStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=20)),
                ('color', models.CharField(default='purple', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Library Statistics',
            },
        ),
        migrations.CreateModel(
            name='Meditation_herosection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_class', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('background_color', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MeditationBenefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('color', models.CharField(default='green', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MeditationSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('icon_color', models.CharField(default='green', max_length=20)),
                ('icon_class', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MeditationTechnique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('color', models.CharField(default='green', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('nss', 'NSS'), ('ncc', 'NCC')], max_length=10)),
                ('full_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('icon_color', models.CharField(default='blue', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SportsFacility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('facility_type', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=200)),
                ('capacity', models.CharField(max_length=50)),
                ('access', models.CharField(max_length=100)),
                ('timings', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('booking', models.TextField()),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='facilities/')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Sports Facilities',
            },
        ),
        migrations.CreateModel(
            name='Student_club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('president_name', models.CharField(max_length=100)),
                ('member_count', models.PositiveIntegerField(default=0)),
                ('contact_email', models.EmailField(max_length=254)),
                ('cover_image', models.ImageField(blank=True, upload_to='Student_clubs/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('button_text', models.CharField(max_length=255)),
                ('button_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentTestimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('testimonial', models.TextField()),
                ('year', models.CharField(help_text='final year or second year', max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='student_testimonials/')),
            ],
        ),
        migrations.CreateModel(
            name='VirtualTour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='virtual_tours/')),
                ('video_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='HostelDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('amenities_title', models.CharField(default='Amenities', max_length=100)),
                ('image', models.ImageField(upload_to='hostel_detail_images/')),
                ('button1_text', models.CharField(default='View Details', max_length=50)),
                ('button1_url', models.URLField(blank=True, null=True)),
                ('button2_text', models.CharField(default='Book Room', max_length=50)),
                ('button2_url', models.URLField(blank=True, null=True)),
                ('hostel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='campuslifeapp.hostel')),
            ],
            options={
                'verbose_name': 'Hostel Detail',
            },
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('order', models.PositiveIntegerField(default=0)),
                ('hostel_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenities', to='campuslifeapp.hosteldetail')),
            ],
            options={
                'verbose_name_plural': 'Hostel Amenities',
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='FacilityFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='campuslifeapp.sportsfacility')),
            ],
            options={
                'verbose_name_plural': 'sports facility',
            },
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('icon', models.CharField(default='🏆', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Student_club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achievements', to='campuslifeapp.student_club')),
            ],
            options={
                'verbose_name_plural': 'Student club Achieveents',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Popular, Multi-Cuisine, Study Friendly, etc.', max_length=50)),
                ('outlet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='campuslifeapp.foodoutlet')),
            ],
            options={
                'verbose_name_plural': 'Food tag',
            },
        ),
    ]
