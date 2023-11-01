# events/views.py
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'index.html')


# def event_list(request):
#     events = Event.objects.order_by('event_time')
#     return render(request, 'events/event_list.html', {'events': events})