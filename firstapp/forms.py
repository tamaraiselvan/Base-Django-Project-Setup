from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from firstapp.models import Profile

### This is the Sign Up Form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter First name'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter last name'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter Email address'}), required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter username'}), required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter Password','aria-describedby':"password1-visible"}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'ReEnter Password','aria-describedby':"reenter-password-visible"}), required=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    ### This is used to check if the registering email is exists in the database or not.
    def clean_email(self):
        email = self.cleaned_data.get("email")
        user_count = User.objects.filter(email=email).count()
        if user_count > 0:
            raise forms.ValidationError("This email is already exists.")
        return email
        
### This is the User editing form        
class User_edit(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter First name'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter last name'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter Email address'}), required=True)
    class Meta:
        model = User
        fields=['email','first_name','last_name',]

### This is the Profile editing form
class profile_edit(forms.ModelForm):
    profile_img = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control', 'onchange':'preview()','id':'formFile'}))

    class Meta:
        model = Profile
        fields=['profile_img']