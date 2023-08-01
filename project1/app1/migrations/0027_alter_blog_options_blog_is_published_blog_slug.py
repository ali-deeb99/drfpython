# Generated by Django 4.2.3 on 2023-07-13 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0026_blog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name_plural': 'My Blogs'},
        ),
        migrations.AddField(
            model_name='blog',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
