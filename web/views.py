#web/views.py
from django.shortcuts import render

app_name = 'web'

def home(request):
    return render(request, 'index.html')

def contactus(request):
    return render(request, 'contactus.html')
