from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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
    if request.user.is_authenticated:
        lst = User.objects.filter(username=request.user).values('id')
        l=[]
        for i in lst:
            i['encrypt_key']=encrypt(i['id'])
            i['id']=i['id']
            l.append(i)
        return render(request, 'profile.html', {'lst':l})
    else:
        messages.error(request, 'Please Provide the credentials to Login to your account.')
        return redirect("login")
    

from django.shortcuts import redirect, render, get_object_or_404
from firstapp.encryption_util import *
@login_required
def update(request,id):
    id=decrypt(id)
    
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(User, id = id)
    if request.user == obj:
 
        # pass the object as instance in form
        form = profile_edit(request.POST or None, instance = obj)
    
        # save the data from the form and
        # redirect to detail_view
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    
        # add form dictionary to context
        context["form"] = form
    
        return render(request, "edit_profile.html", context)
    else:
        messages.error(request,"You cannot access other user profile")
        return redirect("profile")