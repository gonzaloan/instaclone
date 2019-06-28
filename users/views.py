""" User views"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Exceptions
from django.db.utils import IntegrityError
def login_view(request):
    """Login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            #Redirección
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid Username and password'})

    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    """Logout a user"""
    logout(request)
    return redirect('login')


def signup_view(request):
    """Signup View"""
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation doesnt match'})

        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'User already taken'})
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        # Crear un profile
        profile = Profile(user= user)
        profile.save()

        return redirect('login')
    return render(request, "users/signup.html")

