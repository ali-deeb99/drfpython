# Generated by Django 4.2.3 on 2023-07-11 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_delete_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=6)),
                ('level', models.CharField(choices=[('1', 'Beginner'), ('2', 'Intermidiate'), ('3', 'Advansed')], default='1', max_length=20)),
                ('teacher_username', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app1.teacher')),
            ],
        ),
    ]
