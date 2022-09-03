from django.shortcuts import render, redirect
from .models import Equipment, Sport, Court
from .forms import  AddSportForm, AddCourtForm, AddEquipmentForm, AddSlotForm
from django.db.models import Q
from django.contrib import messages

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

def slot_book(request):
    return render(request,'sports/slot_book.html')   