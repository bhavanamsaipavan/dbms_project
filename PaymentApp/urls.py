from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<int:event_id>/', views.CheckOut, name='checkout'),
    path('payment-success/<int:event_id>/', views.PaymentSuccessful, name='payment-success'),
    path('payment-failed/<int:event_id>/', views.paymentFailed, name='payment-failed'),
]