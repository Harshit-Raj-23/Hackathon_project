from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def fashion(request):
    return render(request, 'index.html')

def styling(request):
    return render(request, 'styling.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.warning(request, "Oops12 User does not exist.")
            return redirect('sign_up')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.warning(request, "Incorrect password.")
            return redirect('log_in')
        
        else:
            login(request, user)
            return redirect('fashion')
    
    return render(request, "login.html")

def log_out(request):
    logout(request)
    return redirect('fashion')

def sign_up(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.warning(request, "Username already taken.")
            return redirect('faculty_register')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
            )
        
        user.set_password(password)
        user.save()

        messages.success(request, "Account created successfully.")
        login(request, user)
        
        return redirect('faculty')
    
    return render(request, 'signup.html')