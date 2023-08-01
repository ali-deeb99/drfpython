# Generated by Django 4.2.2 on 2023-07-29 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0030_alter_obada_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_name', models.CharField(max_length=100)),
                ('contact_person_name', models.CharField(max_length=100)),
                ('contact_person_email', models.EmailField(max_length=254)),
                ('contact_person_phone_number', models.CharField(max_length=100)),
                ('brief_decription_of_the_entity', models.TextField()),
                ('website_url', models.URLField()),
                ('type_of_courses_pathes_plan_to_create', models.TextField()),
                ('target_audience_for_courses_paths', models.TextField()),
                ('Proposed_course_name', models.CharField(max_length=100)),
                ('brief_description_of_the_course', models.TextField()),
                ('estimated_number_of_course_programes_plan_to_create', models.IntegerField(blank=True)),
                ('estimated_timeline_for_course_program_creation', models.DateField()),
                ('content_delivery_format', models.TextField()),
                ('any_existing_courses_programes_they_have_created_before', models.TextField(blank=True)),
                ('any_reviews', models.TextField(blank=True)),
                ('any_additional_information', models.TextField(blank=True)),
            ],
        ),
    ]