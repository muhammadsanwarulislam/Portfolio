# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import Profile,Contact

# class UserRegistrationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username','email','password1','password2']

# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username','email']

# class UserProfileUpdateForm(forms.ModelForm):
#     class Mata:
#         model = Profile
#         fields = "__all__"


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Contact


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['pro_img','designation','location']

class UserContactForm(forms.ModelForm):
    class Meta:
        model  = Contact
        fields = ['email','subject','message']
