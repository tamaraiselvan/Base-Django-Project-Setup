from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from firstapp.models import Theme
# Create your views here.
@login_required
def home(request):
    theme = theme_custom(request)
    return render(request, 'home.html', {'color':theme})

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

@login_required
def profile(request):
    theme = theme_custom(request)
    lst = User.objects.filter(username=request.user).values('id')
    l=[]
    for i in lst:
        i['encrypt_key']=encrypt(i['id'])
        i['id']=i['id']
        l.append(i)
    return render(request, 'profile/profile.html', {'lst':l,'color':theme,})

from django.shortcuts import redirect, render, get_object_or_404
from firstapp.encryption_util import *
@login_required
def update(request,id):
    id=decrypt(id)
    theme = theme_custom(request)
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
    
        return render(request, "profile/edit_profile.html", {'form':form,'color':theme,})
    else:
        messages.error(request,"You cannot access other user profile")
        return redirect("profile")

# disable view for details
from django.contrib.auth import logout
@login_required
def disable_user(request, id):
    theme = theme_custom(request)
    # fetch the object related to passed id
    obj = get_object_or_404(User, id = request.user.id)

    if request.method =="POST":
        # disable object
        obj.is_active=False
        obj.save()
        logout(request)
        messages.success(request, 'Profile successfully disabled.')
        return redirect('login')
 
    return render(request, "profile/disable_acc.html", {'color':theme,})

def theme_custom(request):
    if Theme.objects.filter(user=request.user).exists():
        color = Theme.objects.get(user=request.user).color
    else:
        color = 'light'
    
    return color 

from django.urls import resolve
from django.http import HttpResponseRedirect
def theme(request):
    color = request.GET.get('color')
    current_url = resolve(request.path_info).url_name
    # previous_url = self.request.META.get('HTTP_REFERER')
    if color == 'dark':
        if Theme.objects.filter(user=request.user).exists():
            user_theme = Theme.objects.get(user=request.user)
            user_theme.user = request.user
            user_theme.color = 'dark'
            user_theme.save()
        else:
            user2 = Theme(user=request.user, color='dark')
            user2.save()

    elif color == 'light':
        if Theme.objects.filter(user=request.user).exists():
            user_theme1 = Theme.objects.get(user=request.user)
            user_theme1.user = request.user
            user_theme1.color = 'light'
            user_theme1.save()
        else:
            user4 = Theme(user=request.user, color='light')
            user4.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))