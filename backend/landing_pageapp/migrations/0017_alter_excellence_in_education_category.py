# Generated by Django 5.2.2 on 2025-07-25 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_pageapp', '0016_alter_excellence_in_education_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excellence_in_education',
            name='category',
            field=models.CharField(choices=[('Centers OF EXcellence', 'Centre Of Excellence'), ('Research Labs', 'Researc Labs'), ('Infrastructure', 'Infrastructure')], max_length=50),
        ),
    ]
