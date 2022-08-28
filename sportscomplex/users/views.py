from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from .forms import UserRegisterForm


# Create your views here.
def login(request):
    return render(request, 'users/login.html')
 
def dologin(request):
     
    print("here")
    username = request.GET.get('username')
    password = request.GET.get('password')

    print(username)
    print(password)
    print(request.user)
    if not (username and password):
        messages.error(request, "Please provide all the details!!")
        return render(request, 'users/login.html')
 
    user = authenticate(username=username, password=password)
    if user is None:
        messages.error(request, 'Invalid Login Credentials!!')
        return render(request, 'users/login.html')
 
    auth_login(request, user)
    print(request.user)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()                            
            messages.success(request, f'Your Account has been Created Successfully. Now LogIn to explore!')
            return redirect('login')           
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html', {'form': form})

def profile(request):
    return render(request, 'users/profile.html')