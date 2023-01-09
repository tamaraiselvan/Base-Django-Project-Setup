from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        messages.error(request, 'Please Provide the credentials to Login to your account.')
        return redirect("login")

from .forms import SignUpForm, profile_edit
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created ! You are now able to log in')
            return redirect('login')
        else: 
            messages.error(request, 'Please Provide the appropriate credentials to create your account.')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')