

# Create your views here.
# events/views.py
from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Redirect to the event list page
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})


def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})
