from django.db import models


# Create your models here.

class Hardware(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    st_number = models.CharField(max_length=100)
    mini_pc = models.BooleanField(default=False)
    laptop = models.BooleanField(default=False)
    drucker = models.BooleanField(default=False)
    monitore = models.BooleanField(default=False)
    monitor_count = models.IntegerField(null=True, blank=True)
    sonstige_hardware_details = models.CharField(max_length=200, blank=True)
