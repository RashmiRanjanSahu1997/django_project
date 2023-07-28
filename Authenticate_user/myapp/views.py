from .utils import *
from django.shortcuts import  redirect, render
from .form import  UserForm ,UpdateProfile
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import *

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, ("Registration Successful!"))
            return redirect('login_view')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('data')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    context = {
        "form": form
    }
    
    return render(request, "login.html", context)

"""LogOut Page"""
def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out!"))
    return redirect("login_view")

def logout_user(request):
        
        logout(request)
        messages.success(request, "You Were Logged Out!")
          # Replace 'login_view' with the name of your login page URL
        return render(request, "logout.html")

def update_profile(request):
    args = {}
    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=request.user)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = UpdateProfile(instance=request.user)

    args['form'] = form
    return render(request, 'update_profile.html', args)

def userdata(request):
    users = User.objects.all()  # Query all user instances from the database
    return render(request, 'employeedata.html', {'rashmi':users})