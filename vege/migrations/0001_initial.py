# Generated by Django 4.2.3 on 2023-07-26 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='receipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipe_name', models.CharField(max_length=100)),
                ('receipe_description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]