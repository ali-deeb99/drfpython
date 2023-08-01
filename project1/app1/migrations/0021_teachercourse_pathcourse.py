# Generated by Django 4.2.3 on 2023-07-12 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_coursesection'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.course')),
                ('teacher_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.teacher')),
            ],
            options={
                'unique_together': {('teacher_username', 'course_name')},
            },
        ),
        migrations.CreateModel(
            name='PathCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_of_course', models.IntegerField()),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.course')),
                ('path_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.path')),
            ],
            options={
                'unique_together': {('path_name', 'course_name')},
            },
        ),
    ]
