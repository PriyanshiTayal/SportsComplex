from django.shortcuts import render, redirect
from .models import Equipment, Sport, Court, Slot, Booking
from .forms import  AddSportForm, AddCourtForm, AddEquipmentForm, AddSlotForm
from django.db.models import Q
from django.contrib import messages
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required

import datetime

# Create your views here.
def home(request):
    search_term = ''

    if 'search' in request.GET:
        search_term = request.GET['search']
        sports = Sport.objects.all().filter(Q(name__icontains =search_term)) 

    else:
        sports = Sport.objects.all()
    return render(request,'sports/home.html',{'sports':sports})

def sport_page(request,sport):
    sport_name = Sport.objects.get(name = sport)
    equipments = Equipment.objects.filter(sport = sport_name)
    courts = Court.objects.filter(sport = sport_name)
    return render(request, "sports/sport_page.html", {'equipments':equipments, 'sport':sport_name, 'courts':courts})

@login_required
def add_sport(request):
    if request.method == 'POST':
        form = AddSportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Sport Added Successfully!')
            return redirect('add_sport')          
    else:
        form = AddSportForm()
    return render(request,'sports/add_sport.html', {'form': form})       

@login_required
def add_court(request):
    if request.method == 'POST':
        form = AddCourtForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Court Added Successfully!')
            return redirect('add_court')
        else:
            messages.error(request, f"Court couldn't be added!")
            return redirect('add_court')
    else:

        form = AddCourtForm()
        return render(request,'sports/add_court.html',{'form': form})

@login_required
def add_equipment(request):
    if request.method == 'POST':
        form = AddEquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Equipment Added Successfully!')
            return redirect('add_equipment')
        else:
            messages.error(request, f"Equipment couldn't be added!")
            return redirect('add_equipment')
    else:
        form = AddEquipmentForm()
        return render(request,'sports/add_equipment.html',{'form': form}) 
@login_required
def add_slot(request):
    if request.method == 'POST':
        form = AddSlotForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Slot Added Successfully!')
            return redirect('add_slot')
        else:
            messages.error(request, f"Slot couldn't be added!")
            return redirect('add_slot')
    else:
        form = AddSlotForm()
        return render(request,'sports/add_slot.html',{'form': form}) 



def available_slot(request,court):  
    court = Court.objects.get(name = court)  
    today_date = date.today()
    tomm1_date = today_date+timedelta(1)
    tomm2_date = today_date+timedelta(2)

    today_slots = Slot.objects.filter(date = today_date,court = court)
    tomm1_slots = Slot.objects.filter(date = tomm1_date, court = court)
    tomm2_slots = Slot.objects.filter(date = tomm2_date, court = court)
    today = []
    tomm1 = []
    tomm2 = []
    for slot in today_slots:
        if not hasattr(slot, 'booking'):
            today.append(slot)
    for slot in tomm1_slots:
        if not hasattr(slot, 'booking'):
            tomm1.append(slot)
    for slot in tomm2_slots:
        if not hasattr(slot, 'booking'):
            tomm2.append(slot)        

    context = {
        'court': court,
        'today_slots': today,
        'tomm1_slots': tomm1,
        'tomm2_slots': tomm2,
        'today': today_date,
        'tomm1':tomm1_date,
        'tomm2':tomm2_date
    }
    
    return render(request,'sports/available_slot.html', context)

@login_required
def slot_book(request, slot_id):
    slot = Slot.objects.get(id = slot_id)
    if request.method == 'POST':
        Slot.objects.filter(date__lt = date.today()).delete()
        bookings = Booking.objects.filter(booked_by = request.user).count()
        if bookings<3:
            try:
                booking = Booking.objects.create(time_slot = slot, booked_by = request.user)
                booking.save()
                messages.success(request, f'Slot Booked Successfully!')
                return redirect('home')
            except:
                messages.error(request, f"Slot couldn't be booked!")
                return redirect('home')
        else:
            messages.error(request, f"Sorry! You can't book more than 3 Slots")
            return redirect('home')
    else:       
        return render(request,'sports/slot_book.html',{'slot':slot}) 

@login_required
def member_bookings(request):
    bookings = Booking.objects.filter(booked_by = request.user)
    return render(request, 'sports/member_bookings.html', {'bookings':bookings})

@login_required
def sport_bookings(request, sport):
    sport = Sport.objects.get(name = sport)
    courts = Court.objects.filter(sport = sport)
    bookings = []
    for court in courts:
        slots = Slot.objects.filter(court = court)
        for slot in slots:
            if hasattr(slot, 'booking'):
                bookings.append(slot)
    return render(request, 'sports/sport_bookings.html', {'slots':bookings})

@login_required
def all_bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'sports/all_bookings.html', {'bookings':bookings})

@login_required
def delete_booking(request,booking_id):
    if request.method == 'POST':        
        try:
            Booking.objects.get(id = booking_id).delete()
            messages.success(request, f'Booking Deleted Successfully!')
            return redirect('all_bookings')
        except:
            messages.error(request, f"Booking couldn't be deleted!")
            return redirect('all_bookings')
    else: 
        booking = Booking.objects.get(id = booking_id)     
        return render(request,'sports/delete_booking.html',{'booking':booking}) 
