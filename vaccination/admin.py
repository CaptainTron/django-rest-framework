# vaccination/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import User, VaccinationCenter, VaccinationSlot, Booking

# This will enable the custom user model in the admin panel
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'is_admin', 'is_staff', 'is_active']
    list_filter = ['is_admin', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_admin',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_admin',)}),
    )

admin.site.register(User, CustomUserAdmin)

@admin.register(VaccinationCenter)
class VaccinationCenterAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'opening_time', 'closing_time']

@admin.register(VaccinationSlot)
class VaccinationSlotAdmin(admin.ModelAdmin):
    list_display = ['center', 'date', 'available_slots']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'slot', 'booking_time']
    date_hierarchy = 'booking_time'