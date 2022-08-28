from django.shortcuts import render
from .models import Sport

# Create your views here.
def home(request):
    sports = Sport.objects.all()
    return render(request,'sports/home.html',{'sports':sports})

def slot_book(request):
    return render(request,'sports/slot_book.html')