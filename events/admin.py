

# Register your models here.

from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_description', 'event_time', 'event_location', 'event_image')  # Customize displayed fields in the admin

# Optionally, you can add customization for the admin panel display and behavior for the Event model.
