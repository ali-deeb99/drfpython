# Generated by Django 4.2.3 on 2023-07-11 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_teacher_decription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='path',
            name='teacher_id',
        ),
    ]
