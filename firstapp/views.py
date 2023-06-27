from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from firstapp.models import Theme
from django.contrib.admin.models import LogEntry
# Create your views here.

## Home page view
@login_required
def home(request):
    theme = theme_custom(request)
    logs = LogEntry.objects.filter(user_id=request.user.id) ## This retrives the Log entry of the User
    return render(request, 'home.html', {'color':theme,'log':logs,})

### User Registration view
from .forms import SignUpForm, User_edit, profile_edit
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration.html', {'form': form})

### user Profile view
from firstapp.encryption_util import *
@login_required
def profile(request):
    theme = theme_custom(request)
    lst = User.objects.filter(username=request.user).values('id')
    l=[]
    for i in lst: ## This will encrypt the Url for each User, So that the sensitive information is secure
        i['encrypt_key']=encrypt(i['id'])
        i['id']=i['id']
        l.append(i)
    return render(request, 'profile/profile.html', {'lst':l,'color':theme,})

# Profile Update view
from django.shortcuts import redirect, render, get_object_or_404
@login_required
def profile_update(request):
    theme = theme_custom(request)
    if request.method == 'POST':
        u_form = User_edit(request.POST, instance=request.user)
        p_form = profile_edit(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile updated successfully!')
            return redirect('profile')
    else:
        u_form = User_edit(instance=request.user)
        p_form = profile_edit(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'color':theme,
    }
    return render(request, 'profile/edit_profile.html', context)

### Disable User view
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

def ui_elements(request):
    return render(request, 'UI/ui_elements.html')