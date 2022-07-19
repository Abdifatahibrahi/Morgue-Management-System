from django.contrib import admin
from .models import Corpse, Gender

class CorpseAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'gender', 'date_of_death', 'date_of_admission' )
admin.site.register(Corpse, CorpseAdmin)

class GenderAdmin(admin.ModelAdmin):
    list_display = ('gender',)
admin.site.register(Gender, GenderAdmin)


# class AppointmentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'doctor', 'patient', 'date', 'time')
# admin.site.register(Appointment, AppointmentAdmin)
