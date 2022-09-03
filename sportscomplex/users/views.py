from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required

from sports.models import Court, Sport, Equipment, Booking , Slot

from .forms import UserRegisterForm, UserUpdateForm
from .models import Staff, Member
from django.contrib.auth.models import User

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

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f' Your Account has been Updated Successfully!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        bookings = Booking.objects.filter(booked_by = request.user)
    context={
        'u_form':u_form,
        'bookings':bookings
    }
    print(bookings)
    return render(request, 'users/profile.html', context)

@login_required
def add_staff(request):
    if request.method == 'POST':
        try:
            user_id = request.POST.get('staff')
            user = User.objects.filter(id = user_id).first()
            member = Member.objects.get(user = user)
            member.delete() 
            staff = Staff.objects.create(user = user)
            staff.save()
            messages.success(request, f'Staff Added Successfully!')
            return redirect('add_staff')
        except:
            messages.error(request, f'Staff Already exists!')
            return redirect('add_staff')
    else:
        users = User.objects.all()
        return render(request,'users/add_staff.html',{'users':users})

@login_required
def remove_staff(request):
    if request.method == 'POST':
        try:
            staff= request.POST.get('staff')
            user = User.objects.filter(username = staff).first()
            staff = Staff.objects.get(user = user)
            staff.delete()
            member = Member.objects.create(user = user)
            member.save()
            messages.success(request, f'Staff Removed Successfully!')
            return redirect('remove_staff')
        except:
            messages.error(request, f"Staff doesn't exist Already!")
            return redirect('remove_staff')
    else:
        staff = Staff.objects.all()
        return render(request,'users/remove_staff.html',{'staffs':staff}) 

