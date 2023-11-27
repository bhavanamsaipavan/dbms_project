

# Register your models here.

from django.contrib import admin
from .models import Hotel,HotelBooking

@admin.register(Hotel)
class roomAdmin(admin.ModelAdmin):
    list_display = ('hotel_name','hotel_price', 'description','amenities','room_count','room_image','available_rooms')  # Customize displayed fields in the admin

@admin.register(HotelBooking)
class roomAdmin(admin.ModelAdmin):
    list_display = ('hotel','user', 'start_date','end_date','booking_type')
# Optionally, you can add customization for the admin panel display and behavior for the room model.
