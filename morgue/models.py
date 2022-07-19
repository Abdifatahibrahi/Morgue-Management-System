from django.db import models
from time import time, timezone
from datetime import datetime

# Create your models here.
from django.db import models

# GENDER = (
#     ('Male', 'Male'),
#     ('Female', 'Female'),
#     ('Intersex', 'Intersex'),
# )

class Gender(models.Model):
    gender = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.gender}'
    

class Corpse(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    next_of_kin_name = models.CharField(max_length=100, null=True, blank=True)
    next_of_kin_contact = models.IntegerField(max_length=100, blank=True, null=True,)
    date_of_death = models.DateField(blank=True, default=datetime.now())
    date_of_admission = models.DateTimeField(auto_now=True)
    time_of_admission = models.TimeField(default=datetime.now())

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.gender}"




