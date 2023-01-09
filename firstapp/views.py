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

from .forms import SignUpForm


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        messages.error(request, 'Please Provide the credentials to Login to your account.')
        form = SignUpForm()
    return render(request, 'registration/login.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')

def deactivate(request):
    if request.user.is_authenticated:

        return render(request, 'home.html')
    else:
        return redirect(home)


    