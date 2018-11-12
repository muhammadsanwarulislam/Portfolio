from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,UserUpdateForm,UserProfileUpdateForm,UserContactForm
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'This account has been created for {username} !')
            return redirect('login-page')
    else:
        form = UserRegistrationForm()
    context ={
        'form':form
    }
    return render(request,'user/register.html',context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'user/profile.html', context)

def contact(request):
    if request.method == 'POST':
        form = UserContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your message successfully sent')
            return redirect('contact-page')
    else:
        form = UserContactForm()
    context = {
        'form':form
    }
    return render(request,'user/contact.html',context)

def about(request):
    user = User.objects.get(username ='muhammad')
    context = {
        'user':user
    }
    return render(request,'user/about.html',context)