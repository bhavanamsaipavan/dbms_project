# views.py

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login,logout
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from web import views

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'Welcome to Entertinment-District!'
            message = f"""
Dear {form.cleaned_data["username"]},

Thank you for registering with Entertainment District! We are excited to welcome you to our community.

Your account has been successfully created, and you can now [mention any specific actions they can take, such as logging in or exploring your platform]. We appreciate your trust in us and are committed to providing you with a seamless and enjoyable experience.

If you have any questions or encounter any issues, please don't hesitate to reach out to our support team at support@ED.com or contact us directly at 630-178-0884.

Once again, welcome to Entertainment District! We look forward to having you as part of our community.

Best regards,
Darksoul
Entertainment District
Contact Information: 630-178-0884
"""
            from_email = 'vinaycherupally1@gmail.com'  # Replace with your admin email address
            recipient_list = [form.cleaned_data["email"]] # Replace with your admin email address

            send_mail(subject, message, from_email, recipient_list)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(views.home)
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login') 


