# Generated by Django 4.2.3 on 2023-07-11 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_path_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='decription',
            field=models.TextField(default=''),
        ),
    ]
