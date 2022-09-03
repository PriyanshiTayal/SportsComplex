from django.contrib import admin
from .models import Sport, Equipment, Court, Slot, Booking
# Register your models here.

class SportAdmin(admin.ModelAdmin):
    list_display = ('name',)

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('sport','name','quantity')

class CourtAdmin(admin.ModelAdmin):
    list_display = ('name','sport')

class SlotAdmin(admin.ModelAdmin):
    list_display = ('court','date','start_time','end_time')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('time_slot','booked_by')

admin.site.register(Sport,SportAdmin)
admin.site.register(Equipment,EquipmentAdmin)
admin.site.register(Court,CourtAdmin)
admin.site.register(Slot,SlotAdmin)
admin.site.register(Booking,BookingAdmin)