from django.shortcuts import render, redirect, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse,HttpResponseRedirect
from .forms import signupForm,EditprofileForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib import auth


# Create your views here.

def booking(request):
    return render(request,'booking/booking.html')



def login(request):
    if request.method == "POST":
        username = request.POST['user']
        password = request.POST['password']
        try:
            user = auth.authenticate(username=User.objects.get(email=username), password=password)
        except:
            user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Oops! Your username/email address or password is incorrect')
            return HttpResponseRedirect('/accounts/login/')
    else:
        return render(request, 'accounts/login.html')

def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(first_name=first_name,last_name=last_name,
                username=username, email=email, password=password)
            messages.success(request, 'Signup Successfully ')
            return redirect('signup')
    else:
        form = signupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('home')

@login_required(login_url='/accounts/login')
def view_profile(request):
    args={'user':request.user}
    return render(request,'accounts/profile.html',args)

@login_required(login_url='/accounts/login')
def edit_profile(request):
    if request.method == 'POST':
        form = EditprofileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = EditprofileForm(instance=request.user)
        args = {'form':form}
        return render(request,'accounts/edit_profile.html',args)

@login_required(login_url='/accounts/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/accounts/profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_change.html', {
        'form': form
    })

