# Generated by Django 4.2.2 on 2023-07-29 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0031_applicationform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='contact_person_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='contact_person_phone_number',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='entity_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='website_url',
            field=models.URLField(unique=True),
        ),
    ]