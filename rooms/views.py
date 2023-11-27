# Create your views here.
# rooms/views.py
from django.shortcuts import render, redirect,get_object_or_404, HttpResponseRedirect
# from .forms import roomForm
from .models import Hotel,HotelBooking
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from PaymentApp import views
from django.db.models import Q

def Accomodation(request):
    hotels_objs = Hotel.objects.order_by('hotel_price')
    context = {'hotels_objs' : hotels_objs }
    return render(request ,  'rooms/room_list.html' ,context)


def check_booking(start_date  , end_date ,uid , room_count):
    qs = HotelBooking.objects.filter(
        start_date__lte=start_date,
        end_date__gte=end_date,
        hotel__uid = uid
        )
    
    if len(qs) >= room_count:
        return False
    
    return True

def hotel_detail(request,room_id):
    hotel_obj = Hotel.objects.get(uid = room_id)
    already_registered = False
    if request.user.is_authenticated:
        user = request.user
        already_registered = HotelBooking.objects.filter(user=user, uid = room_id).exists()
    if request.method == 'POST':
        checkin = request.POST.get('checkin')
        checkout= request.POST.get('checkout')
        hotel = Hotel.objects.get(uid = room_id)
        
        if not check_booking(checkin ,checkout  , room_id , hotel.available_rooms):
            messages.warning(request, 'Hotel is already booked in these dates ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        HotelBooking.objects.create(hotel=hotel , user = request.user , start_date=checkin
        , end_date = checkout , booking_type  = 'Pre Paid')
        
        messages.success(request, 'Your booking has been saved')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

           
    context = {'hotels_obj' : hotel_obj , 'already_registered': already_registered}

    return render(request , 'rooms/room_details.html' , context)



@login_required
def user_registered_rooms(request):
    user = request.user
    hotels_objs = Hotel.objects.filter(hotel_bookings__user=user)
    return render(request, 'rooms/registered_rooms.html', {'hotels_objs' : hotels_objs})
