from django.shortcuts import render, redirect,HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm


def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            # Send email to admin
            subject = 'New Contact Form Submission'
            message = f'Name: {form.cleaned_data["name"]}\nEmail: {form.cleaned_data["email"]}\nSubject: {form.cleaned_data["subject"]}\nQuery:\n{form.cleaned_data["query"]}'
            from_email = 'vinaycherupally1@gmail.com'  # Replace with your admin email address
            recipient_list = ['cse220001021@iiti.ac.in']  # Replace with your admin email address

            send_mail(subject, message, from_email, recipient_list)

            # Redirect to thank you page
            return HttpResponse('thank_you')
    else:
        form = ContactForm()

    return render(request, 'contactus.html', {'form': form})
