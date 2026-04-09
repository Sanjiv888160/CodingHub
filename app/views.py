from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth



#@login_required(login_url='login')
def index_page(request):
    return render(request, 'app/index.html')

def Dashboard(request):
    return render(request, 'app/dashboard.html')

def About_page(request):
    return render(request, 'app/about.html')


def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        # Check credentials
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Credentials correct → login and redirect to dashboard
            login(request, user)
            return redirect('dashboard')
        else:
            # Credentials wrong → show error
            messages.error(request, 'Username or password is invalid')

    # GET request or failed login
    return render(request, 'app/login.html')
def RegisterPage(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname', '')  # ✅
        lastname  = request.POST.get('lastname', '')
        email     = request.POST.get('email', '')
        username  = request.POST.get('username', '')
        password  = request.POST.get('password', '')
        cpassword = request.POST.get('cpassword', '')

       
        user_obj = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=firstname,
            last_name=lastname
        )
        return redirect('login')

    return render(request, 'app/register.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(name, email, message)  # test

    return render(request, 'app/contact.html')

def logout(request):
    logout(request)
    return redirect('login')
                





