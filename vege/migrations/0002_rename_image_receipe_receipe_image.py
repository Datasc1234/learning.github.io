# Generated by Django 4.2.3 on 2023-07-26 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipe',
            old_name='image',
            new_name='receipe_image',
        ),
    ]