from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    is_admin = models.BooleanField(default=False) 

class VaccinationCenter(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

class VaccinationSlot(models.Model):
    center = models.ForeignKey(VaccinationCenter, on_delete=models.CASCADE)
    date = models.DateField()
    available_slots = models.IntegerField(default=10)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(VaccinationSlot, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)