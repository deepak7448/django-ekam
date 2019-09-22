from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail,EmailMessage
from django.template.loader import get_template
from django.conf import settings
from hotel.models import feedback
from hotel.forms import feedbackForm
from .forms import contactForm
from .models import contact


def contact(request):
    contact = contactForm
    if request.method == 'POST':
        form = contact(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            subjects = request.POST.get('subjects')
            email = request.POST.get('email')
            messages = request.POST.get('messages')
            template = get_template('contact/contact.txt')
            context = {'name' : name,'phone' : phone,'subjects' : subjects,'email' : email,'messages' : messages,}
            content = template.render(context)
            email = EmailMessage("Ekam villas & resort",content,"Ekam villas",['prajapatideepak244@gmail.com'],
            headers = { 'Reply To': email })
            email.send()
            form.save()
            return redirect('contact')
    else:
        form = contactForm()
        context = {'form':form}
    return render(request, 'contact/contact.html',context)

def contact_feedback(request):
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            feedback_name = request.POST.get('feedback_name')
            feedback_email = request.POST.get('feedback_email')
            feedback = request.POST.get('feedback')
            template = get_template('contact/feedback.txt')
            context = {'feedback_name' : feedback_name,'feedback_email' : feedback_email,'feedback' : feedback,}
            content = template.render(context)
            email = EmailMessage("Ekam Feedback",content,"Ekam villas",['prajapatideepak244@gmail.com'],
            headers = { 'Reply To': feedback_email })
            email.send()
            form.save()
            return redirect('contact')
    else:
        form = feedbackForm()
        #context = 
    return render (request,'contact/contact.html',{'form':form})