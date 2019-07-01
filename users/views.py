""" User views"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Exceptions
from django.db.utils import IntegrityError

# Forms
from users.forms import ProfileForm



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


def update_profile(request):
    """Update a user Profile view"""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']
            profile.picture = data['picture']
            profile.save()
            return redirect('update_profile')

    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        })
