from django.contrib import admin
from .models import Admin, Staff, Member

# Register your models here.
class AdminAdmin(admin.ModelAdmin):
    list_display = ('user',)

class StaffAdmin(admin.ModelAdmin):
    list_display = ('user',)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(Admin,AdminAdmin)
admin.site.register(Staff,StaffAdmin)
admin.site.register(Member,MemberAdmin)