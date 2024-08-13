from django.db import models


# Create your models here.

class Hardware(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mini_pc = models.BooleanField(default=False)
    laptop = models.BooleanField(default=False)
    drucker = models.BooleanField(default=False)
    monitore = models.BooleanField(default=False)
    monitor_count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name