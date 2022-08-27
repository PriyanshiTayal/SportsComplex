from django.contrib import admin
from .models import Sport
# Register your models here.

class SportAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Sport,SportAdmin)