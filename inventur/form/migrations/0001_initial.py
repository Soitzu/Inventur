# Generated by Django 4.2.14 on 2024-07-31 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('st_number', models.CharField(max_length=100)),
                ('mini_pc', models.BooleanField(default=False)),
                ('laptop', models.BooleanField(default=False)),
                ('drucker', models.BooleanField(default=False)),
                ('monitore', models.BooleanField(default=False)),
                ('monitor_count', models.IntegerField(blank=True, null=True)),
                ('sonstige_hardware_details', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
