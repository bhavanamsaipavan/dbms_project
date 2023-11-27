from django.shortcuts import render, redirect
from events.models import Event
from events.views import Registration
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def CheckOut(request, event_id):

    event = Event.objects.get(id=event_id)
    print(event_id)
    host = request.get_host()
    cost = event.event_fee
    if cost == 0 :
         user = request.user
         Registration.objects.create(user=user, event=event)
         return redirect('event_detail', event_id=event_id)  

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': cost,
        'item_name': event.event_name,
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('payment-success', kwargs = {'event_id': event.id})}",
        'cancel_url': f"http://{host}{reverse('payment-failed', kwargs = {'event_id': event.id})}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    context = {
        'event': event,
        'paypal': paypal_payment
    }

    return render(request, 'checkout.html', context)

def PaymentSuccessful(request, event_id):
    event = Event.objects.get(id=event_id)
    user = request.user
    Registration.objects.create(user=user, event=event)

    return redirect('event_detail', event_id=event_id)  

def paymentFailed(request, Event_id):

    event = Event.objects.get(id=Event_id)

    return render(request, 'payment-failed.html', {'event': event})