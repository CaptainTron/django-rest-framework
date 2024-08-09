from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    is_admin = models.BooleanField(default=False) 

    # Add related_name to resolve the clash
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="vaccination_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="vaccination_user_set",
        related_query_name="user",
    )

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