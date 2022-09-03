from django import forms
from .models import Court, Sport, Equipment, Booking , Slot

class AddSportForm(forms.ModelForm):
    class Meta:
        model = Sport
        fields = ['name','img_url']

class AddCourtForm(forms.ModelForm):
    class Meta:
        model = Court
        fields = ["sport",'name',]

class AddEquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ["sport",'name',"quantity"]

class AddSlotForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = ["start_time",'end_time',"date","court"]       