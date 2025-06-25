from rest_framework import serializers
from .models import JoinOurAlumni, Branch, AlumniProfile


class JoinOurAlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinOurAlumni
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class AlumniProfileSerializer(serializers.ModelSerializer):
    branch = BranchSerializer(read_only=True)
    branch_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(), source='branch', write_only=True
    )

    class Meta:
        model = AlumniProfile
        fields = [
            'id',
            'full_name', 'email', 'phone_number', 'current_location',
            'graduation_year', 'branch', 'branch_id', 'degree_certificate',
            'current_job_title', 'current_company', 'linkedin_profile_url',
            'professional_bio',
            'available_for_job_referrals', 'available_for_resume_reviews', 'available_for_career_mentoring',
            'button1_text', 'button1_url',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
