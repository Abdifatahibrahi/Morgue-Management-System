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

class Next_of_kin(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.PositiveIntegerField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone}"

class Care_taker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.PositiveIntegerField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Room(models.Model):
    room_no = models.CharField(max_length=50)
    care_taker = models.ForeignKey(Care_taker, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.room_no}"

class Corpse(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    next_of_kin = models.ForeignKey(Next_of_kin, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    date_of_death = models.DateField(blank=True, default=datetime.now())
    date_of_admission = models.DateTimeField(auto_now=True)
    time_of_admission = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.gender}"




