from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import User, VaccinationCenter, VaccinationSlot, Booking
from django.db.models import F
from django.contrib import messages

# These are different views that are used to render the templates
def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
            return render(request, 'signup.html')
        
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        messages.success(request, 'Account created successfully. Welcome!')
        return redirect('user_dashboard')
    return render(request, 'signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.is_admin:
                return redirect('admin_dashboard')
            return redirect('user_dashboard')
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def user_dashboard(request):
    centers = VaccinationCenter.objects.all()
    return render(request, 'user_dashboard.html', {'centers': centers})

@login_required
def book_slot(request, center_id):
    if request.method == 'POST':
        center = VaccinationCenter.objects.get(id=center_id)
        date = request.POST['date']
        slot, created = VaccinationSlot.objects.get_or_create(center=center, date=date)
        
        if slot.available_slots > 0:
            Booking.objects.create(user=request.user, slot=slot)
            slot.available_slots = F('available_slots') - 1
            slot.save()
            return redirect('user_dashboard')
    return redirect('user_dashboard')

@login_required
def admin_dashboard(request):
    if not request.user.is_admin:
        messages.error(request, 'You do not have permission to access the admin dashboard.')
        return redirect('user_dashboard')
    centers = VaccinationCenter.objects.all()
    return render(request, 'admin_dashboard.html', {'centers': centers})

@login_required
def add_center(request):
    if not request.user.is_admin: 
        return redirect('user_dashboard')
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        opening_time = request.POST['opening_time']
        closing_time = request.POST['closing_time']
        VaccinationCenter.objects.create(
            name=name, 
            address=address, 
            opening_time=opening_time, 
            closing_time=closing_time
        )
        return redirect('admin_dashboard')
    return render(request, 'add_center.html')

@login_required
def remove_center(request, center_id):
    if not request.user.is_admin:
        return redirect('user_dashboard')
    center = VaccinationCenter.objects.get(id=center_id)
    center.delete()
    return redirect('admin_dashboard')

@login_required
def dosage_details(request):
    if not request.user.is_admin:
        messages.error(request, 'You do not have permission to view dosage details.')
        return redirect('user_dashboard')
    centers = VaccinationCenter.objects.all()
    details = []
    for center in centers:
        total_doses = Booking.objects.filter(slot__center=center).count()
        details.append({'center': center, 'total_doses': total_doses})
    return render(request, 'dosage_details.html', {'details': details})



@login_required
def add_center(request):
    if not request.user.is_admin:
        messages.error(request, 'You do not have permission to add centers.')
        return redirect('user_dashboard')

    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        opening_time = request.POST['opening_time']
        closing_time = request.POST['closing_time']
        
        VaccinationCenter.objects.create(
            name=name,  
            address=address, 
            opening_time=opening_time, 
            closing_time=closing_time
        )
        messages.success(request, 'Vaccination center added successfully.')
        return redirect('admin_dashboard')

    return render(request, 'add_center.html')