#from django.contrib import admin
#from .models import Room, Faculty, Tutor

#admin.site.register(Room)
#admin.site.register(Faculty)
#admin.site.register(Tutor)

from django.contrib import admin
from .models import Room, Faculty, Tutor

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'building')  # Fields to show in the list view
    search_fields = ('number', 'building')  # Enable search by these fields
    list_filter = ('building',)  # Add a filter for building

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'dean')  # Fields to show in the list view
    search_fields = ('name', 'dean')  # Enable search by these fields

from django.contrib import admin
from .models import Tutor, Room, Faculty

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ['forenames', 'surname', 'email']
    search_fields = ['forenames', 'surname', 'email']

