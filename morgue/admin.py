from django.contrib import admin
from .models import Corpse, Gender, Next_of_kin, Room, TypeOfCorpse, Care_taker

class CorpseAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'gender', 'date_of_death', 'date_of_admission' )
admin.site.register(Corpse, CorpseAdmin)

class GenderAdmin(admin.ModelAdmin):
    list_display = ('gender',)
admin.site.register(Gender, GenderAdmin)

class TypeOfCorpseAdmin(admin.ModelAdmin):
    list_display = ('type',)
admin.site.register(TypeOfCorpse, TypeOfCorpseAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_no', 'care_taker', 'no_of_shelves')
admin.site.register(Room, RoomAdmin)

class Next_of_kinAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',)
admin.site.register(Next_of_kin, Next_of_kinAdmin)

class Care_takerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone')
admin.site.register(Care_taker, Care_takerAdmin)


# class AppointmentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'doctor', 'patient', 'date', 'time')
# admin.site.register(Appointment, AppointmentAdmin)
