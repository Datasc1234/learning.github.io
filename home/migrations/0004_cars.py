# Generated by Django 4.2.3 on 2023-07-26 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_student_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('speed', models.IntegerField(default=50)),
            ],
        ),
    ]
