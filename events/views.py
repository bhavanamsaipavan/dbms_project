

# Create your views here.
# events/views.py
from django.shortcuts import render, redirect,get_object_or_404
from .forms import EventForm
from .models import Event,Registration
from django.contrib.auth.decorators import login_required
from PaymentApp import views

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Redirect to the event list page
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})


def event_list(request):
    events = Event.objects.order_by('event_time')
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    # Check if the user is already registered for the event
    
    if request.user.is_authenticated:
        user = request.user
        already_registered = Registration.objects.filter(user=user, event=event).exists()
    else:
        user = None
        already_registered = False

    return render(request, 'events/event_details.html', {
        'event': event,
        'already_registered': already_registered
    })
    
    
@login_required
def register_for_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    user = request.user

    # Check if the user is already registered for the event
    if Registration.objects.filter(user=user, event=event).exists():
        # You may want to display a message saying the user is already registered
        pass
    else:
        return views.CheckOut(request, event_id)
        # Optionally, you can also display a success message

    return redirect('event_detail', event_id=event_id)  # Redirect to the event detail page

@login_required
def user_registered_events(request):
    user = request.user
    registered_events = Event.objects.filter(registration__user=user)
    return render(request, 'events/registered_events.html', {'registered_events': registered_events})
