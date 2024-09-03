from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import UserRegistrationForm, CustomUserChangeForm, CustomLoginForm, CustomUserForm
from .models import CustomUser

# Custom admin required decorator
def admin_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            messages.error(request, 'You do not have permission to access this page.')
            return redirect('home')
    return wrap

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            auth_login(request, user)
            messages.success(request, 'Registration successful! Welcome.')
            return redirect('home')  # Redirect to a home page or dashboard
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Login successful! Welcome back.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials. Please try again.')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    else:
        form = CustomLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout(request):
    auth_logout(request)  # This logs out the user
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')  # Redirect to a home page or login page after logout

@login_required
def profile_view(request):
    user = get_object_or_404(CustomUser, email=request.user.email)
    context = {
        'user': user
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required
@admin_required
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})

@login_required
@admin_required
def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully!')
            return redirect('user_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserForm(instance=user)
    return render(request, 'edit_user.html', {'form': form})

@login_required
@admin_required
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully!')
        return redirect('user_list')
    return render(request, 'confirm_delete.html', {'user': user})











import csv
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import CustomUser

@login_required
@admin_required
def download_users_csv(request):
    # Create the HttpResponse object with CSV header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="caco_users.csv"'

    writer = csv.writer(response)
    # Write the header row with only essential field names
    writer.writerow([
        'ID', 'Email', 'First Name', 'Middle Name', 'Surname',
        'NIDA Number', 'Phone Number 1', 'Phone Number 2', 
        'Gender'
    ])

    # Fetch users from the database excluding superusers
    users = CustomUser.objects.filter(is_superuser=False)
    for user in users:
        writer.writerow([
            user.id, user.email, user.first_name, user.middle_name, user.surname,
            user.nida_number, user.phone_number_1, user.phone_number_2,
            user.gender
        ])

    return response
