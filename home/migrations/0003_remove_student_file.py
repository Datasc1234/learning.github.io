# Generated by Django 4.2.3 on 2023-07-26 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_student_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='file',
        ),
    ]