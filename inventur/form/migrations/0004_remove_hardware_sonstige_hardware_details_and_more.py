# Generated by Django 4.2.14 on 2024-08-13 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_alter_hardware_drucker_alter_hardware_laptop_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hardware',
            name='sonstige_hardware_details',
        ),
        migrations.RemoveField(
            model_name='hardware',
            name='st_number',
        ),
    ]
