from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


User = get_user_model()  # Get the User model you've defined

from django.contrib.auth import login, authenticate

def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})



def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Log the user in
            user = form.get_user()
            login(request, user)
            # Redirect to a success page or do something else
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})



def signout_view(request):
    logout(request)
    # Redirect to a different page or URL after logout (optional).
    # For example, you can redirect to your home page.
    return redirect('/')

